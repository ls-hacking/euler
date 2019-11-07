import enum


class OrderedEnum(enum.Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class CardValue(OrderedEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14

    @classmethod
    def from_string(cls, s):
        return {
            "2": cls.two,
            "3": cls.three,
            "4": cls.four,
            "5": cls.five,
            "6": cls.six,
            "7": cls.seven,
            "8": cls.eight,
            "9": cls.nine,
            "T": cls.ten,
            "J": cls.jack,
            "Q": cls.queen,
            "K": cls.king,
            "A": cls.ace,
        }[s]


class CardSuit(enum.Enum):
    clubs = enum.auto()
    diamonds = enum.auto()
    hearts = enum.auto()
    spades = enum.auto()

    @classmethod
    def from_string(cls, s):
        return {
            "C": cls.clubs,
            "D": cls.diamonds,
            "H": cls.hearts,
            "S": cls.spades,
        }[s]


class Card:
    def __is_same_class(self, other):
        if not self.__class__ is other.__class__:
            return NotImplemented

    def __ge__(self, other):
        self.__is_same_class(other)
        return self.value >= other.value

    def __gt__(self, other):
        self.__is_same_class(other)
        return self.value > other.value

    def __le__(self, other):
        self.__is_same_class(other)
        return self.value <= other.value

    def __lt__(self, other):
        self.__is_same_class(other)
        return self.value < other.value

    def __eq__(self, other):
        # cards are equal if their values are equal. Suit is not compared
        self.__is_same_class(other)
        return self.value == other.value

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @classmethod
    def from_string(cls, txt: str):
        # TODO: validate format of `txt`
        return cls(
            value=CardValue.from_string(txt[0]),
            suit=CardSuit.from_string(txt[1]),
        )
