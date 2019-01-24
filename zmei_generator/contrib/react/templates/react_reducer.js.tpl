

export const reloadPageDataAction = (newState) => ({
    /**
     * Apply loaded from server state
     */
    'type': 'SERVER_DATA_RELOAD',
    newState
});

export const {{ name }}Reducer = (state, action) => {
    if (action.type === 'SERVER_DATA_RELOAD') {
        console.log('Reloading state from server: ', state);
        return {...state, ...action.newState}
    }
    return state
};