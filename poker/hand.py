from collections import Counter

from poker.card import Card
from poker.card import CardValue
from poker.utils import OrderedEnum


class HandRank(OrderedEnum):
    high_card = 0
    one_pair = 1
    two_pairs = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8
    royal_flush = 9


class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, reverse=True)
        self._rank()

    def __eq__(self, other):
        if self.rank != other.rank:
            return False
        else:
            # all cards not in rank have the same values
            return all(
                (
                    a.value == b.value
                    for a, b
                    in zip(self.cards_not_in_rank, other.cards_not_in_rank)
                )
            )

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return False

        # ranks are the same
        for a, b in zip(self.cards_in_rank, other.cards_in_rank):
            if a.value == b.value:
                continue
            else:
                return a.value > b.value
        for a, b in zip(self.cards_not_in_rank, other.cards_not_in_rank):
            if a.value == b.value:
                continue
            else:
                return a.value > b.value

        # all card values are equal
        return False

    @classmethod
    def from_string(cls, string_repr):
        return cls((Card.from_string(s) for s in string_repr.split()))

    def _rank(self):
        # if it's not a flush, we can skip some tests
        is_flush = True
        flush_suit = self.cards[0].suit
        for card in self.cards[1:]:
            if card.suit != flush_suit:
                is_flush = False
                break

        # if it's not a straight, we can skip some tests
        is_straight = True
        values = [each.value for each in self.cards]
        for i in range(1, 5):
            if values[i].value + 1 != values[i-1].value:
                is_straight = False
                break

        # get a count of each card's value
        value_counter = Counter((each.value for each in self.cards))
        most_common = value_counter.most_common(1)[0]
        second_most_common = value_counter.most_common(2)[1]

        # royal flush
        if is_flush and is_straight and self.cards[0].value == CardValue.ace:
            self.rank = HandRank.royal_flush
            self.cards_in_rank = self.cards[:]
            self.cards_not_in_rank = []

        # straight flush
        elif is_flush and is_straight:
            self.rank = HandRank.straight_flush
            self.cards_in_rank = self.cards[:]
            self.cards_not_in_rank = []

        # four of a kind
        elif most_common[1] == 4:
            self.rank = HandRank.four_of_a_kind
            self.cards_in_rank = [
                card for card in self.cards
                if card.value == most_common[0].value
            ]
            self.cards_not_in_rank = [
                card for card in self.cards
                if card.value != most_common[0].value
            ]

        # full house
        elif most_common[1] == 3 and second_most_common[1] == 2:
            self.rank = HandRank.full_house
            self.cards_in_rank = [
                card for card in self.cards
                if card.value == most_common[0].value
                or card.value == second_most_common[0].value
            ]
            self.cards_not_in_rank = [
                card for card in self.cards
                if card.value != most_common[0].value
                and card.value != second_most_common[0].value
            ]

        # flush
        elif is_flush:
            self.rank = HandRank.flush
            self.cards_in_rank = self.cards[:]
            self.cards_not_in_rank = []

        # straight
        elif is_straight:
            self.rank = HandRank.straight
            self.cards_in_rank = self.cards[:]
            self.cards_not_in_rank = []

        # three of a kind
        elif most_common[1] == 3 and second_most_common[1] != 2:
            self.rank = HandRank.three_of_a_kind
            self.cards_in_rank = [
                card for card in self.cards
                if card.value == most_common[0].value
            ]
            self.cards_not_in_rank = [
                card for card in self.cards
                if card.value != most_common[0].value
            ]

        # two pairs
        elif second_most_common[1] == 2:
            self.rank = HandRank.two_pairs
            self.cards_in_rank = [
                card for card in self.cards
                if card.value == most_common[0].value
                or card.value == second_most_common[0].value
            ]
            self.cards_not_in_rank = [
                card for card in self.cards
                if card.value != most_common[0].value
                and card.value != second_most_common[0].value
            ]

        # one pair
        elif most_common[1] == 2 and second_most_common[1] == 1:
            self.rank = HandRank.one_pair
            self.cards_in_rank = [
                card for card in self.cards
                if card.value == most_common[0].value
            ]
            self.cards_not_in_rank = [
                card for card in self.cards
                if card.value != most_common[0].value
            ]

        # high card
        else:
            self.rank = HandRank.high_card
            self.cards_in_rank = []
            self.cards_not_in_rank = self.cards[:]

