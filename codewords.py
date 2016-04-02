from bottle import route, run, static_file, template
import random
import string

# import our data persistence
from database import Db

# get settings
from config import settings

from game import Game


# short ID generator
# NOTE: This method of randomization is NOT cryptographically secure.  That's not a problem in this case.
def id_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# games running
games = {}


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')


@route('/')
def serveHomepage():
    return template('homepage')


@route('/game', method='GET')
def makeGameMessage():
    return "Please create a new game"


@route('/game/<gameid>', method='GET')
def serveGame(gameid='TEST'):
    return template('game', gameid=gameid)


@route('/game/<gameid>/<color>', method='GET')
def serveClueGiverPage(gameid='TEST', color='w'):
    if color in ['w', 'W', 'b', 'B']:
        return template('cluegiver', gameid=gameid, team=color)
    else:
        return {'message': invalid}


# ### API ROUTES ####

@route('/api/game', method='POST')
def createGame():
    # create a new game
    global games
    # get an ID for the game and make sure it isn't already being used
    while True:
        gameId = id_generator()
        if gameId not in games:
            # add the game to our dictionary of games
            games[gameId] = Game(gameId)
            break
    print("CREATING GAME " + gameId)
    print(games[gameId])
    return {'message': "Created game " + gameId + ".", 'gameid': str(gameId)}


@route('/api/game/<gameid>', method='GET')
def displayGame(gameid='TEST'):
    if gameid in games:
        game = games[gameid]
        words_to_send = [{'word': game.words[index],
                          'teamifknown': (str(game.teams[index].name) if game.revealed[index] else Game.TeamNames.unknown.name)} for index in range(len(game.words))]
        return {'message': "Code words game",
                'gamestatus': game.status.name,
                'gameid': str(gameid),
                'words': words_to_send,
                'hiddenblack': game.getHiddenCounts()["black"],
                'hiddenwhite': game.getHiddenCounts()["white"]}
    else:
        return {'message': 'invalid game-id'}


@route('/api/game/<gameid>/<color>', method='GET')
def displayGame(gameid='TEST', color='w'):
    # for the clue givers: give a list of each word and its color and whether or not it's been revealed
    if gameid in games:
        game = games[gameid]
        words_to_send = [{'word': game.words[index],
                          'team': str(game.teams[index].name),
                          'revealed': game.revealed[index]} for index in range(len(game.words))]
        result = {'gamestatus': game.status.name, 'gameid': str(gameid), 'words': words_to_send}
        return result
    else:
        return {'message': 'invalid game-id'}


@route('/api/game/<gameid>/guess/<word>', method='POST')
def makeGuess(gameid='TEST', word='pass'):
    # first make sure the word exists and is in the given game
    message = ""
    if gameid in games:
        game = games[gameid]
        if word == 'pass':
            # current team has ended their turn
            game.updateStatus(word)
        else:
            if word in game.words:
                # reveal the word
                game.updateStatus(word)
                message = word + " is " + str(game.teams[game.words.index(word)].name)
                # see who's turn it should be
            else:
                message = "word " + word + " not in game " + gameid
        words_to_send = [{
                'word': game.words[index],
                'teamifknown': (str(game.teams[index].name) if game.revealed[index] else Game.TeamNames.unknown.name)} for index in range(len(game.words))]
        return {'message': message,
                'gamestatus': game.status.name,
                'gameid': str(gameid),
                'words': words_to_send,
                'hiddenblack': game.getHiddenCounts()["black"],
                'hiddenwhite': game.getHiddenCounts()["white"]}
    else:
        message = "invalid game-id"
        return {'message': message}

# create a test game, this won't collide with real games since they don't use capital letters in their IDs
games["TEST"] = Game("TEST")

if __name__ == '__main__':
    # must put 0.0.0.0 instead of localhost to be able to serve to the local network
    run(host=settings.host, port=settings.port, debug=settings.debug, reloader=settings.reloader)
