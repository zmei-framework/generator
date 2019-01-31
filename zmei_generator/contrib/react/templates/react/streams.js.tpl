
import {omit, keys, difference} from "lodash";

import ReconnectingWebSocket from 'reconnectingwebsocket';
import {reloadPageDataAction} from "./state";


export const streamEnterAction = (uri) => ({
    /**
     * Apply loaded from server state
     */
    'type': 'STREAM_ENTER',
    uri
});
export const streamLeaveAction = (uri) => ({
    /**
     * Apply loaded from server state
     */
    'type': 'STREAM_LEAVE',
    uri
});

export const streamHandlerReducer = (state, action) => {
    if (action.type === 'STREAM_ENTER') {
        return {...state, ...{[action.uri]: (state[action.uri] || 0) + 1}}
    }
    if (action.type === 'STREAM_LEAVE') {
        let newCount = (state[action.uri] || 0) - 1;
        if (newCount < 1) {
            return omit(state, action.uri);
        }
        return {...state, ...{[action.uri]: newCount}}
    }

    return state || {};
};


class StreamHandler {

    constructor(store) {
        this.store = store;
        this.streams = {};
        this.currentValue = null;
    }

    setState = (response) => {
        if (response.data.__error__) throw response.data.__error__;
        if (response.data.__state__) {
            this.store.dispatch(reloadPageDataAction(response.data.__state__));
            return response.data.__state__;
        }
        return response.data;
    };

    onStoreUpdate = () => {
        let previousValue = this.currentValue;
        this.currentValue = this.store.getState().streams;

        if (previousValue !== this.currentValue) {

            difference(keys(this.currentValue), keys(this.streams)).map((uri) => {
                console.debug('Connecting to ', uri);

                const socket = new ReconnectingWebSocket(uri);
                socket.onmessage = (e) => this.setState({data: JSON.parse(e.data)});

                this.streams = {...this.streams, ...{[uri]: socket}};
            });
            difference(keys(this.streams), keys(this.currentValue)).map((uri) => {
                console.debug('Disconnecting from ', uri);

                this.streams[uri].close();

                this.streams = omit(this.streams, uri);
            });

        }
    }
}

export default StreamHandler;
