var $ = require('cheerio');
var request = require('request');
var config = require('../../config');

var url = process.env.SCRAPE_URL;
var currentHour = new Date();


request(url, function (error, response, body) {
    // Use Cheerio to grab all game cards elements from the response body
    var gameCards = $('.game-card-container', body);
    var gameStart = $('.game-time-start', gameCards[0]);

    console.log(gameStart);

});
