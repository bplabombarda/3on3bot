var koa = require('koa');
var route = require('koa-route');
var mongoose = require('koa-mongoose');
var User = require('./models/user');

var app = koa();

// Functions
function* index() {
  this.body = "<h1>Frigg off, Barb!</h1>";
}

function* about() {
  this.body = "<h2>Those are my burgers!</h2>";
}

// Routes
app.use(route.get('/', index));
app.use(route.get('/about', about));

app.listen(8008);
console.log('Koa listening on port 8008');
