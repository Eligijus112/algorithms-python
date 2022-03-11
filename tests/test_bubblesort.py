# Main framework to test 
from algorithms.BubbleSort.BubbleSort import BubbleSort

def test_bubblesort():
    # Arrange 
    a = [-5, 1, 158, 0, -99, 56]

    # Act 
    obj = BubbleSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [-99, -5, 0, 1, 56, 158]

def test_full_bubblesort_algorithm():
    # Arrange 
    b = [9, -1, 19, 2]

    # Act 
    obj = BubbleSort(b)
    obj.sort(save_intermediate=True)
    _intermediate_results = obj.intermediate_results
    
    # Assert
    assert [
        [-1, 9, 19, 2], 
        [-1, 9, 19, 2],
        [-1, 9, 2, 19],
        [-1, 9, 2, 19],
        [-1, 2, 9, 19],
        [-1, 2, 9, 19]
        ] == _intermediate_results

def test_sorted_array():
    # Arrange
    c = [1, 2, 3, 4, 5]

    # Act
    obj = BubbleSort(c)
    obj.sort()

    # This should take 4 iterations to sort the array
    assert obj.n_iter == 4