var koa = require('koa');
var route = require('koa-route');

var app = koa();

//and we'll set up 2 routes, for our index and about me pages
app.use(route.get('/', index));
app.use(route.get('/about', about));

//The asterisk is key, designates a function as a generator.
function *index() {
  this.body = "<h1>Frigg off, Barb!</h1>";
}

function *about() {
  this.body = "<h2>Those are my burgers!</h2>";
}

app.listen(8008);
console.log('Koa listening on port 8008');
