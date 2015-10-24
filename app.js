var Twitter = require('twitter');
var config = require('./config.js');

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
    status: awayTeam + ' @ ' + homeTeam + ' #3on3'
};

client.post('statuses/update', params, function(error, tweet, response){
    if (!error) {
        console.log(tweet);
    }
});
