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
    "axios": "^0.18.0",
    "babel-cli": "^6.26.0",
    "babel-core": "^6.26.3",
    "babel-loader": "^7.1.4",
    "babel-polyfill": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "babel-preset-react": "^6.24.1",
    "css-loader": "^0.28.11",
    "file-loader": "^2.0.0",
    "mini-css-extract-plugin": "^0.4.2",
    "node-sass": "^4.9.3",
    "react": "^16.4.2",
    "react-dom": "^16.4.2",
    "react-redux": "^5.0.7",
    "redux": "^4.0.0",
    "sass-loader": "^7.1.0",
    "style-loader": "^0.21.0",
    "django-channels": "^1.1.6",
    "webpack": "^4.12.0",
    "webpack-cli": "^3.0.8"{% if packages|length > 0 %},{% endif %}
    {% for package, version in packages.items() -%}
    "{{ package }}": "{{ version }}"{% if not loop.last %},{% endif %}
    {% endfor %}
  }
}
