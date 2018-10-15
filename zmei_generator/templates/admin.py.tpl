
{{ imports }}

{% for cname, col in collections %}
class {{ col.class_name }}ModelForm(forms.ModelForm):
    class Meta:
        model = {{ col.class_name }}
        exclude = ()
        widgets = {
    {% for field in col.fields.values() %}{% if field.get_admin_widget() %}'{{ field.name }}': {{ field.get_admin_widget().declaration }},{% endif %}{% endfor %}
    }

{% for inline in col.admin.inlines %}{% if inline.collection == col %}
class {{ inline.class_name }}({{ inline.parent_classes|join(', ') }}):
    model  = {{ inline.target_collection.class_name }}{% if inline.tab %}
    suit_classes = 'suit-tab suit-tab-{{ inline.tab }}'
    {% endif %}{% if inline.target_collection.sortable %}
    sortable = {{ inline.target_collection.sortable_field.0|repr }}
    {% endif %}{% if not inline.inline_type == 'polymorphic' %}
    extra = {{ inline.extra_count }}
    fk_name = '{{ inline.source_field_name }}'
    fields = [{{ inline.field_set|field_names() }}]
    {% else %}{% for col in inline.target_collection.child_collections %}
    class {{ col.class_name }}{{ inline.class_name }}({% if col.translatable %}TranslatableInlineModelAdmin, {% endif %}{{ inline.parent_classes[0] }}.Child):
        model = {{ col.class_name }}
        suit_classes = 'suit-tab suit-tab-{{ inline.tab }}'{% endfor %}

    child_inlines = ({% for col in inline.target_collection.child_collections %}
        {{ col.class_name }}{{ inline.class_name }},{% endfor %}
    )
    {% endif %}
{% endif %}{% endfor %}

class {{ col.class_name }}Admin({{ col.admin.class_declaration }}):
    """
    #{{ col.ref }}
    {{ col.class_name }} Admin
    """

    {% if col.polymorphic and col.tree_polymorphic_list %}
    polymorphic_list = True
    {% endif %}

    {# ***** POLYMORPHIC ********* #}
    {% if col.polymorphic or col.parent %}
    base_model = {{ col.class_name }}
    {% endif %}
    {% if col.polymorphic %}
    child_models = ({{ col.child_model_classes|join(', ') }},)
    {% endif %}
    {% if col.sortable %}
    sortable = {{ col.sortable_field[0]|repr }}
    {% endif %}



    {% if col.prepopulated_fields %}
    prepopulated_fields = {{ col.prepopulated_fields |repr }}
    {% endif %}

    {% if col.admin.read_only %}
    readonly_fields = ({{ col.admin.read_only|field_names(admin=True) }},)
    {% endif %}

    {% if col.date_hierarchy %}
    date_hierarchy = '{{ col.date_hierarchy }}'
    {% endif %}

    {# ***** TABS & FIELDS ********* #}
{% if not col.polymorphic %}
    form = {{ col.class_name }}ModelForm

    {% if col.admin.tabs %}
    suit_form_tabs = ({% for tab in col.admin.tabs %}
        ('{{ tab }}', '{{ col.admin.tab_names.get(tab)|to_name }}'),{% endfor %}
    )

    fieldsets = ({% for tab in col.admin.tabs %}{% if col.admin.fields_for_tab(tab) %}
        (None, {
            'classes': ('suit-tab', 'suit-tab-{{ tab }}',),
            'fields': [{{ col.admin.fields_for_tab(tab)|field_names(admin=False) }}]
        }),{% endif %}{% endfor %})

    {{ col.render_tabs }}
    {% elif col.admin.fields %}
    fields = [{{ col.admin.fields|field_names(admin=False) }}]
    {% endif %}

    {# ***** INLINES ********* #}
    {% if col.admin.inlines %}
    inlines = [{{ col.admin.inline_classes|join(', ') }}]
    {% endif %}

{% endif %}

{% if col.admin.admin_list %}
    list_display = [{% if col.tree %}'tree_actions', 'indented_title',{% else %}{% endif %}{{ col.admin.admin_list|field_names(admin=True) }}]
    {% if col.admin.list_editable %}
    list_editable = [{{ col.admin.list_editable|field_names(admin=False) }}]
    {% endif %}
    {% if col.admin.list_filter %}
    list_filter = [{{ col.admin.list_filter|field_names(admin=False) }}]
    {% endif %}
    {% if col.admin.list_search %}
    search_fields = [{{ col.admin.list_search|field_names(admin=False) }}]
    {% endif %}

    {% for field in col.admin.list %}
    {% if field.admin_list_renderer %}
    def get_{{ field.name }}(self, obj):
        {{ field.admin_list_renderer }}
    get_{{ field.name }}.short_description = {{ field.verbose_name|repr }}
    get_{{ field.name }}.allow_tags = True
    {% endif %}

    {% endfor %}
{% endif %}

    {% for field in col.expression_fields %}
    {% if field.admin_list_renderer %}
    def get_{{ field.name }}(self, obj):
        {{ field.admin_list_renderer }}
    get_{{ field.name }}.short_description = {{ field.verbose_name|repr }}
    get_{{ field.name }}.allow_tags = True{% if field.boolean %}
    get_{{ field.name }}.boolean = True{% endif %}
    {% endif %}
    {% endfor %}

    {% if col.admin.js or col.admin.css %}
    class Media:{% if col.admin.css %}
        css = {"all": {{ col.admin.css|repr }} }
        {% endif %}{% if col.admin.js %}
        js = {{ col.admin.js|repr }}
        {% endif %}
    {% endif %}


admin.site.register({{ col.class_name }}, {{ col.class_name }}Admin)
{% endfor %}