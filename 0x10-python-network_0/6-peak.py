#!/usr/bin/python3
"""
An element in the list is said to be peak if
it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.
"""


def find_peak(A):
    """find pick element"""
    if A == []:
        return None

    def recursive(A, left=0, right=len(A) - 1):
        """helper recursive function"""

        middle = (left + right) // 2

        # check if the middledle element is greater than its neighbors
        if ((middle == 0 or A[middle - 1] <= A[middle]) and
                (middle == len(A) - 1 or A[middle + 1] <= A[middle])):
            return A[middle]

        # If the left neighbor of `middle` is greater than the middledle element,
        # find the peak recursively in the left sublist
        if middle - 1 >= 0 and A[middle - 1] > A[middle]:
            return recursive(A, left, middle - 1)

        # If the right neighbor of `middle` is greater than the middledle element,
        # find the peak recursively in the right sublist
        return recursive(A, middle + 1, right)

    return recursive(A)
