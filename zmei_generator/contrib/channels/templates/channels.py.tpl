{{ imports }}

channel_layer = get_channel_layer()

{% for page in pages %}
class {{ page.view_name }}Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('page_{{ page.name }}', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('page_{{ page.name }}', self.channel_name)

    {% for stream_model in page[ext].models %}
    async def state_update__{{ stream_model.stream_name }}(self, event):
        if event['wait_db_sync']:
            await sleep(.3)

        serialized_state = await self.get_new_state__{{ stream_model.stream_name }}(
            me=event['instance'],
            url=type('url', (object,), self.scope),
            request=type('request', (object,), self.scope),
            kwargs=self.scope['url_route']['kwargs'],
        )
        if serialized_state:
            await self.send(text_data=serialized_state)

    @database_sync_to_async
    def get_new_state__{{ stream_model.stream_name }}(self, me, url, request, kwargs):
        {%- if stream_model.filter_expr %}
        if not ({{ stream_model.filter_expr }}):
            return
        {% endif %}
        view = {{ page.view_name }}(request=request, kwargs=kwargs)
        data = view.get_data(url, request, inherited=False)
        {%- if stream_model.fields %}
        data = {key:val for key, val in data.items() if key in {{ stream_model.fields|repr }} }
        {% endif %}
        return ZmeiJsonEncoder(view=view).encode({'__state__': data})
    {%- endfor %}


{% for stream_model in page[ext].models %}
@receiver(post_save, sender={{ stream_model.model_class_name }})
@receiver(post_delete, sender={{ stream_model.model_class_name }})
@receiver(post_delete_bulk, sender={{ stream_model.model_class_name }})
@receiver(post_bulk_create, sender={{ stream_model.model_class_name }})
@receiver(post_get_or_create, sender={{ stream_model.model_class_name }})
@receiver(post_update_or_create, sender={{ stream_model.model_class_name }})
@receiver(post_update, sender={{ stream_model.model_class_name }})
@receiver(m2m_changed, sender={{ stream_model.model_class_name }})
def {{ page.name }}_{{ stream_model.model_class_name|lower }}_change_listener(sender=None, signal=None, instance=None, **kwargs):
    async_to_sync(channel_layer.group_send)("page_{{ page.name }}", {
        "type": f"state_update__{{ stream_model.stream_name }}",
        "wait_db_sync": signal not in (post_delete, m2m_changed),
        "instance": instance
    })
{%- endfor %}
{%- endfor %}
