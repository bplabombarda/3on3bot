var Twitter = require('twitter');
var config = require('./config.js');
var express = require('express');
var app = express();

// ====================================================================
// Routes
// ====================================================================
// GET method route
app.get('/', function(req, res) {
    res.send('GET request');
});

// POST method route
app.post('/', function(req, res) {
    res.send('POST request');
});

app.all('/secret', function(req, res, next) {
    console.log("Accessing the secret!");
    next(); // pass control to the next handler
});

// ====================================================================
// Twitter Hookups
// ====================================================================
var client = new Twitter({
    consumer_key: process.env.CONSUMER_KEY,
    consumer_secret: process.env.CONSUMER_SECRET,
    access_token_key: process.env.ACCESS_TOKEN_KEY,
    access_token_secret: process.env.ACCESS_TOKEN_SECRET
});

var homeTeam = 'VAN',
    awayTeam = 'CGY';

var params = {
    status: awayTeam + ' @ ' + homeTeam + ' #NHL3on3'
};

client.post('statuses/update', params, function(error, tweet, response){
    if (!error) {
        console.log(tweet);
    }
});
