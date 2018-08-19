{{ imports }}

import React from 'react';
import ReactDOM from 'react-dom';

export {React, ReactDOM};
export { {% for page in pages %}{{ page }}{{ "," if not loop.last }}{% endfor %} };