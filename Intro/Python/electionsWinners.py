def electionsWinners(votes, k):
    winners = 0
    maximum = max(votes)
    
    for candidate_vote in votes:
        if candidate_vote+ k > maximum:
            winners +=1
        
    if votes.count(maximum) >1 and winners ==0:
        return 0
    if winners == 0:
        return 1
        
        
    
    return winners
        

