def bubble_sort(L):
    """
    Implementation of the bubble sort algorithm
    Complexity: O(n^2)
    :param L: List-object
    :return: Sorted list-object
    """
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j], L[j-1] = L[j-1], L[j]
    return L
