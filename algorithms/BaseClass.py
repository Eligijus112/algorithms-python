class BaseClass:
    def __init__(
        self,
        arr: list = [float]
        ):
        """
        The base class for all the algorithms to inherit from 
        """
        # Ensuring the correct type 
        if type(arr) != list:
            raise TypeError("Expected a list")
        
        # Saving the array to memory 
        self.arr = arr

        # Saving the length of the array 
        self.n = len(arr)