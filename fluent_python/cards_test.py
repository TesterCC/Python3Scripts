#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/1 06:09'

import unittest

from fluent_python.cards import Card, FrenchDeck

"""
Unit test to test func
"""


class TestCardsMethods(unittest.TestCase):

    def setUp(self):
        self.beer_card = Card('7', 'diamonds')
        self.deck = FrenchDeck()

    def test_generate_card(self):
        # beer_card = Card('7', 'diamonds')
        self.assertIsNotNone(self.beer_card, msg="Object is None")
        self.assertIsInstance(self.beer_card, Card)
        self.assertEqual(str(self.beer_card), "Card(rank='7', suit='diamonds')")

    def test_frenchdeck(self):
        self.assertEqual(len(self.deck), 52)

    def test_random_get_card(self):
        # 从一个序列中随机选出一个元素
        from random import choice
        self.assertIsInstance(choice(self.deck), Card)


if __name__ == '__main__':
    unittest.main()