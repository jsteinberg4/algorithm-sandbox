from datetime import datetime
import random
from typing import List

import pytest

from mergesort import mergesort

# Consistent randomness
NOW = datetime.now().date()
SEED = hash(NOW)


def _sort_example(x) -> List:
    return list(mergesort(x))


def test_mergesort_presorted():
    x = list(range(3))
    assert x == _sort_example(x)


def test_mergesort_reverse_ordered():
    x = list(range(10, 0, -1))
    assert x[::-1] == _sort_example(x), "mergesort failed to reverse a list"


def test_mergesort_random_n50():
    random.seed(SEED)
    unsorted = [random.randint(-100, 100) for _ in range(8)]
    sorted_ = _sort_example(unsorted)
    assert sorted(unsorted) == sorted_


def test_mergesort_empty():
    assert [] == _sort_example([])


def test_mergesort_none_throws_value_error():
    with pytest.raises(ValueError):
        mergesort(None)
