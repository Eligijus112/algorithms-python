# Main class to test 
from algorithms.SelectionSort.SelectionSort import SelectionSort

def test_sorting():
     # Arrange 
    a = [-5, 1, 158, 0, -99, 56]

    # Act 
    obj = SelectionSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [-99, -5, 0, 1, 56, 158]