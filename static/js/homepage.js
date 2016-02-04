var startNewGame = function() {
    APIcreateURI = "/api/game";
    GamePlayURIbase = "/game/";
    $.post(APIcreateURI).done(function(data) {
        location.href = GamePlayURIbase + data.gameid;
    });
}