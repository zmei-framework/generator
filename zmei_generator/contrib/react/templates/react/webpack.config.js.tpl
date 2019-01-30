const path = require('path');

const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: {"all": ["./src/index.jsx"]},

    mode: "development",
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader',
                options: {
                    presets: [
                        '@babel/preset-env', '@babel/preset-react'
                    ],
                    plugins: [
                        '@babel/plugin-proposal-class-properties',
                        "dynamic-import-webpack"
                    ]
                },

            },

            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader',
                ],
            },
            {
                test: /\.(svg|jpg|gif|png|jpeg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]',
                    outputPath: 'images/',
                    publicPath: '/static/react/images/'
                }
            },

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
        libraryTarget: 'var',

        publicPath: '/static/react/'
    }
};