#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    实现对象的打印输出
    对象的绝对值
    对象的bool值
    对象相加、相乘

"""
from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1)

v3 = v1 + v2
print(v3)

v4 = Vector(3, 4)
print(abs(v4))
print(v4 * 3)
print(abs(v4 * 3))
