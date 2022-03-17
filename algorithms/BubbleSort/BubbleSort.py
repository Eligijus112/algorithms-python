# Base class 
from algorithms.BaseClass import BaseClass


class BubbleSort(BaseClass):
    def __init__(self, arr: list):
        """
        Object constructor 

        Arguments
        ---------
        arr: list
            The array to be sorted.
        
        Returns
        -------
        None; 
            The array is save to memory
        """
        # Inheriting the base class constructor
        super().__init__(arr)

    def sort(self) -> None:
        """
        The bubble sort implementation in Python.

        Arguments
        ---------
        save_intermediate: bool 
            Whether to save the intermediate results to a master list or not. 
            The intermediate saved results can be used for visualization, analysis, etc.

        Returns
        -------
        None; The sorted array is saved to memory as a **arr_sorted** variable
        """
        # Creating the sorted array pointer in memory 
        self.arr_sorted = self.arr.copy()

        # Checking if the array is at least length of 2 
        if self.n >= 2:
            # Initiating the iteration counter 
            _n_iter = 0

            # Traversing the whole array from left to right and comparing each element with its adjacent element
            # In every iteration, we decrease the maximum right element that we check 
            for i in range(self.n - 1):
                # Initiating the clause to break the loop; 
                # This will happen if no changes are made in the elements, 
                # meaning that the array is already sorted
                _cur_changes = 0

                for j in range(self.n - i - 1): 
                    # Incrementing the iterations
                    _n_iter += 1

                    left_element = self.arr_sorted[j]
                    right_element = self.arr_sorted[j + 1]

                    # Incrementing the comparison number
                    if right_element < left_element:
                        # Switching the left and right elements
                        self.arr_sorted[j] = right_element
                        self.arr_sorted[j + 1] = left_element

                        # Incrementing the comparison counter
                        _cur_changes += 1

                if _cur_changes == 0:
                    break

            # Saving the stats to memory 
            self.n_iter = _n_iter