# Base class
from algorithms.BaseClass import BaseClass


class QuickSort(BaseClass):
    def __init__(self, arr):
        # Inheriting from base class 
        super().__init__(arr)

        # Indication whether the current element is partitioned or not 
        self.sorted = False
        if self.n <= 1:
            self.sorted = True 

        # Partitioning 
        self.partition()

    def partition(self):
        """
        In this implementation we will use the right most element as a pivot
        """
        if self.n > 1:
            # Extracting the right most element 
            _pivot = self.arr[-1]

            # Saving the pivot element to memory 
            self.pivot = [_pivot] 

            # Creating the left and right lists
            _left_arr = []
            _right_arr = []

            for i in range(self.n - 1):
                # The item to check 
                _ith_element = self.arr[i]

                # Populating the right and left elements
                if _ith_element <= _pivot:
                    _left_arr.append(_ith_element)
                else: 
                    _right_arr.append(_ith_element)
            
            # Recursevly partitioning the gotten lists
            self.left = QuickSort(_left_arr)
            self.right = QuickSort(_right_arr)
    
    def sort(self):
        """
        Merges the left and right arrays. 
        The element between the two lists is the _pivot element
        """
        if not self.left.sorted:
            self.left.sort()

        if not self.right.sorted:
            self.right.sort()

        if self.left.sorted and self.right.sorted:
            self.arr = self.left.arr + self.pivot + self.right.arr 

        self.sorted = True