# Importing the main framework
from algorithms.MergeSort.MergeSort import MergeSort

def test_merge_sort_min_node():
    """
    The minimal array of two elements
    """
    # Arrange 
    a = [5, -1]

    # Act 
    node = MergeSort(a)
    node.merge_sort()

    # Assert 
    assert node.left.arr == [5]
    assert node.right.arr == [-1]
    assert node.arr == [-1, 5]

def test_node_spliting():
    """
    Test if the node spliting is correct
    """
    # Arrange 
    a = [5, -1, -99, 168, 54, 12, 3]

    # Act 
    node = MergeSort(a)

    # Assert 
    assert node.left.arr == [5, -1, -99]
    assert node.right.arr == [168, 54, 12, 3]

    assert node.left.left.arr == [5]
    assert node.left.left.sorted 
    
    assert node.left.right.arr == [-1, -99]
    assert not node.left.right.sorted

    assert node.right.left.arr == [168, 54]
    assert node.right.right.arr == [12, 3]

def test_merge_sort_full():
    """
    Tests the full implementation of merge sort 
    """
    # Arrange 
    a = [5, -1, -99, 168, 54, 12, 3]

    # Act 
    node = MergeSort(a)
    node.merge_sort()

    # Asserting 
    assert node.arr == [-99, -1, 3, 5, 12, 54, 168]
