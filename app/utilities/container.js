var $ = require('cheerio');
var request = require('request');
var config = require('../../config');

var url = process.env.SCRAPE_URL;


request(url, function (error, response, body) {
    // Use Cheerio to grab all game cards elements from the response body
    var gameCards = $('.game-card-container', body);
    var gameStart = $('.game-time-start', gameCards[0]);

    var gameStartHour = Number(gameStart.text().split(':')[0]);
    var ampm = gameStart.text().split(' ')[1];

    var now = new Date();
    var curHour = now.getHours();

    if (ampm == 'PM') {
        gameStartHour += 12;
        console.log(gameStartHour);
    } else {
        // console.log(gameStartHour);
    }

    // console.log(curHour, ampm);

});

function checkSchedule(gameStartHour, curHour) {
    if(gameStartHour !== 0 && gameStartHour <= (curHour - 1)) {
        var tweeter = require('./tweeter');
    }
}
