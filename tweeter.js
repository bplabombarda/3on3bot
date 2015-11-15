var $ = require('cheerio');
var request = require('request');
var Twitter = require('twitter');


// --- MOVE TO CONFIG --------------------------------------------------
// process.env.TWITTER_CONSUMER_KEY = '';
// process.env.TWITTER_CONSUMER_SECRET = '';
// process.env.TWITTER_ACCESS_TOKEN_KEY = '';
// process.env.TWITTER_ACCESS_TOKEN_SECRET = '';

var url = 'http://www.sportsnet.ca/hockey/nhl/scores/';
// --- END MOVE TO CONFIG ----------------------------------------------

request(url, function (error, response, body) {

    var client = new Twitter({
        consumer_key: '',
        consumer_secret: '',
        access_token_key: '',
        access_token_secret: ''
    });

    // Use Cheerio to grab all game cards elements from the response body
    var gameCards = $('.game-card-container', body);

    for (var i = 0; i < gameCards.length; i++) {
        var gameCard = gameCards[i];
        tweet3on3(gameCard, client);
    }

});

function tweet3on3(gameCard, client) {

    // Game ID
    var gameIdAttrib = gameCard.attribs.id;
    var gameId = gameIdAttrib.split('_')[3];

    // Game Info
    // var gameStart = $('.game-time-start', gameCard);
    var gameStatus = $('.scores-game-status', gameCard);
    var gameProgress = $('.game-current-time', gameStatus).text();
    var gamePeriod = $('.game-current-period', gameStatus).text();
    // var gameFinal = $('.final', gameCard);

    // Away Team Info
    var awayTeamInfo = $('.team-container-1', gameCard);
    var awayTeamLogo = $('.scores-team-logo img', awayTeamInfo).attr('src');
    var awayTeamCity = $('.scores-team-city', awayTeamInfo).text();
    var awayTeamName = $('.scores-team-name', awayTeamInfo).text();
    // var awayTeamScore = $('.scores-team-score', awayTeamInfo).text().trim();

    // Home Team Info
    var homeTeamInfo = $('.team-container-2', gameCard);
    var homeTeamLogo = $('.scores-team-logo img', homeTeamInfo).attr('src');
    var homeTeamCity = $('.scores-team-city', homeTeamInfo).text();
    var homeTeamName = $('.scores-team-name', homeTeamInfo).text();
    // var homeTeamScore = $('.scores-team-score', homeTeamInfo).text().trim();

    if ((gamePeriod == '3RD' && gameProgress == 'END') || gamePeriod == 'OT') {
        status = awayTeamName + ' @ ' + homeTeamName + ' #3on3bot';
        console.log('Overtime!');
    }
    else {
        status = awayTeamName + ' @ ' + homeTeamName + ' #3on3NOT';
        console.log('Nooovertime! ' + status);
    }

    var params = {status: status};
    client.post('statuses/update', params, function(error, tweets, response){
        if (!error) {
            console.log(tweets);
        }
        else {
            console.log(error);
        }
    });

}
