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
    return "6-Flush"

# returns "Straight" if all cards are consecutive values
# takes sorted ranks array which is a list of integers translated from card values
def checkStraight(ranks):
    for i in range(5):
        # the second condition accounts for the ace-low straight
        if (ranks[i] + i != ranks[0] and ranks[i] + i + 8 != ranks[0]):
            return None
    return "5-Straight"

# checks for Quads, Trips or Full House
# takes sorted ranks array of length = 5
# returns three-part array [str(hand rank), quadsOrTrips, leftover cards]
def checkQuads(ranks):
    for i in range(2):
        if ranks[i] == ranks[i+3]:
            quads = ranks[i]
            hicard = ranks[i-1]
            return ["8-Quads", quads, hicard]
    for i in range(3):
        if ranks[i] == ranks[i+2]:
            trips = ranks[i]
            remainder = [ranks[i-1], ranks[i-2]]
            if (remainder[0] == remainder[1]):
                pair = remainder[0]
                return ["7-FullHouse", trips, pair]
            else:
                trips_score = ["4-Trips", trips]
                trips_score.extend(remainder)
                return trips_score
    return [None]
    
# this function is only valid once checkQuads() has returned None
# it checks for two pair and one pair hands
# takes sorted ranks array of length = 5
def checkPair(ranks):
    pairCount = 0
    for i in range(4):
        if ranks[i] == ranks[i+1]: # if there is a pair discovered
            pairCount = pairCount + 1
            if pairCount == 1: 
                high_pair = ranks[i]
                first_pair_location = i
                remainder = [ranks[i-1], ranks[i-2], ranks[i-3]]
            if pairCount == 2: 
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
    if pairCount == 1:
        pairScore = ["2-OnePair", high_pair]
        pairScore.extend(remainder)
        return pairScore
    if pairCount == 2:
        return ["3-TwoPair", high_pair, low_pair, remainder]
    return [None]


# define main function
# this function evaluates hands in highest to lowest order. 

# it produces a score for each hand

# the first ele
def evaluateHand(cards):
    # translate card ranks
    ranks = []
    for i in range(5):
        ranks.append(rank(cards[i]))
    ranks.sort(reverse=True)
    # print(ranks)

    # set results array
    score = []

    # check straight flush
    if checkFlush(cards) == "6-Flush":
        if checkStraight(ranks) == "5-Straight": 
            score.append("9-StraightFlush")
            score.extend(ranks)
            return score

    # check four of a kind
    quads = checkQuads(ranks)

    if quads[0] == "8-Quads":
        return quads

    # check full house 
    if quads[0] == "7-FullHouse":
        return quads 

    # check flush
    if checkFlush(cards) == "6-Flush":
        score.append("6-Flush")
        score.extend(ranks)
        return score
    
    # check straight
    if checkStraight(ranks) == "5-Straight": 
        score.append("5-Straight")
        score.extend(ranks)
        return score

    # check three of a kind 
    if quads[0] == "4-Trips":
        return quads

    # check for pair and two pair
    pair = checkPair(ranks)

    if pair[0] == "3-TwoPair":
        return pair

    if pair[0] == "2-OnePair":
        return pair

    # check high card
    score.append("1-high card")
    score.extend(ranks)
    return score


# it declares a winner when one player has a higher ranking hand type
# when players tie on hand rank, it evaluates alternate tiebreakers like high cards. 
def compareHands(hand1, hand2):
    eval1 = evaluateHand(hand1)
    eval2 = evaluateHand(hand2)
    if eval1[0] > eval2[0]:
        print("player 1 wins with", eval1[0], ", beating player 2s", eval2[0])
        return "Player 1"
    elif eval1[0] < eval2[0]:
        print("player 2 wins with", eval2[0], ", beating first players", eval1[0])
        return "Player 2"
    elif eval1[0] == eval2[0]:
        for i in range(len(eval1)):
            if eval1[i] > eval2[i]:
                print("player 1 wins with", eval1[0], "with a", eval1[i], ", beating player 2's same hand but with a", eval2[i], "in the", i, "position")
                return "Player 1"
            elif eval1[i] < eval2[i]:
                print("player 2 wins with", eval2[0], "with a", eval2[i], ", beating player 1's who had a", eval1[i], "in the", i, "position")
                return "Player 2"
    return None

hand = ['7H', '4C', '9C', '3H', '9H']
print(evaluateHand(hand))

# reads the text file with the poker hands
# puts cards into a list for each hand for each player
f = open("poker54.txt", "r")
wins = 0
for lines in range(0, case):
    hands = f.readline()
    hand1 = hands[0:14].split()
    hand2 = hands[15:29].split()
    print("")
    print("hand1", hand1)
    print("hand2", hand2)
    if compareHands(hand1, hand2) == "Player 1":
        wins = wins + 1
f.close()



print("player 1 wins", wins, "hands")
print(time.time() - t0, "seconds elapsed")

