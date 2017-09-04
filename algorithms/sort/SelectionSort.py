def selection_sort(L):
    """
    Implementation of a selection sort algorithm
    Complexity: O(n^2)
    :param L: List-object
    """
    index = 0
    while index != len(L):
        for i in range(index, len(L)):
            if L[i] < L[index]:
                L[index], L[i] = L[i], L[index]
        index += 1
    return L
