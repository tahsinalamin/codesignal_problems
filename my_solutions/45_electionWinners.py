"""
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

Example

For votes = [2, 3, 5, 2] and k = 3, the output should be
electionsWinners(votes, k) = 2.

"""


def electionsWinners(votes, k):
    candidates=0
  
    maxV=max(votes)
    if k==0:
        for i in votes:
            if i==maxV:
                candidates+=1   
            if candidates>1:
                return 0
         
    
    for i in votes:        
        if i+k > maxV:
            candidates+=1
        
        
    return candidates

