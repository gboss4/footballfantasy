__author__ = 'geoffreyboss'

import nflgame

games = nflgame.games(year= [2013,2012,2011])#week=[1,2,3,4,5,6,7,8])
players = nflgame.combine_game_stats(games)
inp = raw_input('Please enter a statistic category(i.e. rushing, passing): ')

def searchQuestions():

def passing():
    while inp == 'passing':
        for p in players.passing().sort('passing_yds').limit(15):
            msg = '%s %d attempts for %d yards and %d TDs'
            print msg % (p, p.passing_att, p.passing_yds, p.passing_tds)
        break


def rushing():
    while inp == 'rushing':
        for p in players.rushing().sort('rushing_yds').limit(15):
            msg = '%s %d carries for %d yards and %d TDs'
            print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)
        break

def try_again():
    print 'We are sorry please be more specific! (i.e. rushing, passing)'


if __name__ == '__main__':
    if inp == 'passing':
        passing()
    elif inp == 'rushing':
        rushing()
    else:
        try_again()

