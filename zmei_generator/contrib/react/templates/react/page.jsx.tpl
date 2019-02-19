{{ imports }}
import {connect} from "react-redux";
import axios from "axios";
import {withRouter} from "react-router-dom";
import {PageContextProvider, reloadPageDataAction} from "../../state";{% if streams %}
import {streamEnterAction, streamLeaveAction} from "../../streams";{% endif %}
import { reverse } from "named-urls";
import { routes } from '../../router'

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
    renderContent = () => <p>Nothing here!</p>;
    {% endif %}
    {% for area, blocks in blocks.items() -%}
    render{{ area|capitalize }} = () => <>{% for block in blocks -%}
        {{ block|indent(8) }}
    {% endfor %}</>;
    {% endfor %}
}

{{ name }} = connect(
    store => {
        return {store}
    },
    dispatch => {
        return {dispatch}
    },
)({{ name }});

{{ name }} = withRouter({{ name }});

export default {{ name }};
