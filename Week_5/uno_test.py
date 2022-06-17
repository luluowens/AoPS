from uno import UnoCard, UnoDeck, UnoPile, UnoPlayer
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_Uno_Cards(self) :
        uno_card1 = UnoCard(3, "blue")
        uno_card2 = UnoCard(5, "blue")
        uno_card3 = UnoCard(3, "green")
        uno_card4 = UnoCard(5, "green")
        self.assertEqual(uno_card1.is_match(uno_card2), True)
        self.assertEqual(uno_card1.is_match(uno_card3), True)
        self.assertEqual(uno_card1.is_match(uno_card4), False)

    def test_Uno_Deck(self) :
        uno_deck = UnoDeck()
        self.assertEqual(len(uno_deck.deck), 100)

if __name__ == '__main__':
    unittest.main()
