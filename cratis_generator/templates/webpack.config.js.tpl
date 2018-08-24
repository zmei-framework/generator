const path = require('path');

module.exports = {
  entry: {{ entries|tojson(2)|safe }},

  mode: "development",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        options: { presets: ['env', 'react'] }
      }
    ]
  },
  resolve: { extensions: ['*', '.js', '.jsx'] },
  output: {
    path: path.resolve(__dirname, '../app/static/react'),
    filename: '[name].bundle.js',
    library: 'R',
    libraryTarget: 'var'
  }
};