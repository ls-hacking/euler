import pytest

from poker.card import Card
from poker.card import CardSuit
from poker.card import CardValue


class TestCardValue:
    @pytest.mark.parametrize(
        "string_repr, value, name",
        (
            ("2", 2, "two"),
            ("3", 3, "three"),
            ("4", 4, "four"),
            ("5", 5, "five"),
            ("6", 6, "six"),
            ("7", 7, "seven"),
            ("8", 8, "eight"),
            ("9", 9, "nine"),
            ("T", 10, "ten"),
            ("J", 11, "jack"),
            ("Q", 12, "queen"),
            ("K", 13, "king"),
            ("A", 14, "ace"),
        ),
    )
    def test_from_string(self, string_repr, value, name):
        v = CardValue.from_string(string_repr)
        assert v.value == value
        assert v.name == name

    def test_comparison(self):
        VALUES = (
            CardValue.two,
            CardValue.three,
            CardValue.four,
            CardValue.five,
            CardValue.six,
            CardValue.seven,
            CardValue.eight,
            CardValue.nine,
            CardValue.ten,
            CardValue.jack,
            CardValue.queen,
            CardValue.king,
            CardValue.ace,
        )
        for i in range(len(VALUES)):
            this_value = VALUES[i]
            for smaller_value in VALUES[:i]:
                assert smaller_value < this_value
                assert this_value > smaller_value
            for larger_value in VALUES[i+1:]:
                assert larger_value > this_value
                assert this_value < larger_value


class TestCardSuit:
    @pytest.mark.parametrize(
        "string_repr, name",
        (
            ("C", "clubs"),
            ("D", "diamonds"),
            ("H", "hearts"),
            ("S", "spades"),
        )
    )
    def test_from_string(self, string_repr, name):
        v = CardSuit.from_string(string_repr)
        assert v.name == name


class TestCard:
    @pytest.mark.parametrize(
        "string_repr, value, suit",
        (
            ("AC", CardValue.ace, CardSuit.clubs),
            ("JH", CardValue.jack, CardSuit.hearts),
            ("2D", CardValue.two, CardSuit.diamonds),
            ("9S", CardValue.nine, CardSuit.spades),
        )
    )
    def test_from_string(self, string_repr, value, suit):
        card = Card.from_string(string_repr)
        assert card.value == value
        assert card.suit == suit

    def test_comparison(self):
        card = Card.from_string("8C")
        assert card > Card.from_string("6C")
        assert card > Card.from_string("6H")
        assert card < Card.from_string("JC")
        assert card < Card.from_string("JH")
        # same card (should never happen)
        assert card == Card.from_string("8C")
        # same value, different suit.
        assert card == Card.from_string("8H")


