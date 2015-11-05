requirejs(["jquery", "react", "jsx!main"], function($, React, Main) {
    $(function() {
        React.render(React.createElement(Main, null), document.body);
    });
});
