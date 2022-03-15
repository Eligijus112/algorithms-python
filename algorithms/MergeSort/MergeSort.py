# Dir traversal 
import os 

class MergeSortNode:
    def __init__(self, arr):
        # Ensuring the correct type 
        if type(arr) != list:
            raise TypeError("Expected a list")
        
        # Saving the array to memory 
        self.arr = arr

        # Saving the length of the array 
        self.n = len(arr)

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
            # right nodes
            self.left = MergeSortNode(left_arr)
            self.right = MergeSortNode(right_arr)
        else: 
            # This indicates that the current node is the bottom one
            self.left = None 
            self.right = None 

    def merge(self):
        """
        Merges the two nodes to the left and on the right
        """
        if self.n > 1:
            # Extracting the arrays
            _left_arr = self.left.arr
            _right_arr = self.right.arr

            # Arrays length
            _n = len(_left_arr)
            _k = len(_right_arr)

            # Creating the empty sorted array 
            _arr_sorted = [None] * (_n + _k)

            # The bellow algorithms assumes that both _left_arr and _right_arr
            # are already sorted
            i = 0
            j = 0
            while (i < _n) or (j < _k): 
                if _left_arr[i] <= _right_arr[j]:
                    _arr_sorted[i + j] = _left_arr[i]
                    
                    i +=1
                else: 
                    _arr_sorted[i + j] = _right_arr[j]

                    j += 1
        
        self.arr = _arr_sorted