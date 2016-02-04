
/* 
        words_to_send = [{'word': game.words[index], 'team': str(game.teams[index].name), 'revealed': game.revealed[index]} for index in range(len(game.words))]
        result = {'gamestatus': game.status.name, 'gameid':str(gameid), 'words': words_to_send}
*/

function clueGiverWordsViewModel() {
    var self = this;
    
    self.gameURI = "/api/game/";
    self.myTeam = $("#team").text();
    self.gameId = $("#gameId").text();


    //self.message = ko.observable("Welcome to the code words game");
    self.mywords = ko.observableArray([]);
    self.opponentwords = ko.observableArray([]);
    self.neutralwords = ko.observableArray([]);
    self.killerword = ko.observable();
    self.myfullteam = ko.observable("white");
    self.otherteam = ko.observable("black");
    //self.hiddenblack = ko.observable();
    //self.hiddenwhite = ko.observable();

    if (self.myTeam == 'b' || self.myTeam == 'B') {
        self.myfullteam("black");
        self.otherteam("white");   
    } 


    self.teamcolor = ko.observable(self.myfullteam());

    self.getFromAPI = function(uri, gameId) {
        var query = gameId + "/" + self.myTeam;
        return $.getJSON(uri + query);
    }

    self.getFromAPI(self.gameURI, self.gameId).done(function(data) {
        var allWords = data.words;
        
        var myWords = [];
        var opponentWords = [];
        var neutralWords = [];


        allWords.forEach(function(word) {
            if (word.team == "neutral") {
                neutralWords.push(word);
            }
            else if (word.team == "killer") {
                self.killerword(word.word);
            }    
            else if (word.team == self.myfullteam()) {
                myWords.push(word);
            }
            else {
                opponentWords.push(word);
            }
        });
        
        self.mywords(myWords);
        self.opponentwords(opponentWords);
        self.neutralwords(neutralWords);
    });
    
}


ko.applyBindings(clueGiverWordsViewModel());
