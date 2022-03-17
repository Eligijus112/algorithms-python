# OS traversal 
import os 

# Importing the base class 
from algorithms.BaseClass import BaseClass


class InsertionSort(BaseClass):
    def __init__(
        self, 
        arr: list
        ):
        # Inheriting the base class constructor
        super().__init__(arr)        

        # Infering the local file path
        self.current_dir = os.path.dirname(os.path.realpath(__file__))

    def sort(self):
        """
        Method that applies the Insertion Sort algorithm to the array 
        in memory
        """
        if len(self.arr) < 2:
            self.arr_sorted = self.arr 
        else:
            # Creating the empty "sorted" array with length of n 
            arr_sorted = [None] * self.n 

            # Saving the first element to the sorted array 
            arr_sorted[0] = self.arr[0] 

            # Stating the iteration counter 
            _n_iter = 0 

            # Looping through the original array and putting elements in the 
            # "sorted" algorithm to the correct places 
            for i in range(1, self.n):
                # Extracting the current element in the raw array 
                _ith_element = self.arr[i]

                # Looping through the "sorted" part and putting the element where it 
                # belongs 
                j = 0
                while (j < i) and (_ith_element >= arr_sorted[j]):
                    # Incrementing the index 
                    j += 1

                    # Incrementing the iteration count 
                    _n_iter += 1
                
                # Shifting all the elements from the jth coordinate to the right 
                arr_sorted[(j + 1):(i + 1)] = arr_sorted[j:i]  
                
                # Placing the number to the right coordinate
                arr_sorted[j] = _ith_element 

            # Saving the sorted array to memory 
            self.arr_sorted = arr_sorted