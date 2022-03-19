# Importing the base class
from algorithms.BaseClass import BaseClass


class SelectionSort(BaseClass):
    def __init__(
        self, 
        arr:list
        ):
        # Inheriting the base class
        super().__init__(arr)

    def sort(self):
        """
        The selection sorting implemenetation
        """
        # Creating a copy of the original array 
        _sorted_arr = self.arr.copy()

        # Iteration counter
        _n_iter = 0

        # Iterating over the original array 
        for i in range(self.n):
            # The ith coordinate is the one which will be changed
            # with the smallest element from the whole list 

            for j in range(i + 1, self.n):
                # Iterating over the whole list to the right from the ith coordinate 
                # and checking if there are any smaller elements
                _ith_element = _sorted_arr[i]
                _jth_element = _sorted_arr[j]
                if _sorted_arr[i] >= _sorted_arr[j]:
                    _sorted_arr[i] = _jth_element
                    _sorted_arr[j] = _ith_element
                
                # Incrementing the iteration counter 
                _n_iter += 1
        
        # Saving the sorted array to memory 
        self.arr_sorted = _sorted_arr