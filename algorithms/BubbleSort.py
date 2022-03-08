class BubbleSort:
    def __init__(self, arr: list):
        self.arr = arr

    def sort(self):
        """
        The bubble sort implementation in Python.
        """
        # Length of the array 
        _n = len(self.arr)

        # Creating the sorted array pointer in memory 
        self.arr_sorted = self.arr.copy()

        # Checking if the array is at least length of 2 
        if _n >= 2:
            # Starting the number of comparisons counter
            _n_comparisons = 0

            # Traversing the whole array from left to right and comparing each element with its adjacent element
            # In every iteration, we decrease the maximum right element that we check 
            for i in range(_n - 1):
                for j in range(_n - i - 1): 
                    left_element = self.arr_sorted[j]
                    right_element = self.arr_sorted[j + 1]

                    # Incrementing the comparison number
                    _n_comparisons += 1

                    if right_element < left_element:
                        self.arr_sorted[j] = right_element
                        self.arr_sorted[j + 1] = left_element
        
            self.n_comparisons = _n_comparisons