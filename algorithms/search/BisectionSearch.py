def bisection_search1(L, e):
    """
    Implementation 1 for the divide-and-conquer algorithm
    Complexity: O(n log n)
    :param L: List-object
    :param e: Element to look for
    :return: Boolean value if element has been found
    """
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisection_search1(L[:half], e)
        else:
            return bisection_search1(L[half:], e)


def bisection_search2(L, e):
    """
       Implementation 2 for the divide-and-conquer algorithm
       Complexity: O(log n)
       :param L: List-object
       :param e: Element to look for
       :return: Boolean value if element has been found
       """
    def helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return helper(L, e, low, mid - 1)
        else:
            return helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return helper(L, e, 0, len(L) - 1)
