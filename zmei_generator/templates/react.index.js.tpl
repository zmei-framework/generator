{{ imports }}

export { {% for page in pages %}{{ page }}{{ "," if not loop.last }}{% endfor %} };
export { {% for page in pages %}{{ page }}Reducer{{ "," if not loop.last }}{% endfor %} };

import './index.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import ReactDOMServer from 'react-dom/server';

import {createStore} from 'redux'
import {Provider} from 'react-redux'
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const renderElement = (rootReducer, component, state) => {

    const store = createStore(rootReducer, state);

    store.dispatch({type: 'INIT'});

    return <Provider store={store}>
        {React.createElement(component)}
    </Provider>
};

export const renderClient = (rootReducer, component, state, targetElement, hydrate) => {
    const render = hydrate ? ReactDOM.hydrate : ReactDOM.render;
    return render(renderElement(rootReducer, component, state), targetElement);
};

export const renderServer = (rootReducer, component, state) => {
    return ReactDOMServer.renderToString(renderElement(rootReducer, component, state), null);
};