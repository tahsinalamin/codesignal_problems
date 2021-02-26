"""
In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is declared the winner unless their opponent had already won 5 games, in which case the set continues until one of the players has won 7 games.

Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final score of score1 : score2.

Example

For score1 = 3 and score2 = 6, the output should be
tennisSet(score1, score2) = true.
"""

def tennisSet(score1, score2):
    maxscore=max(score1,score2)
    minscore=min(score1,score2)
    
    if maxscore == 6:
        if minscore<5:
            return True
    if maxscore == 7:
        if minscore ==5 or minscore ==6:
            return True
    return False

