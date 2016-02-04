function playerWordsViewModel() {
    var self = this;
    
    self.gameURI = "/api/game/";
    self.guessPath = "/guess/";

    // get gameId from template
    self.gameId = $("#gameId").text();
    
    self.turnText = function (status) {
        var text = " team's turn";
        if (status == "black" || status == "white"){
            text = status + text;
        }
        else {
            if (status == "finished_black_win") text = "BLACK TEAM WINS!";
            if (status == "finished_white_win") text = "WHITE TEAM WINS!";
        }        
        return text;
    }

    self.message = ko.observable("Welcome to the code words game");
    self.words = ko.observableArray([]);
    self.gamestatus = ko.observable("Whose turn?");
    self.turn = ko.observable(self.turnText(self.gamestatus()));
    self.hiddenblack = ko.observable()
    self.hiddenwhite = ko.observable()

    self.getFromAPI = function(gameId) {
        return $.getJSON(self.gameURI + gameId);
    }
    
    self.postGuess = function(gameId, word) {
        var guessURI = self.gameURI + gameId + self.guessPath + word;
        return $.post(guessURI);
    }


    self.revealWord = function(word) {
        self.postGuess(self.gameId, word).done(function(data) {
            self.message(data.message);
            self.words(data.words);
            self.gamestatus(data.gamestatus);
            self.turn(self.turnText(data.gamestatus));
            self.hiddenblack(data.hiddenblack);
            self.hiddenwhite(data.hiddenwhite);
        });
    }
    
    self.getFromAPI(self.gameId).done(function(data) {
        self.message(data.message);
        self.words(data.words); 
        self.gamestatus(data.gamestatus);
        self.turn(self.turnText(data.gamestatus));
        self.hiddenblack(data.hiddenblack);
        self.hiddenwhite(data.hiddenwhite);
    });
    
}


ko.applyBindings(playerWordsViewModel());

