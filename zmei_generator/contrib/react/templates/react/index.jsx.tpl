import './index.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import ReactDOMServer from 'react-dom/server';

import {createStore} from 'redux'
import {Provider} from 'react-redux'
import axios from "axios";
import RootRouter from "./router";
import RootReducer from "./reducer";
import StreamHandler from "./streams";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";


const renderElement = (rootReducer, component, state) => {
    const store = createStore(RootReducer, {data: state});
    const handler = new StreamHandler(store);

    store.subscribe(handler.onStoreUpdate);

    store.dispatch({type: 'INIT'});

    return <Provider store={store}>
        <RootRouter/>
    </Provider>
};

export const renderClient = (rootReducer, component, state, targetElement, hydrate) => {
    const render = hydrate ? ReactDOM.hydrate : ReactDOM.render;
    return render(renderElement(rootReducer, component, state), targetElement);
};

export const renderServer = (rootReducer, component, state) => {
    return ReactDOMServer.renderToString(renderElement(rootReducer, component, state), null);
};