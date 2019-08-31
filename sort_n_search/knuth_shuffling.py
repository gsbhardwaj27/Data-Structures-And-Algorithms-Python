# The right way to shuffle
import random


def knuth_shuffle(n):
    items = [i for i in range(n)]
    for i in range(n):
        num = random.randint(0, i)
        items[i], items[num] = items[num], items[i]
    return items


if __name__ == '__main__':
    print(knuth_shuffle(0))
    print(knuth_shuffle(1))
    print(knuth_shuffle(2))
    print(knuth_shuffle(5))
    print(knuth_shuffle(10))
