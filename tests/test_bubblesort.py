# Main framework to test 
from algorithms.BubbleSort import BubbleSort

def test_bubblesort():
    # Arrange 
    a = [-5, 1, 158, 0, -99, 56]

    # Act 
    obj = BubbleSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [-99, -5, 0, 1, 56, 158]