import turtle
import math


bob = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)


circle2(bob, 50)

print(bob)
input()