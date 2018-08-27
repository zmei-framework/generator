const path = require('path');

const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: {{ entries|tojson(4)|safe }},

    mode: "development",
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader',
                options: {presets: ['env', 'react']}
            },

            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader',
                ],
            }

        ]
    },

    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].bundle.css',
        })
    ],

    resolve: {extensions: ['*', '.js', '.jsx']},
    output: {
        path: path.resolve(__dirname, '../app/static/react'),
        filename: '[name].bundle.js',
        library: 'R',
        libraryTarget: 'var'
    }
};