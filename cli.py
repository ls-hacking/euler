from collections import Counter
import logging

from poker.hand import Hand


# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def main():
    wins = Counter()
    with open("p054_poker.txt", "r+") as f:
        for text in f:
            p1, p2 = hands_from_text(text)
            logger.debug(f"p1 rank: {p1.rank}")
            logger.debug(f"p2 rank: {p2.rank}")
            if p1 > p2:
                logger.debug("winner: 1")
                wins.update(('Player 1', ))
            elif p2 > p1:
                logger.debug("winner: 2")
                wins.update(('Player 2', ))
            else:
                wins.update(('draw', ))
    print("Wins:")
    for player, wins in wins.most_common():
        print(f" - {player}: {wins}")

def hands_from_text(text):
    p1_cards = text[:14]
    p2_cards = text[15:].strip()
    logger.debug(f"cards: {p1_cards}/{p2_cards}")
    return (
        Hand.from_string(p1_cards),
        # use strip() to remove he newline (if present)
        Hand.from_string(p2_cards),
    )


if __name__ == "__main__":
    main()
