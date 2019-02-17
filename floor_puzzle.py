# -*- coding: utf-8 -*-

#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# 1   Hopper does not live on the top floor. 
# 2   Kay does not live on the bottom floor. 
# 3   Liskov does not live on either the top or the bottom floor. 
# 4   Perlis lives on a higher floor than does Kay. 
# 5   Ritchie does not live on a floor adjacent to Liskov's. 
# 6   Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    floors = bottom,_,_,_,top =  [1,2,3,4,5]
    orders = list(itertools.permutations(floors))
    for (H, K, L, P, R) in orders:
        if (H is not top                #1
            and K is not bottom         #2
            and L is not top            #3
            and L is not bottom         #3
            and P > K                   #4
            and abs( L - R )  > 1       #5
            and abs( L - K )  > 1):     #6
            return [H, K, L, P, R]
print(floor_puzzle())




