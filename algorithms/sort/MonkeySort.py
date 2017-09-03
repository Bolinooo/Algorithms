import random

def monkey_sort(L):
    """
    Implementation of a monkey sort algorithm
    Complexity: O(?)
    :param L: List-object
    """
    while not sorted(L):
        random.shuffle(L)

