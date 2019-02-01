{{ imports }}
import {connect} from "react-redux";
import axios from "axios";
import {reloadPageDataAction} from "../../state";{% if streams %}
import {streamEnterAction, streamLeaveAction} from "../../streams";{% endif %}

class {{ name }} extends React.Component {

    setState = (response) => {
        if (response.data.__error__) throw response.data.__error__;
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
    {%- endif %}

    reload = () => axios.get('').then(this.setState);
    {% for name, func in page.list_own_or_parent_functions().items() %}
    {{ name }} = ({% if func.args %}{{ func.render_python_args() }}{% endif %}) => axios.post('', {'method': '{{ name }}'{% if func.args %}, args: [{{ func.render_python_args() }}]{% else %}{% endif %}}).then(this.setState);
    {%- endfor %}

    render() {
        return (
            {{ source|indent(12) }}
        );
    }
}

{{ name }} = connect(
    store => {
        return {store}
    },
    dispatch => {
        return {dispatch}
    },
)({{ name }});

export default {{ name }};
