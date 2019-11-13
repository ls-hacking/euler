import pytest

from poker.hand import Hand
from poker.hand import HandRank


class TestHandRank:
    RANKS = (
        HandRank.high_card,
        HandRank.one_pair,
        HandRank.two_pairs,
        HandRank.three_of_a_kind,
        HandRank.straight,
        HandRank.flush,
        HandRank.full_house,
        HandRank.four_of_a_kind,
        HandRank.straight_flush,
        HandRank.royal_flush,
    )

    def test_comparisons(self):
        """Ensure all six comparison operators work as expected"""
        num_ranks = len(self.RANKS)
        for idx_outer, rank in enumerate(self.RANKS):
            for idx_inner, other_rank in enumerate(self.RANKS):
                if idx_outer < idx_inner:
                    assert rank < other_rank
                    assert rank <= other_rank
                    assert other_rank > rank
                    assert other_rank >= rank
                elif idx_outer > idx_inner:
                    assert rank > other_rank
                    assert rank >= other_rank
                    assert other_rank < rank
                    assert other_rank <= rank
                else:
                    assert rank == other_rank
                    assert rank >= other_rank
                    assert rank <= other_rank
                    assert other_rank == rank
                    assert other_rank >= rank
                    assert other_rank <= rank


class TestHand:
    def test_sorting(self):
        hand = Hand.from_string("2H 5H 4H 3H 6H")
        assert [6, 5, 4, 3, 2] == [c.value.value for c in  hand.cards]

    @pytest.mark.parametrize(
        "cards, rank",
        (
            ("2H 3C 5H 6S 7C", HandRank.high_card),
            ("2H 2C 5H 6S 7C", HandRank.one_pair),
            ("2H 2C 5H 5S 7C", HandRank.two_pairs),
            ("2H 2C 2H 5S 7C", HandRank.three_of_a_kind),
            ("2H 3C 4H 5S 6C", HandRank.straight),
            ("2H 3H 4H 5H 9H", HandRank.flush),
            ("2H 2C 2H 5S 5C", HandRank.full_house),
            ("2H 2C 2H 2S 5C", HandRank.four_of_a_kind),
            ("2H 3H 4H 5H 6H", HandRank.straight_flush),
            ("KH AH TH JH QH", HandRank.royal_flush),
        )
    )
    def test_rank(self, cards, rank):
        hand = Hand.from_string(cards)
        assert hand.rank == rank

    @pytest.mark.parametrize(
        "cards1, cards2",
        (
            ("4H 4C 7H 8H 9H", "5C 5S 8C 9C TC"),
            ("2C 3C 4C 5C 6C", "3H 4H 5H 6H 7H"),
            # TODO: Add additional hands for comparison
        ),
    )
    def test_high_card_in_rank_comparison(self, cards1, cards2):
        h1 = Hand.from_string(cards1)
        h2 = Hand.from_string(cards2)
        assert h2 > h1

    @pytest.mark.parametrize(
        "cards1, cards2",
        (
            ("4H 4C 7H 8H 9H", "4C 4S 8C 9C TC"),
            # TODO: Add additional hands for comparison
        ),
    )
    def test_high_card_not_in_rank_comparison(self, cards1, cards2):
        h1 = Hand.from_string(cards1)
        h2 = Hand.from_string(cards2)
        assert h2 > h1
