# Algorithms and data structures

Examples of various popular data structures and algorithms in Python. 

# Algorithms 

All the algorithms are in the `algorithms directory`. 

Experimentations and showcasing of the algorithms are added in the `algorithms/notebooks` directory,

The base class that checks the input and has the general variables and methods for all the alogirthms is in `algorithms/BaseClass.py` file. 

## Bubble sort 

The class that implements the bubble sort algorithm is in the `algorithms/BubbleSort/BubbleSort.py` file.

## Selection sort 

The class that implements the selection sort algorithm is in the `algorithms/SelectionSort/SelectionSort.py` file.

## Insertion sort 

The class that implements the insertion sort algorithm is in the `algorithms/InsertionSort/InsertionSort.py` file.

## Merge sort

The class that implements the merge sort algorithm is in the `algorithms/MergeSort/MergeSort.py` file.

## Quick sort 

The class that implements the quick sort algorithm is in the `algorithms/QuickSort/QuickSort.py` file.

# Tests 

All the tests are in the `tests` directory. Every algorithm class has a test file that tests its correctness.

To test out if the algorithms are working correctly, run the command:

```
pytest
```

# Animations 

To help get a feel of the algorithms the animations of various sorting methods are available in the `animations` directory. Each of the algorithms sort the same array, but the animations are different because of the underlying implementation.

The array that is sorted: 

```
[5, -1, 19, -6, 20, -10, 2, 9]
```

To animate the algorithms use the following commands:

```
python -m animations.BubbleSortAnimation
python -m animations.InsertionSortAnimation
python -m animations.SelectionSortAnimation
```