{{ imports }}
import axios from "axios";
import {PageContextProvider, reloadPageDataAction} from "../../state";{% if streams %}
import {streamEnterAction, streamLeaveAction} from "../../streams";{% endif %}


class {{ name }} extends React.Component {

    handleResponse = (response) => {
        if (response.data.__error__) throw response.data.__error__;
        if (response.data.__redirect__) this.props.history.push(response.data.__redirect__);
        if (response.data.__state__) {
            this.props.dispatch(reloadPageDataAction(response.data.__state__));
            return response.data.__state__;
        }
        return response.data;
    };
    {% if streams %}
    componentDidMount = () => {
        {% for stream in streams -%}
        this.props.dispatch(
            streamEnterAction(window.location.protocol.replace('http', 'ws') + '//' + window.location.host + '/ws/pages/{{ stream.page.application.app_name }}/{{ stream.page.name }}')
        );
        {%- endfor %}
        this.reload();
    };

    componentWillUnmount() {
        setTimeout(() => {
            {% for stream in streams -%}
            this.props.dispatch(
                streamLeaveAction(window.location.protocol.replace('http', 'ws') + '//' + window.location.host + '/ws/pages/{{ stream.page.application.app_name }}/{{ stream.page.name }}')
            );
            {%- endfor %}
        }, 1000);
    }
    {% else %}
    componentDidMount() {
        this.reload();
    }
    {%- endif %}

    reload = () => axios.get('').then(this.handleResponse);
    submit = (data) => axios.post('', data).then(this.handleResponse);
    {% for name, func in page.list_own_or_parent_functions().items() %}
    {{ name }} = ({% if func.args %}{{ func.render_python_args() }}{% endif %}) => axios.post(window.location.href, {'method': '{{ name }}'{% if func.args %}, args: [{{ func.render_python_args() }}]{% else %}{% endif %}}).then(this.handleResponse);
    {%- endfor %}

    render() {
        return (
            {{ source|indent(12) }}
        );
    }
    {% if 'content' not in blocks %}
    renderContent() {
        return <p>Nothing here!</p>;
    }
    {% endif %}
    {% for area, blocks in blocks.items() -%}
    render{{ area|capitalize }}() {
        return <>
        {% for block_ref, block in blocks -%}
            {% if block_ref %}{this.renderBlock{{ to_camel_case(block_ref) }}()}{% else %}{{ block|indent(8) }}{% endif %}
        {% endfor %}</>;
    }
    {% endfor %}

    {% for area, blocks in blocks.items() %}{% for block_ref, block in blocks if block_ref -%}
    renderBlock{{ to_camel_case(block_ref) }}() {
        return {{ block|indent(8) }};
    }
    {% endfor %}{% endfor %}
}

export default {{ name }};
