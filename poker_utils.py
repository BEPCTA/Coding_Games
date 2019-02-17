# -*- coding: utf-8 -*-
# ===========================================================
# !!! These probabilities are for 7-card poker hands !!!
# Rank   Hand        Frequency Probability Cumulative Odds
# ==========================================================
# 9 Royal flush          4,324    0.0032%  0.0032% 30939  : 1
# 8 Straight flush      37,260    0.0279%  0.0311%  3589.6: 1
# 7 Four of a kind     224,848    0.168%   0.199%    594  : 1
# 6 Full house       3,473,184    2.60%    2.80%   37.5   : 1
# 5 Flush            4,047,644    3.03%    5.82%   32.1   : 1
# 4 Straight         6,180,020    4.62%   10.4%    20.6   : 1
# 3 Three of a kind  6,461,620    4.83%   15.3%    19.7   : 1
# 2 Two pair        31,433,400   23.5%    38.8%     3.26  : 1
# 1 One pair        58,627,800   43.8%    82.6%     1.28  : 1
# 0 No pair         23,294,460   17.4%    100%      4.74  : 1   
#    Total         133,784,560   100% 	  100% 	    0     : 1 
#=============================================================
# echo "# Coding_Games" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/BEPCTA/Coding_Games.git
# git push -u origin master
# http://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html
# =============================================================================
hand_names= [ "Straight flush", "Four of a kind",
              "Full house", "Flush", "Straight", 
              "Three of a kind", "Two pair", 
              "One pair", "High card" ]
              
def highest_hand(hands):
    return max(hands, key=hand_rank)

def poker(hands):
    "Return a list of winning hands: poker([hand,...])=> [hand,.]"
    return allmax(hands, key=hand_rank)

def allmax( iterable, key=None):
    " Return a list of all items equal to the max of the iterable"
    result, maxval = [], None
    key = key or (lambda x:x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

def card_ranks(hand):
    '''Return a list of the ranks, sorted with higher first'''
    card_names = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    card_values= [ 2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14]
    card_dict  = dict(zip(card_names, card_values))
    ranks = [card_dict[r] for r,s in hand]
    #ranks = ['--23456789TJKA'.index(r) for r,s  in hand ]
    #ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]: ranks = [5,4,3,2,1] 
    return ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    for i in range(1, len(ranks)):
        if ranks[i] + i != ranks[0]:
            return False
    return True

def flush(hand):
    "Return True if all the cards have the same suit."
#    for i in range(len(hand)-1): 
#        if hand[-1][1] != hand[i][1]:
#            return False
#   return True
    suits =[ s for r, s in hand]
    return len(set(suits)) == 1 

def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""

    a, b = 0, 0
    for r in set(ranks):
        if ranks.count(r) == 2:
            a , b = b, r
    if a > 0: 
        if a >b : return a, b
        else: return b,a 
    return None

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert highest_hand([sf] + 99*[fh]) == sf

    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)   

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [ 9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10,10,10, 7, 7]

    return 'tests pass'

#print(test())
    