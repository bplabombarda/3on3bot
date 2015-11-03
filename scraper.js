var fs = require('fs');
var cheerio = require('cheerio');
var request = require('request');
var express = require('express');
var app = express();

var url = 'http://www.sportsnet.ca/hockey/nhl/scores/';

request(url, function(error, response, html) {
    if(!error) {

        var $ = cheerio.load(html);
        var timeLeft = $('.game-card-container').find('.game-current-time');

        console.log(timeLeft);

        // for(var i = 0; i < timeLeft.length; i++) {
        //     console.log(timeLeft[i].children);
        // }
    }
});
