/* sources of learning webpack :
 *
 * http://christianalfoni.github.io/react-webpack-cookbook/Running-a-workflow.html
 * https://github.com/petehunt/webpack-howto
 *
 */

var webpack = require('webpack');

var definePlugin = new webpack.DefinePlugin({
    __DEV__: JSON.stringify(JSON.parse(process.env.BUILD_DEV || 'true')),
    __PRERELEASE__: JSON.stringify(JSON.parse(process.env.BUILD_PRERELEASE || 'false'))
});

module.exports = {
    // entry point
    entry: ['webpack/hot/dev-server', './app/js/main.js'],
    output: {
        // outfile
        path: './build',
        publicPath: '/assets/', // used to generate urls
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            // to load jsx + ES6
            { test: /\.js$/, loader: 'babel-loader' }
        ]
    },
    resolve: {
        // to require('file') without extention (instead of require('file.js'))
        extensions: ['', '.js', '.json']
    },
    plugins: [definePlugin]
};
