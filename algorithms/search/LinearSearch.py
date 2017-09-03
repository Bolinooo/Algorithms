def linear_search(L, e):
    """
    Function of linear searching a list to look for specific element
    Complexity: O(n)
    :param L: List-object
    :param e: Element to look for
    :return: Boolean value if element has been found
    """
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
