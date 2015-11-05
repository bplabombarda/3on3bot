requirejs.config({
    baseUrl: "/static",
    paths: {
        jquery: "vendors/jquery/dist/jquery",
        jsx: "vendors/jsx-requirejs-plugins/js/jsx",
        JSXTransformer: "vendors/jsx-requirejs-plugins/js/JSXTransformer",
        react: "vendors/react/react-with-addons",
        text: "vendors/requirejs-text/text"
    },
    jsx: {
        fileExtension: ".jsx"
    }
})
