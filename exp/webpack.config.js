//# generated: a62b74dcf5169f723380448fc5aed8ae

const path = require('path');

module.exports = {
    entry: {
        "blog": [
            "babel-polyfill",
            "./src/Blog/index.js"
        ],
        "blog_server": [
            "babel-polyfill",
            "./src/Blog/index_server.js"
        ]
    },

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
                test: /\.scss$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].css'
                        }
                    },

                    {
                        loader: 'sass-loader', options: {
                            includePaths: ['./node_modules', './node_modules/grommet/node_modules']
                        }
                    }
                ]
            }
        ]
    },
    resolve: {extensions: ['*', '.js', '.jsx']},
    output: {
        path: path.resolve(__dirname, '../app/static/react'),
        filename: '[name].bundle.js',
        library: 'R',
        libraryTarget: 'var'
    }
};