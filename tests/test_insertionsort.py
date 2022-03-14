# Main class to test 
from algorithms.InsertionSort.InsertionSort import InsertionSort

def test_sorting():
     # Arrange 
    a = [-5, 1, 158, 0, -99, 56]

    # Act 
    obj = InsertionSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [-99, -5, 0, 1, 56, 158]

def test_worst_case():
     # Arrange 
    a = [99, 10, 0, -10, -99]

    # Act 
    obj = InsertionSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [-99, -10, 0, 10, 99]

def test_best_case():
    # Arrange 
    a = [-99, -10, 0, 10, 99]

    # Act 
    obj = InsertionSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [-99, -10, 0, 10, 99]

def test_empty_array():
    # Arrange 
    a = []

    # Act 
    obj = InsertionSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == []

def test_one_element():
    # Arrange 
    a = [1]

    # Act 
    obj = InsertionSort(a)
    obj.sort()

    # Assert 
    assert obj.arr_sorted == [1]