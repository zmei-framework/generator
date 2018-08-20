{
  "name": "genius-react-app",
  "version": "1.0.0",
  "description": "New genius app",
  "keywords": [],
  "scripts": {
    "build": "webpack"
  },
  "author": "Genius",
  "license": "ISC",
  "dependencies": {
    "react": "^16.4.2",
    "react-dom": "^16.4.2",
    "babel-cli": "^6.26.0",
    "babel-core": "^6.26.3",
    "babel-loader": "^7.1.4",
    "babel-polyfill": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "babel-preset-react": "^6.24.1",
    "css-loader": "^0.28.11",
    "style-loader": "^0.21.0",
    "webpack": "^4.12.0",
    "webpack-cli": "^3.0.8"{% if packages|length > 0 %},{% endif %}
    {% for package, version in packages.items() -%}
    "{{ package }}": "{{ version }}"{% if not loop.last %},{% endif %}
    {% endfor %}
  }
}
