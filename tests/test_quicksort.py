# Importing the main framework to test 
from algorithms.QuickSort.QuickSort import QuickSort

def test_partitioning():
    # Arrange
    a = [-5, 2, 1]

    # Act 
    obj = QuickSort(a)

    # Assert 
    assert obj.pivot == [1] 
    assert obj.left.arr == [-5]
    assert obj.right.arr == [2]

def test_merge_sort_full():
    """
    Tests the full implementation of merge sort 
    """
    # Arrange 
    a = [5, -1, -99, 168, 54, 12, 3]

    # Act 
    obj = QuickSort(a)
    obj.sort()

    # Asserting 
    assert obj.arr == [-99, -1, 3, 5, 12, 54, 168]