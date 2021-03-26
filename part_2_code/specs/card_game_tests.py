import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame = CardGame()

    def test_if_ace_can_be_found(self):
        card1 = Card("Ace", 1)
        self.assertEqual(True, self.cardgame.check_for_ace(card1))

    def test_find_highest_Card(self):
        card1 = Card("Ace", 1)
        card2 = Card("Queen", 0)
        self.assertEqual(card1, self.cardgame.highest_card(card1, card2))

    def test_total_cards(self):
        card1 = Card("Ace", 1)
        card2 = Card("Queen", 0)
        card3 = Card("Joker", 2)
        cards = (card1, card2, card3)
        self.assertEqual("You have a total of 3", self.cardgame.cards_total(cards))
    
