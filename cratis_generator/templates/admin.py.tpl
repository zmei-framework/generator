
{{ imports }}

{% for cname, col in collections %}
class {{ col.class_name }}ModelForm(forms.ModelForm):
    class Meta:
        model = {{ col.class_name }}
        exclude = ()
        widgets = {
    {% for field in col.fields.values() %}{% if field.get_admin_widget() %}'{{ field.name }}': {{ field.get_admin_widget().declaration }},{% endif %}{% endfor %}
    }

{% for inline in col.admin_inlines %}
class {{ inline.class_name }}({{ inline.parent_classes|join(', ') }}):
    model  = {{ inline.target_collection.class_name }}{% if inline.tab %}
    suit_classes = 'suit-tab suit-tab-{{ inline.tab }}'
    {% endif %}{% if inline.target_collection.sortable %}
    sortable = '{{ inline.target_collection.sortable_field }}'
    {% endif %}{% if not inline.inline_type == 'polymorphic' %}
    extra = {{ inline.extra_count }}
    fk_name = '{{ inline.source_field_name }}'
    fields = [{{ inline.field_names|field_names() }}]
    {% else %}{% for col in inline.target_collection.child_collections %}
    class {{ col.class_name }}{{ inline.class_name }}({% if col.translatable %}TranslatableInlineModelAdmin, {% endif %}{{ inline.parent_classes[0] }}.Child):
        model = {{ col.class_name }}{% endfor %}

    child_inlines = ({% for col in inline.target_collection.child_collections %}
        {{ col.class_name }}{{ inline.class_name }},{% endfor %}
    )
    {% endif %}
{% endfor %}

class {{ col.class_name }}Admin({{ col.admin_class_declaration }}):
    """
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
    sortable = '{{ col.sortable_field }}'
    {% endif %}



    {% if col.prepopulated_fields %}
    prepopulated_fields = {{ col.prepopulated_fields |repr }}
    {% endif %}

    {% if col.read_only_fields %}
    readonly_fields = ({{ col.read_only_fields|field_names(admin=True) }},)
    {% endif %}

    {% if col.date_hierarchy %}
    date_hierarchy = '{{ col.date_hierarchy }}'
    {% endif %}

    {# ***** TABS & FIELDS ********* #}
{% if not col.polymorphic %}
    form = {{ col.class_name }}ModelForm

    {% if col.admin_tabs %}
    suit_form_tabs = ({% for tab in col.admin_tabs %}
        ('{{ tab }}', '{{ col.tab_names.get(tab)|to_name }}'),{% endfor %}
    )

    fieldsets = ({% for tab in col.admin_tabs %}{% if col.fields_for_tab(tab) %}
        (None, {
            'classes': ('suit-tab', 'suit-tab-{{ tab }}',),
            'fields': [{{ col.fields_for_tab(tab)|field_names(admin=False) }}]
        }),{% endif %}{% endfor %})

    {{ col.render_tabs }}
    {% elif col.admin_fields %}
    fields = [{{ col.admin_fields|field_names(admin=True) }}]
    {% endif %}

    {# ***** INLINES ********* #}
    {% if col.admin_inlines %}
    inlines = [{{ col.admin_inline_classes|join(', ') }}]
    {% endif %}

{% endif %}

{% if col.admin_list %}
    list_display = [{% if col.tree %}'tree_actions', 'indented_title',{% else %}{% endif %}{{ col.admin_list|field_names(admin=True) }}]
    {% if col.admin_list_editable %}
    list_editable = [{{ col.admin_list_editable|field_names(admin=False) }}]
    {% endif %}
    {% if col.admin_list_filter %}
    list_filter = [{{ col.admin_list_filter|field_names(admin=False) }}]
    {% endif %}
    {% if col.admin_list_search %}
    search_fields = [{{ col.admin_list_search|field_names(admin=False) }}]
    {% endif %}

    {% for field in col.admin_list %}
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

    {% if col.admin_js or col.admin_css %}
    class Media:{% if col.admin_css %}
        css = {"all": {{ col.admin_css|repr }} }
        {% endif %}{% if col.admin_js %}
        js = {{ col.admin_js|repr }}
        {% endif %}
    {% endif %}


admin.site.register({{ col.class_name }}, {{ col.class_name }}Admin)
{% endfor %}