{
  "name": "zmei-react-app-1",
  "version": "1.0.0",
  "description": "New zmei app",
  "keywords": [],
  "scripts": {
    "build": "webpack"
  },
  "author": "John Doe",
  "license": "ISC",
  "dependencies": {
    "@babel/cli": "^7.0.0",
    "@babel/core": "^7.0.0",
    "@babel/plugin-proposal-class-properties": "^7.0.0",
    "@babel/polyfill": "^7.0.0",
    "@babel/preset-env": "^7.0.0",
    "@babel/preset-react": "^7.0.0",
    "axios": "^0.18.0",
    "babel-loader": "^8.0.0",
    "babel-plugin-dynamic-import-webpack": "^1.1.0",
    "css-loader": "^0.28.11",
    "django-channels": "^1.1.6",
    "file-loader": "^2.0.0",
    "mini-css-extract-plugin": "^0.4.2",
    "node-sass": "^4.9.3",
    "react": "^16.6.3",
    "react-dom": "^16.6.3",
    "react-redux": "^5.0.7",
    "react-router-dom": "^4.3.1",
    "redux": "^4.0.0",
    "sass-loader": "^7.1.0",
    "style-loader": "^0.21.0",
    "reconnectingwebsocket": "^1.0.0",
    "webpack": "^4.12.0",
    "webpack-cli": "^3.0.8"{% if packages|length > 0 %},{% endif %}
    {% for package, version in packages.items() -%}
    "{{ package }}": "{{ version }}"{% if not loop.last %},{% endif %}
    {% endfor %}
  }
}
