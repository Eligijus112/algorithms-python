# Base class
from algorithms.BaseClass import BaseClass


class MergeSort(BaseClass):
    def __init__(self, arr):
        # Inheriting from base class
        super().__init__(arr)

        # Initiating the recursive splitting of the arrays
        self.split_node()

        # When creating the node, the initial arr in state is not sorted
        self.sorted = False

        if self.n == 1:
            # An array of length 1 is always sorted
            self.sorted = True

    def split_node(self):
        """
        Splits the array into two parts
        """
        if self.n > 1:
            # Calculating the middle point
            middle_point = len(self.arr) // 2

            # Creating the two new arrays
            left_arr = self.arr[:middle_point]
            right_arr = self.arr[middle_point:]

            # Creating the pointers in memory to left and 
            # right subarrays
            self.left = MergeSort(left_arr)
            self.right = MergeSort(right_arr)

    def merge_sort(self):
        """
        Merges the two nodes to the left and on the right
        """
        if not self.left.sorted: 
            self.left.merge_sort()
        
        if not self.right.sorted:
            self.right.merge_sort()

        if self.left.sorted and self.right.sorted:
            # Extracting the arrays
            _left_arr = self.left.arr
            _right_arr = self.right.arr

            # Arrays length
            _n = len(_left_arr)
            _k = len(_right_arr)

            # final array length
            _N = _n + _k

            # Creating the empty sorted array 
            _arr_sorted = [None] * _N

            # The bellow algorithms assumes that both _left_arr and _right_arr
            # are already sorted
            i = 0 # Iterator for the left array 
            j = 0 # Iterator for the right array 
            h = 0 # Iterator for the final array

            while h < _N:
                if j >= _k: 
                    # This clause means that every element from the right array has been 
                    # exhausted
                    for elem in range(i, _n):
                        _arr_sorted[j + elem] = _left_arr[elem]
                
                elif i >= _n: 
                    # This clause means that every element from the left array has been
                    # exhaysted 
                    for elem in range(j, _k):
                        _arr_sorted[i + elem] = _right_arr[elem]
                
                else: 
                    # This clause means that there are elements in both of the left and right 
                    # arrays
                    if _left_arr[i] <= _right_arr[j]:
                        _arr_sorted[i + j] = _left_arr[i]
                        i += 1
                    else: 
                        _arr_sorted[i + j] = _right_arr[j]
                        j += 1
                
                # Incrementing the h 
                h += 1
        
            self.arr = _arr_sorted
            self.sorted = True