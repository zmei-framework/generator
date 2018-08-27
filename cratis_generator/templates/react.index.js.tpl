{{ imports }}

export { {% for page in pages %}{{ page }}{{ "," if not loop.last }}{% endfor %} };

import './index.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import ReactDOMServer from 'react-dom/server';

import {createStore} from 'redux'
import {Provider} from 'react-redux'

const rootReducer = (state, action) => {
    console.log(state, action);
    return state
};

const renderElement = (component, state) => {

    const store = createStore(rootReducer, state);

    store.dispatch({type: 'INIT'});

    return <Provider store={store}>
        {React.createElement(component)}
    </Provider>
};

export const renderClient = (component, state, targetElement) => {
    return ReactDOM.hydrate(renderElement(component, state), targetElement);
};

export const renderServer = (component, state) => {
    return ReactDOMServer.renderToString(renderElement(component, state), null);
};