<html>
<head>
<script type='text/javascript' src='/static/js/knockout.min.js'></script>
<script type='text/javascript' src='/static/js/jquery.min.js'></script>
<script type='text/javascript' src='/static/js/homepage.js' defer='defer'></script>
<link rel="stylesheet" type="text/css" href="/static/styles.css">
</head>
<body>
    <header class="header">
        <h2>Welcome to the Code Names Game</h2>
    </header>
    <div class="content">
        <div id="startmenu">
            <input type="button" class="actionbutton" value="New Game" onclick="startNewGame()"/>
            <br/>
            or
            <br/>
            Enter a Game ID to join:<br/>
            <input type="text" id="gameToJoin"/>
            <input type="button" value="Go" class="actionbutton" id="joinGame" onclick="location.href='/game/' + $('#gameToJoin').val()"/>
        </div>
    </div>    

</body>
    
</html>