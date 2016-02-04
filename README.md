# codewords-game
A local multiplayer hidden word game made with Python, Bottle, and Knockout.js

By default, running codewords.py will start a local server on port 4000.  You can change the settings in `config/settings.py`.

Once a game has been created, the clue-givers navigate their browsers to 
`http://host:4000/game/\<game-id\>/b`
or 
`http://host:4000/game/\<game-id\>/w`
for their respective teams (b for black, w for white).
