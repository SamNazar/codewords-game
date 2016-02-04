<html>
<head>
<script type='text/javascript' src='/static/js/knockout.min.js'></script>
<script type='text/javascript' src='/static/js/jquery.min.js'></script>
<script type='text/javascript' src='/static/js/game.js' defer='defer'></script>
<link rel="stylesheet" type="text/css" href="/static/styles.css">
</head>
<body>
    <header class="header">
        <div id="whosturn" data-bind="css: gamestatus">
            <strong data-bind="text: turn">.</strong><br/>
            <input type="button" value="pass" onclick="revealWord('pass')"/>
        </div>
        <div class="message">
            <strong data-bind="text: message">hello</strong>
        </div>
        <div class="scores">
            Words Left:<br/>
            <span class="black" data-bind="text: hiddenblack"></span>
            <span class="white" data-bind="text: hiddenwhite"></span>
        </div>
    </header>
    
    <div class="words">
        <ul class="word-list" data-bind="foreach: words">
            <li data-bind="css: teamifknown, click: teamifknown == 'unknown' ? function() {revealWord(word);} : function () {return false;}">
                <span data-bind="text:word"></span>
            </li>
        </ul>
    </div>    

    <div id="gameId" style="display:none">{{gameid}}</div>

</body>
    
</html>