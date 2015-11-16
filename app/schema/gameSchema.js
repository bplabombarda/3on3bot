var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var gameSchema = new Schema({
    id:  Number,
    awayTeam: {
        city: String,
        name: String,
        score: Number,
        logoURL: String
    },
    homeTeam: {
        city: String,
        name: String,
        score: Number,
        logoURL: String
    },
    winningGoal: {
        time: Number,
        scorer: String,
        assist1: String,
        assist2: String,
        videoURL: String
    }
});
