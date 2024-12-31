#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/1 05:20'

"""
P45 1-1  一摞有序的纸牌  Python 3.4
"""

import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])  # namedtuple,构建只有少数属性但是没有方法的对象


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):   # 实现该方法使对象可迭代
        return self._cards[position]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[-1])

    print('-'*50)
    # 从一个序列中随机选出一个元素
    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print(type(choice(deck)))

    print('-' * 50)
    # 查看最上面3张
    print(deck[:3])

    # 只看牌面是A的牌 -- 先抽出索引是12的那张牌，然后每隔13张拿1张
    print(deck[12::13])

    print('-' * 50)

    # 迭代
    for card in deck:
        print(card)

    print('-'*30)
    # 反向迭代
    for card in reversed(deck):
        print(card)

    print('-' * 50)
    # P48 in
    print(Card('Q', 'hearts') in deck)
    print(Card('Q', 'bearts') in deck)

    print('-' * 50)
    # P48 用点数来确定扑克牌大小
    # 2最小，A最大；spades > hearts > diamonds > clubs
    # clubs 2 -> 0,  spades A -> 51
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    # 对牌进行升序排序
    for card in sorted(deck, key=spades_high):
        print(card)
