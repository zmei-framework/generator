
import {combineReducers} from "redux";

import {streamHandlerReducer} from "./streams"
import {pageDataReducer} from "./state"

const RootReducer = combineReducers({
    streams: streamHandlerReducer,
    data: pageDataReducer
});


export default {{ name }}Reducer;