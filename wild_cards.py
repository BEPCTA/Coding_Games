# -*- coding: utf-8 -*-

import itertools
#import poker_utils as pu

#allranks = 'A23456789TJQK'
#redcards = [ r+s for r in allranks for s in 'DH']
#blackcards = [ r+s for r in allranks for s in 'SC']
#hand_rank = pu.hand_rank
#card_ranks = pu.card_ranks
#flush = pu.flush
#straight = pu.straight
#kind = pu.kind
#two_pair= pu.two_pair

def group(items):
    '''
    Returns a list of [(count, x),..], 
    highest count firt, then highest x first.                        
    '''
    group = [(items.count(x), x) for x in set(items)]
    return sorted(group, reverse = True)

def hand_rank(hand):
    "Return a value indicating how high the hand ranks"
    # counts is the count of each rank, 
    # ranks lists corresponding ranks
    # e.g. '7 T 7 9 7' => counts = (3,1,1), ranks = (7,10,9)
    groups = group(['--23456789TJQKA'.index(r) for r,s, in hand])
    counts, ranks = zip(*groups)
    if ranks == (14,5,4,3,2): 
        ranks = ( 5,4,3,2,1)
    straight = len(ranks) ==5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else
            8 if straight and flush else
            7 if (4,1) == counts else
            6 if (3,2) == counts else
            5 if flush else
            4 if straight else
            3 if (3,1,1) == counts else
            2 if (2,2,1) == counts else
            1 if (2,1,1,1) == counts else
            0 ) , ranks
              
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h) 
               for h in itertools.product(*map(replacements, hand)))
    print(hands)
    return max(hands, key = hand_rank)

def replacements(card):
    """
    Returns a list of possible replacements for a card.
    """
    if card == "?B":
        return list( set(blackcards) - set(hand))
    elif card == "?R":
        return list(set(redcards) - set(hand))
    else:
        return [card]
       
def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    return max(itertools.combinations(hand,5), key = hand_rank)

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'
def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    
    assert (sorted(best_wild_hand("7C TC TD ?R ?B 5C 5H".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

print(test_best_hand())
#print(test_best_wild_hand())
