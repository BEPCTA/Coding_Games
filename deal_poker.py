# -*- coding: utf-8 -*-

import random # this will be a useful library for shuffling
import poker_utils as pu

hand_names= [ "Straight flush", "Four of a kind",
              "Full house", "Flush", "Straight", 
              "Three of a kind", "Two pair", 
              "One pair", "High card" ]
              
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 


def deal_mine(numhands, n=5, deck=mydeck):
    
    a = [[0 for i in range(n)] for j in range(numhands)]
    for i in range(n):
        for j in range(numhands):
           a[j][i] = deck.pop(random.randint(0,len(deck)-1))
    return a

def deal(numhands, n=5, 
         deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands) ] 
    
 #print(deal(13,4))
 
def hand_percentage(n=700_000):
      """
      Sample n random hands and print a table of
      percentages for each type of hand.
      """
      count = [0] * len(hand_names)
      for i in range(n//10):
          for hand in deal(10):
              ranking = pu.hand_rank(hand)[0]
              count[ranking] += 1
      for i in range(len(hand_names)):
          print("%16s: %6.3f %%" %(hand_names[-1-i], 100*count[i]/n))

hand_percentage(1000)
              