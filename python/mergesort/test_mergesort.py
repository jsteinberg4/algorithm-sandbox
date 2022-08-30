from datetime import datetime
from itertools import product
import random
from typing import List

import pytest

from mergesort import mergesort, parallel_mergesort

# Consistent randomness
NOW = datetime.now().date()
SEED = hash(NOW)


def _sort_example(x, parallel: bool) -> List:
    if parallel:
        return list(parallel_mergesort(x))
    else:
        return list(mergesort(x))


@pytest.mark.parametrize("parallel", [False, True])
def test_mergesort_presorted(parallel: bool):
    x = list(range(3))
    assert x == _sort_example(x, parallel)


@pytest.mark.parametrize("parallel", [False, True])
def test_mergesort_reverse_ordered(parallel: bool):
    x = list(range(10, 0, -1))
    assert x[::-1] == _sort_example(x, parallel), "mergesort failed to reverse a list"


# @pytest.mark.parametrize('parallel,n', [(True, 3899), (True, 3900)]) # Shows where ThreadPoolExecutor fails for me
@pytest.mark.parametrize("parallel,n", list(product([False, True], [50, 100, 1_000])))
def test_mergesort_random_n(parallel: bool, n: int):
    random.seed(SEED)
    unsorted = [random.randint(-100, 100) for _ in range(n)]
    sorted_ = _sort_example(unsorted, parallel)
    assert sorted(unsorted) == sorted_


@pytest.mark.parametrize("parallel", [False, True])
def test_mergesort_empty(parallel: bool):
    assert [] == _sort_example([], parallel)


@pytest.mark.parametrize("parallel", [False, True])
def test_mergesort_none_throws_value_error(parallel: bool):
    with pytest.raises(ValueError):
        mergesort(None)
