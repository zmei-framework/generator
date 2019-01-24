{{ imports }}
import {connect} from "react-redux";
import axios from "axios";
import ReconnectingWebSocket from 'reconnecting-websocket';

class {{ name }} extends React.Component {

    setState = (response) => {
        if (response.data.__error__) throw response.data.__error__;
        if (response.data.__state__) {
            this.props.dispatch(reloadPageDataAction(response.data.__state__));
            return response.data.__state__;
        }
        return response.data;
    };
    {% if page.stream -%}
    componentDidMount = () => {
        const socket = new ReconnectingWebSocket('ws://' + window.location.host + '/ws/pages' + window.location.pathname);
        socket.onmessage = (e) => this.setState({data: JSON.parse(e.data)});
    };
    {%- endif %}

    reload = () => axios.get('').then(this.setState);
    {% for name, func in page.functions.items() %}
    {{ name }} = ({% if func.args %}{{ func.render_python_args() }}{% endif %}) => axios.post('', {'method': '{{ name }}'{% if func.args %}, args: [{{ func.render_python_args() }}]{% else %}{% endif %}}).then(this.setState);
    {%- endfor %}

    render() {
        {{ body|indent(8) }}
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

export { {{ name }} };
