#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    通过实现 __len__ 和 __getitem__ 这两个特殊方法，FranchDeck就跟一个Python自有
    的序列数据类型一样，可以体现出Python的核心语言特性（例如迭代和切片）。同时这个类
    还可以用于标准库中诸如random.choice、reversed和sorted这些函数。

    首先明确一点，特殊方法的存在是为了被Python解释器调用的，我们自己并不需要调用它们。
    也就是说没有my_object.__len__()这种写法，而应该使用len(my_object)。在执行len(my_object)
    的时候，如果my_object是一个自定义的对象，那么Python会自己去调用其中由你实现的__len__方法。
"""

# 一摞Python风格的纸牌
import collections

# 用以构建只有少量属性但是没有方法的对象，比如数据库条目
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank=rank, suit=suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value


deck = FrenchDeck()

print(len(deck))

# 支持下标索引取值、切片
print(deck[0], deck[-1])
print(deck[:3])
print(deck[12::13])

# 因为实现了__getitem__，所以支持迭代
for card in deck:
    print(card)
for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)


# 排序 2最小、A最大, 黑桃最大、红桃次之、方块再次、桃花最小
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]

deck = sorted(deck, key=spades_high)
print(deck[:5])


# 可以使用shuffle函数
from random import shuffle
shuffle(deck)
print(deck[:3])


# 支持通用对列表操作的方法
from random import choice
print(choice(deck))
