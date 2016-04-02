from enum import IntEnum
from collections import namedtuple
import random
import string

from config import settings

# load words info and close file
with open(settings.words_file) as wordsfile:
    all_words = [line.rstrip('\n').upper() for line in wordsfile]

# define a game class
class Game:

    class Statuses(IntEnum):
        black = 1
        white = 2
        finished_black_win = 3
        finished_white_win = 4

    class TeamNames(IntEnum):
        unknown = 0
        black = 1
        white = 2
        neutral = 3
        killer = 4

    def __init__(self, gameId):
        self.gameId = gameId
        # select 25 random words from the loaded word list
        self.words = self.pick25words()
        # pick which team is going first
        self.status = random.choice(list(Game.Statuses)[:2])
        # teams represents which team is associated with each word
        # to initialize teams, we add 8 of each team, plus 7 neutral words (0s) and 1 more for the teams who goes first 
        # then we shuffle the array
        self.teams = ([Game.TeamNames.black] * 8) + ([Game.TeamNames.white] * 8) + ([Game.TeamNames.neutral] * 7)
        self.teams += [Game.TeamNames.killer] + [Game.TeamNames(int(self.status))]
        random.shuffle(self.teams)
        # none of the words have yet been revealed
        self.revealed = [False] * 25

    def __str__(self):
        # return string of pretty-printed game
        result = (str(self.status.name) + '\'s turn\n')
        for i in range(len(self.words)-1):
            result += self.words[i] + " \t\t"
            if self.revealed[i]:
                result += str(self.teams[i].name) + '\n'
            else:
                result += '( ' + str(self.teams[i].name) + ' )\n'
        return result

    def pick25words(self):
        # shuffle the words array and pick the first 25 words
        global all_words
        random.shuffle(all_words)
        return all_words[0:25]

    def swapStatus(self):
        if self.status == Game.Statuses.white:
            self.status = Game.Statuses.black
        elif self.status == Game.Statuses.black:
            self.status = Game.Statuses.white

    # return hidden counts for black and white
    def getHiddenCounts(self):
        black_count = 0
        white_count = 0
        for index in range(len(self.words)):
            if not self.revealed[index]:
                if self.teams[index] == Game.TeamNames.black:
                    black_count += 1
                elif self.teams[index] == Game.TeamNames.white:
                    white_count += 1
        return {'black': black_count, 'white': white_count}
            
    def updateStatus(self, word):
        if word == 'pass':
            self.swapStatus()
        else:
            if word in self.words:
                wordindex = self.words.index(word)
                self.revealed[wordindex] = True
                # if the word just revealed was the killer, the game is over
                if self.teams[wordindex] == Game.TeamNames.killer:
                    if self.status == Game.Statuses.white:
                        self.status = Game.Statuses.finished_black_win
                    elif self.status == Game.Statuses.black:
                        self.status = Game.Statuses.finished_white_win
                # now see if anyone has won (hidden words at 0)
                elif self.getHiddenCounts()['black'] == 0:
                    self.status = Game.Statuses.finished_black_win
                elif self.getHiddenCounts()['white'] == 0:
                    self.status = Game.Statuses.finished_white_win
                else:
                    # if the team guessed their own color
                    if self.status == self.teams[wordindex]:
                        # it is still their turn
                        pass
                    else:
                        # otherwise their turn ends
                        self.swapStatus()
