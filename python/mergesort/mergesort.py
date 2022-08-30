from collections import deque
from typing import Iterable, List


def mergesort(x: List[int]) -> List[int]:
    pass


def _merge(left: Iterable[int], right: Iterable[int]) -> List[int]:
    """Merges the given lists into a single list.
    Time Complexity: O(n)

    :param left: sorted list of integers
    :param right: sorted list of integers
    :return: all elements of left and right in sorted order
    """
    left_idx = 0
    right_idx = 0
    merged = deque()

    while left_idx < len(left) and right_idx < len(right):




if __name__ == '__main__':
    pass