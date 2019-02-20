import React, { Component, createContext } from "react";

export const reloadPageDataAction = (newState) => ({
    /**
     * Apply loaded from server state
     */
    'type': 'SERVER_DATA_RELOAD',
    newState
});

export const pageDataReducer = (state, action) => {
    if (action.type === 'SERVER_DATA_RELOAD') {
        console.log('Reloading state from server: ', state);
        return {...action.newState}
    }

    return state || {};
};


const PageContext = createContext({page: null});

class PageContextProvider extends Component {
   render() {
      return (
         <PageContext.Provider value={ {page: this.props.page } }>
            {this.props.children}
         </PageContext.Provider>
      );
   }
}
const PageContextConsumer = PageContext.Consumer;

export { PageContextProvider, PageContextConsumer };
