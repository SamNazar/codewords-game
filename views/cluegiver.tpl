<html>
<head>
<script type='text/javascript' src='/static/js/knockout.min.js'></script>
<script type='text/javascript' src='/static/js/jquery.min.js'></script>
<script type='text/javascript' src='/static/js/cluegiver.js' defer='defer'></script>
<link rel="stylesheet" type="text/css" href="/static/styles.css">
</head>
<body>
    <header class="header">
        <h2>Your Team: <span data-bind="text: teamcolor"></span></h2>
    </header>
    <div class="content">
        <div class="wordlists">
            <div id="killerword">
                Killer Word: <span class="killer" data-bind="text:killerword"></span>
            </div>
            <div id="yourwords" data-bind="css: teamcolor">
                Your Words
                <ul class="word-list-team" data-bind="foreach: mywords">
                    <li data-bind="css: {revealedword: revealed}, text:word">
                    </li>
                </ul>                    
            </div>
            <div id="opponentswords" data-bind="css: otherteam">
                Opponent's Words
                <ul class="word-list-team" data-bind="foreach: opponentwords">
                    <li data-bind="css: {revealedword: revealed}, text:word">
                    </li>
                </ul>                    
            </div>
            <div id="neutralwords">
                Neutral Words
                <ul class="word-list-team" data-bind="foreach: neutralwords">
                    <li data-bind="css: {revealedword: revealed}, text:word">
                    </li>
                </ul>                    
            </div>
        </div>
    </div>    
    <div id="gameId" style="display:none">{{gameid}}</div>
    <div id="team" style="display:none">{{team}}</div>
</body>
    
</html>