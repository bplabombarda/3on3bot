var $ = require('cheerio');
var request = require('request');
var Twitter = require('twitter');


// --- MOVE TO CONFIG --------------------------------------------------
// process.env.TWITTER_CONSUMER_KEY = 'm0VhXEbzZzmJgwIKvzIbuYpt4';
// process.env.TWITTER_CONSUMER_SECRET = 'sgzZaG3UXb8NgWHhBzA3Vs4u3DN3HbhBHlNuCgNgyC16ZkVZqw';
// process.env.TWITTER_ACCESS_TOKEN_KEY = '4026302193-84IorOoSRTUy7zzqAt9hQt1RgtMMnGfuC5QPUpc';
// process.env.TWITTER_ACCESS_TOKEN_SECRET = 'mTR80znoNcQqmlFFyBEKHYf23lB2MravbSipsvnEtoMlV';

var url = 'http://www.sportsnet.ca/hockey/nhl/scores/';
// --- END MOVE TO CONFIG ----------------------------------------------

var games = [];

request(url, function (error, response, body) {
    // Use Cheerio to grab all game cards elements from the response body
    var gameCards = $('.game-card-container', body);

    for (var i = 0; i < gameCards.length; i++) {
        var gameCard = gameCards[i];
        parseGameCard(gameCard);
    }

});


function parseGameCard(gameCard) {
    var gameId = gameCard.attribs.id;
    var gameStart = $('.game-time-start', gameCard);
    //var gameProg = $('.game-time-start', gameCard);
    var gameFinal = $('.final', gameCard);

    var awayTeamInfo = $('.team-container-1', gameCard);
    var awayTeamLogo = $('.scores-team-logo img', awayTeamInfo).attr('src');
    var awayTeamCity = $('.scores-team-city', awayTeamInfo).text();
    var awayTeamName = $('.scores-team-name', awayTeamInfo).text();
    var awayTeamScore = $('.scores-team-score', awayTeamInfo).text().trim();


    var homeTeamInfo = $('.team-container-2', gameCard);
    var homeTeamLogo = $('.scores-team-logo img', homeTeamInfo).attr('src');
    var homeTeamCity = $('.scores-team-city', homeTeamInfo).text();
    var homeTeamName = $('.scores-team-name', homeTeamInfo).text();
    var homeTeamScore = $('.scores-team-score', homeTeamInfo).text().trim();

    console.log(awayTeamLogo);
    console.log(awayTeamCity);
    console.log(awayTeamName);
    console.log(awayTeamScore);
    console.log(homeTeamLogo);
    console.log(homeTeamCity);
    console.log(homeTeamName);
    console.log(homeTeamScore);

}
