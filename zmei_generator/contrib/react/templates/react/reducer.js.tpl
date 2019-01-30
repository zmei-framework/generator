
import {combineReducers} from "redux";

export const reloadPageDataAction = (newState) => ({
    /**
     * Apply loaded from server state
     */
    'type': 'SERVER_DATA_RELOAD',
    newState
});

const pageDataReducer = (state, action) => {
    if (action.type === 'SERVER_DATA_RELOAD') {
        console.log('Reloading state from server: ', state);
        return {...state, ...action.newState}
    }

    return state || {};
};


const RootReducer = combineReducers({
    data: pageDataReducer
});


export default {{ name }}Reducer;