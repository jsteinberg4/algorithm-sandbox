from typing import Iterable, Tuple, List


def mergesort(x: List[int]) -> List[int]:
    """Sorts a list using a recursive mergesort.

    Runtime: O(n^2)
    Ex: mergesort([1,2,3]) -> [1,2,3]
    Ex: mergesort([3,2,1]) -> [1,2,3]
    Ex: mergesort([]) -> []

    :param x: list to be sorted
    :returns: elements of x in non-decreasing order
    :raises ValueError: if x is None
    """
    # Handling edge cases
    if x is None:
        raise ValueError("List to sort cannot be None")
    if len(x) < 2:
        return x

    # Steps:
    # 1) Split list
    left, right = _split(x)

    # 2) Sort left, right
    # 3) merge left, right
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    merged = _merge(left_sorted, right_sorted)

    return merged


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merges the given lists into a single list.
    Time Complexity: O(n)

    :param left: sorted list of integers
    :param right: sorted list of integers
    :return: all elements of left and right in sorted order
    """
    left_idx = 0
    right_idx = 0
    merged = list()

    # Until one list runs out of elements, append the smallest element from
    # either list.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:  # left[left_idx] > right[right_idx]
            merged.append(right[right_idx])
            right_idx += 1

    # If either list has elements remaining, append to the end
    if left_idx < len(left):
        merged.extend(left[left_idx:])
    elif right_idx < len(right):
        merged.extend(right[right_idx:])

    return merged


def _split(whole: List[int]) -> Tuple[List[int], List[int]]:
    """Split a list into two equal* parts

    *if len(whole) is uneven, the left sublist will have 1 more element
    """
    middle = len(whole) // 2
    return whole[:middle], whole[middle:]
