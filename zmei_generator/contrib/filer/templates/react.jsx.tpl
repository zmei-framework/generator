{{ imports }}
{% if connect %}import {connect} from "react-redux";{% endif %}

{% if not connect %}export {% endif %}class {{ name }} extends React.Component {
    render() {
        {{ body|indent(8) }}
        return (
            {{ source|indent(12) }}
        );
    }
}
{% if connect %}
{{ name }} = connect(
    store => {
        return {store}
    },
    dispatch => {
        return {dispatch}
    },
)({{ name }});
export { {{ name }} };
{% endif %}
