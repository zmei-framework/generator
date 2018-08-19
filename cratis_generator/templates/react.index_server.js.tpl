{{ imports }}

import React from 'react';
import ReactDOMServer from 'react-dom/server';

export {React, ReactDOMServer as ReactDOM};
export { {% for page in pages %}{{ page }}{{ "," if not loop.last }}{% endfor %} };