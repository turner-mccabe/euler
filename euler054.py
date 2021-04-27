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
# takes ranks array which is a list of integers translated from card values
def checkStraight(ranks):
    ranks.sort(reverse=True)
    for i in range(5):
        # the second condition accounts for the ace-low straight
        if (ranks[i] + i != ranks[0] and ranks[i] + i + 8 != ranks[0]):
            return None
    return "Straight"


# define main function
def evaluateHand(cards):
    # translate card ranks
    ranks = []
    for i in range(5):
        ranks.append(rank(cards[i]))
    ranks.sort(reverse=True)
    print(ranks)

    # check straight flush
    if checkFlush(cards) == "Flush":
        if checkStraight(ranks) == "Straight": 
            return "StraightFlush", ranks[0]


    # check four of a kind
    

    # check full house 

    # check flush
    if checkFlush(cards) == "Flush":
        return "Flush", ranks
    
    # check straight
    if checkStraight(ranks) == "Straight": 
        return "Straight", ranks[0]

    # check three of a kind 

    # check pair

        # check two pair

    # check high card
    return "high card", ranks


cards = ['AS', '2S', '3S', '4S', '5S']

print(checkFlush(cards))
print(evaluateHand(cards))

# reads the text file with the poker hands
# puts cards into a list for each hand for each player
f = open("poker54.txt", "r")
for lines in range(0, case):
    hands = f.readline()
    hand1 = hands[0:14].split()
    hand2 = hands[15:29].split()

    print("hand1", hand1)
    print("hand2", hand2)
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
