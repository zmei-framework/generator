{{ imports }}
import {connect} from "react-redux";
import {withRouter} from "react-router-dom";


class {{ name }} extends {{ parent }} {
    renderContent() {
        return (
            super.renderContent() || <>Empty react component. Edit {{ name }}.jsx</>
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

{{ name }} = withRouter({{ name }});

export default {{ name }};
