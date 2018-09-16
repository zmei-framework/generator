{{ imports }}
import {connect} from "react-redux";
import axios from "axios";

class {{ name }} extends React.Component {

    reload = () => axios.get('').then((response) => {
        // var state = {...this.props.store, ...response.data};
        this.props.dispatch(reloadPageDataAction(response.data))
    });

    foo = (...args) => () => axios.post('', {'method': 'foo', args: args});

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
