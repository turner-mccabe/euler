class Card:
    def __init__(self, card):
        ranks = {}
        for i in range(2, 10):
            ranks[str(i)] = i
        ranks['T'] = 10
        ranks['J'] = 11
        ranks['Q'] = 12
        ranks['K'] = 13
        ranks['A'] = 14
        self.rank = ranks[card[0]]
        self.suit = card[1]

    def __gt__(self, other):
        return self.rank > other.rank

    def __str__(self):
        return f'Rank: {self.rank} Suit: {self.suit}'

class Hand:
    def __init__(self, cards_str):
        self.cards = sorted([Card(c) for c in cards_str.split(' ')])
        self.ranks = [card.rank for card in self.cards][::-1]
        self.score = self._score()

    def _score(self):
        flush_score = self._flush_score()
        straight_score = self._straight_score()
        if flush_score != 0 and straight_score != 0:
            return [9] + straight_score

        quads_score = self._quads_score()
        if quads_score != 0:
            return [8] + quads_score

        full_house_score = self._full_house_score()
        if full_house_score != 0:
            return [7] + full_house_score

        if flush_score != 0:
            return [6] + flush_score

        if straight_score != 0:
            return [5] + straight_score

        three_kind_score = self._three_kind_score()
        if three_kind_score != 0:
            return [4] + three_kind_score

        two_pair_score = self._two_pair_score()
        if two_pair_score != 0:
            return [3] + two_pair_score

        one_pair_score = self._one_pair_score()
        if one_pair_score != 0:
            return [2] + one_pair_score

        high_card_score = self.high_card_score()
        return [1] + high_card_score

    def _straight_score(self):
        for i in range(len(self.cards) - 1):
            if self.cards[i].rank != self.cards[i+1].rank - 1:
                return 0
        return self.ranks

    def _flush_score(self):
        for i in range(len(self.cards) - 1):
            if self.cards[i].suit != self.cards[i+1].suit:
                return 0
        return self.ranks

    def _quads_score(self):
        quads = False
        for rank in self.ranks:
            count = self.ranks.count(rank)
            if count == 4:
                quads = True
                break
        if not quads:
            return 0
        else:
            return [rank] + [r for r in self.ranks if r != rank]

    def _full_house_score(self):
        counts = {self.ranks.count(rank) for rank in self.ranks}
        if counts != {3, 2}:
            return 0
        else:
            trip = list({rank for rank in self.ranks if self.ranks.count(rank) == 3})[0]
            pair = list({rank for rank in self.ranks if self.ranks.count(rank) == 2})[0]
            return [trip, pair]

    def _three_kind_score(self):
        counts = {self.ranks.count(rank) for rank in self.ranks}
        if counts != {3, 1}:
            return 0
        else:
            trip = list({rank for rank in self.ranks if self.ranks.count(rank) == 3})[0]
            return [trip] + [rank for rank in self.ranks if rank != trip]

    def _two_pair_score(self):
        counts = sorted([self.ranks.count(rank) for rank in self.ranks])
        if counts != [1, 2, 2, 2, 2]:
            return 0
        else:
            pairs = sorted({rank for rank in self.ranks if self.ranks.count(rank) == 2})[::-1]
            return pairs + [rank for rank in self.ranks if self.ranks.count(rank) == 1]

    def _one_pair_score(self):
        counts = {self.ranks.count(rank) for rank in self.ranks}
        if counts != {2, 1}:
            return 0
        else:
            pair = [rank for rank in self.ranks if self.ranks.count(rank) == 2]
            return pair + [rank for rank in self.ranks if self.ranks.count(rank) == 1]

    def high_card_score(self):
        return self.ranks

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        hand = f'Hand:\n'
        for card in self.cards:
            hand += f'\t{card}\n'
        return hand


def tally_player1_wins():
    hands = []
    with open('problem_54.txt') as infile:
        for line in infile:
            hands.append([line[:len(line)//2].strip(), line[len(line)//2:].strip()])
    tally = 0
    for hand in hands:
        p1_hand = Hand(hand[0])
        p2_hand = Hand(hand[1])
        if p1_hand > p2_hand:
            tally += 1
    return tally
print(tally_player1_wins())