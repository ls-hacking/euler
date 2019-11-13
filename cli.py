from collections import Counter

from poker.hand import Hand


def main():
    wins = Counter()
    with open("p054_poker.txt", "r+") as f:
        for text in f:
            p1, p2 = hands_from_text(text)
            if p1 > p2:
                wins.update(('player 1', ))
            elif p2 > p1:
                wins.update(('player 2', ))
            else:
                wins.update(('draw', ))
    print(wins.most_common())

def hands_from_text(text):
    return (
        Hand.from_string(text[:14]),
        # use strip() to remove the newline (if present)
        Hand.from_string(text[15:].strip()),
    )


if __name__ == "__main__":
    main()
