
{{ imports }}

{% for model_name, model in models %}
class {{ model.class_name }}ModelForm(forms.ModelForm):
    class Meta:
        model = {{ model.class_name }}
        exclude = ()
        widgets = {
    {% for field in model.fields.values() %}{% if field.get_admin_widget() %}'{{ field.name }}': {{ field.get_admin_widget().declaration }},{% endif %}{% endfor %}
    }

{% for inline in model[ext].inlines %}{% if inline.model == model %}
class {{ inline.class_name }}({{ inline.parent_classes|join(', ') }}):
    model  = {{ inline.target_model.class_name }}{% if inline.tab %}
    suit_classes = 'suit-tab suit-tab-{{ inline.tab }}'
    {% endif %}{% if inline.target_model.sortable %}
    sortable = {{ inline.target_model.sortable_field.0|repr }}
    {% endif %}{% if not inline.inline_type == 'polymorphic' %}
    extension = {{ inline.extension_count }}
    fk_name = '{{ inline.source_field_name }}'
    fields = [{{ inline.field_set|field_names() }}]
    {% else %}{% for model in inline.target_model.child_models %}
    class {{ model.class_name }}{{ inline.class_name }}({% if model.translatable %}TranslatableInlineModelAdmin, {% endif %}{{ inline.parent_classes[0] }}.Child):
        model = {{ model.class_name }}
        suit_classes = 'suit-tab suit-tab-{{ inline.tab }}'{% endfor %}

    child_inlines = ({% for model in inline.target_model.child_models %}
        {{ model.class_name }}{{ inline.class_name }},{% endfor %}
    )
    {% endif %}
{% endif %}{% endfor %}

class {{ model.class_name }}Admin({{ model[ext].class_declaration }}):
    """
    #{{ model.ref }}
    {{ model.class_name }} Admin
    """

    {% if model.polymorphic and model.tree_polymorphic_list %}
    polymorphic_list = True
    {% endif %}

    {# ***** POLYMORPHIC ********* #}
    {% if model.polymorphic or model.parent %}
    base_model = {{ model.class_name }}
    {% endif %}
    {% if model.polymorphic %}
    child_models = ({{ model.child_model_classes|join(', ') }},)
    {% endif %}
    {% if model.sortable %}
    sortable = {{ model.sortable_field[0]|repr }}
    {% endif %}



    {% if model.prepopulated_fields %}
    prepopulated_fields = {{ model.prepopulated_fields |repr }}
    {% endif %}

    {% if model[ext].read_only %}
    readonly_fields = ({{ model[ext].read_only|field_names(admin=True) }},)
    {% endif %}

    {% if model.date_hierarchy %}
    date_hierarchy = '{{ model.date_hierarchy }}'
    {% endif %}

    {# ***** TABS & FIELDS ********* #}
{% if not model.polymorphic %}
    form = {{ model.class_name }}ModelForm

    {% if model[ext].tabs %}
    suit_form_tabs = ({% for tab in model[ext].tabs %}
        ('{{ tab }}', '{{ model[ext].tab_names.get(tab)|to_name }}'),{% endfor %}
    )

    fieldsets = ({% for tab in model[ext].tabs %}{% if model[ext].fields_for_tab(tab) %}
        (None, {
            'classes': ('suit-tab', 'suit-tab-{{ tab }}',),
            'fields': [{{ model[ext].fields_for_tab(tab)|field_names(admin=False) }}]
        }),{% endif %}{% endfor %})

    {{ model.render_tabs }}
    {% elif model[ext].fields %}
    fields = [{{ model[ext].fields|field_names(admin=False) }}]
    {% endif %}

    {# ***** INLINES ********* #}
    {% if model[ext].inlines %}
    inlines = [{{ model[ext].inline_classes|join(', ') }}]
    {% endif %}

{% endif %}

{% if model[ext].admin_list %}
    list_display = [{% if model.tree %}'tree_actions', 'indented_title',{% else %}{% endif %}{{ model[ext].admin_list|field_names(admin=True) }}]
    {% if model[ext].list_editable %}
    list_editable = [{{ model[ext].list_editable|field_names(admin=False) }}]
    {% endif %}
    {% if model[ext].list_filter %}
    list_filter = [{{ model[ext].list_filter|field_names(admin=False) }}]
    {% endif %}
    {% if model[ext].list_search %}
    search_fields = [{{ model[ext].list_search|field_names(admin=False) }}]
    {% endif %}

    {% for field in model[ext].list %}
    {% if field.admin_list_renderer %}
    def get_{{ field.name }}(self, obj):
        {{ field.admin_list_renderer }}
    get_{{ field.name }}.short_description = {{ field.verbose_name|repr }}
    get_{{ field.name }}.allow_tags = True
    {% endif %}

    {% endfor %}
{% endif %}

    {% for field in model.expression_fields %}
    {% if field.admin_list_renderer %}
    def get_{{ field.name }}(self, obj):
        {{ field.admin_list_renderer }}
    get_{{ field.name }}.short_description = {{ field.verbose_name or field.name|repr }}
    get_{{ field.name }}.allow_tags = True{% if field.boolean %}
    get_{{ field.name }}.boolean = True{% endif %}
    {% endif %}
    {% endfor %}

    {% if model[ext].js or model[ext].css %}
    class Media:{% if model[ext].css %}
        css = {"all": {{ model[ext].css|repr }} }
        {% endif %}{% if model[ext].js %}
        js = {{ model[ext].js|repr }}
        {% endif %}
    {% endif %}


admin.site.register({{ model.class_name }}, {{ model.class_name }}Admin)
{% endfor %}