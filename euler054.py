import sys
import time
# import pandas as pd

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=54

# for information, please visit: 
# https://projecteuler.net/about

# read in case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# gets rank of card and converts face cards to equivalent values
def rank(card):
    rank = card[0] 
    if rank == "A":
        return 14
    if rank == "K":
        return 13
    if rank == "Q":
        return 12
    if rank == "J":
        return 11   
    if rank == "T":
        return 10
    return int(rank)

# returns "Flush" if all 5 cards have the same suit
def checkFlush(cards):
    suits = []
    st = 0
    for i in range(5):
        st = cards[i][1]
        suits.append(st)
        if st != suits[0]:
            return None
    return "Flush"

# returns "Straight" if all cards are consecutive values
# takes sorted ranks array which is a list of integers translated from card values
def checkStraight(ranks):
    for i in range(5):
        # the second condition accounts for the ace-low straight
        if (ranks[i] + i != ranks[0] and ranks[i] + i + 8 != ranks[0]):
            return None
    return "Straight"

# checks for Quads, Trips or Full House
# takes sorted ranks array of length = 5
# returns three-part array [str(hand rank), quadsOrTrips, leftover cards]
def checkQuads(ranks):
    for i in range(2):
        if ranks[i] == ranks[i+3]:
            quads = ranks[i]
            hicard = ranks[i-1]
            return ["Quads", quads, hicard]
    for i in range(3):
        if ranks[i] == ranks[i+2]:
            trips = ranks[i]
            remainder = [ranks[i-1], ranks[i-2]]
            if (remainder[0] == remainder[1]):
                return ["Full House", trips, pair]
            else:
                return ["Trips", trips, remainder]
    return [None]
    
# this function is only valid once checkQuads() has returned None
# it checks for two pair and one pair hands
# takes sorted ranks array of length = 5
def checkPair(ranks):
    paircount = 0
    for i in range(4):
        if ranks[i] == ranks[i+1]: # if there is a pair discovered
            paircount = paircount + 1
            if paircount == 1: 
                high_pair = ranks[i]
                first_pair_location = i
                remainder = [ranks[i-1], ranks[i-2], ranks[i-3]]
            if paircount == 2: 
                low_pair = ranks[i]
                if i == 2: # if second pair begins on 3rd card, then remainder is on last card
                    remainder = ranks[4]
                elif first_pair_location == 0: 
                    # if first pair is at beginnning, and second pair begins on 3rd card, remainder is middle card
                    remainder = ranks[2]
                elif first_pair_location == 1:
                    # if the first pair is the second card, the remainder is the first card
                    remainder = ranks[0]
                else:
                    return "unexpected pair error"
    if paircount == 1:
        return ["One Pair", high_pair, remainder]
    if paircount == 2:
        return ["Two Pair", high_pair, low_pair, remainder]
    return [None]


# define main function
# this function evaluates hands in highest to lowest order. 
# it declares a winner when one player has a higher ranking hand type
# when players tie on hand rank, it evaluates alternate tiebreakers like high cards. 
# it would be more flexible to have this function be general to score hands and then compare scores to determine who wins. 
# however, it is faster and simpler to have the function return simply the player with the winning hand
# and that is all we need for the scope of this problem. 
def evaluateHand(cards):
    # translate card ranks
    ranks = []
    for i in range(5):
        ranks.append(rank(cards[i]))
    ranks.sort(reverse=True)
    # print(ranks)

    # check straight flush
    if checkFlush(cards) == "Flush":
        if checkStraight(ranks) == "Straight": 
            return "StraightFlush", ranks[0]

    # check four of a kind
    quads = checkQuads(ranks)

    if quads[0] == "Quads":
        return quads

    # check full house 
    if quads[0] == "Full House":
        return quads 

    # check flush
    if checkFlush(cards) == "Flush":
        return "Flush", ranks
    
    # check straight
    if checkStraight(ranks) == "Straight": 
        return "Straight", ranks[0]

    # check three of a kind 
    if quads[0] == "Trips":
        return quads

    # check for pair and two pair
    pair = checkPair(ranks)

    if pair[0] == "Two Pair":
        return pair

    if pair[0] == "One Pair":
        return pair

    # check high card
    return "high card", ranks


# cards = ['AS', 'AS', 'AS', 'AH', '5S']

# print(cards[-1])

# remainder = [cards[-1], cards[-2]]
# print(remainder)
# print(checkFlush(cards))
# print(evaluateHand(cards))

# reads the text file with the poker hands
# puts cards into a list for each hand for each player
f = open("poker54.txt", "r")
for lines in range(0, case):
    hands = f.readline()
    hand1 = hands[0:14].split()
    hand2 = hands[15:29].split()
    print("")
    print("hand1", hand1)
    print(evaluateHand(hand1))
    print("")
    print("hand2", hand2)
    print(evaluateHand(hand2))
f.close()


# find solution
# sol = evaluateHand(case)
# print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")


# using pandas:

# # read in the poker hands
# df = pd.read_csv('poker54.txt', sep = " ", header = None)
# # assign column names
# df.columns = ["1a", "1b", "1c", "1d","1e", "2a", "2b", "2c", "2d", "2e"]

# print(df.head())
