# Directory traversal 
import os
import shutil

# GIF building 
import imageio

# Ploting 
import matplotlib.pyplot as plt 

from animations import (
    _cur_dir # Current directory
)


class AnimateMergeSort:
    """
    Class used to animate the bubble sort algorithm
    """
    def __init__(self, left_arr, right_arr):
        """
        Initializes the class
        """
        # Assuming that both of the arrays are already sorted
        self.left_arr = left_arr
        self.right_arr = right_arr 

    @staticmethod
    def plot_array(
        x_left: list, 
        y_left: list, 
        x_right: list, 
        y_right: list,
        filename: str, 
        check_index_left: int = None, 
        check_color_left: str = None,
        check_index_right: int = None, 
        check_color_right: str = None,
        left_line_index: int = None,
        right_line_index: int = None 
        ):
        """
        A helper method for the animation of sorting. 

        Plots a barplot given x, y and other parameters
        """
        fig = plt.figure(figsize=(12, 10))

        # Calculating the y max and y min coordinates
        

        # Ploting the original array
        plt.subplot(2, 2, 1)
        bar1 = plt.bar(x_left, y_left, color='blue', edgecolor='black')
        if check_index_left is not None:
            bar1[check_index_left].set_color(check_color_left)
            bar1[check_index_left].set_edgecolor('black')

        if left_line_index is not None:
            plt.axvline(x=left_line_index + 0.5, color='red', label='Elements to check')
            plt.legend(loc = "lower left")

        plt.xlabel("Array index")
        plt.ylabel("Left array values")

        plt.subplot(2, 2, 2)
        bar2 = plt.bar(x_right, y_right, color='blue', edgecolor='black')
        if check_index_right is not None:
            bar2[check_index_right].set_color(check_color_right)
            bar2[check_index_right].set_edgecolor('black')

        if right_line_index is not None:
            plt.axvline(x=right_line_index + 0.5, color='red', label='Elements to check')
            plt.legend(loc = "lower left")

        plt.xlabel("Array index")
        plt.ylabel("Right array values")

        plt.show()
        plt.savefig(filename)
        plt.close()

    def animate_sorting(
        self, 
        animation_speed: float = 1,
        gif_dir: str = 'merge_sort_animation',
        gif_name: str = 'merge sort animation.gif'
        ):
        # Creating the temporary directory for frames
        _gif_dir = os.path.join(_cur_dir, gif_dir)
        if not os.path.exists(_gif_dir):
            os.mkdir(_gif_dir)

        # Creating the temporary directory for frames
        _tmp_dir = os.path.join(_gif_dir, 'tmp')
        if not os.path.exists(_tmp_dir):
            os.mkdir(_tmp_dir)

        # Arrays length
        _n = len(self.left_arr)
        _k = len(self.right_arr)

        # Defining the left and right x coordinates
        _x_left = [i for i in range(0, _n)]
        _x_right = [i for i in range(0, _k)]

        # List to store the filenames for later GIF creation
        filenames = []
        
        # Definin the initial filename
        filename = f'{_tmp_dir}/frame_0.png'
        filenames.append(filename)

        # Ploting the initial lists
        self.plot_array(
            _x_left, 
            self.left_arr, 
            _x_right, 
            self.right_arr,
            filename=filename
        )

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
                    _arr_sorted[j + elem] = self.left_arr[elem]
            
            elif i >= _n: 
                # This clause means that every element from the left array has been
                # exhaysted 
                for elem in range(j, _k):
                    _arr_sorted[i + elem] = self.right_arr[elem]
            
            else: 
                # This clause means that there are elements in both of the left and right 
                # arrays
                if self.left_arr[i] <= self.right_arr[j]:
                    _arr_sorted[i + j] = self.left_arr[i]
                    i += 1
                else: 
                    _arr_sorted[i + j] = self.right_arr[j]
                    j += 1
            
            # Incrementing the h 
            h += 1
        
        # Build GIF
        with imageio.get_writer(os.path.join(_gif_dir, gif_name), mode='I', duration=animation_speed) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        
        # Remove files
        for filename in set(filenames):
            os.remove(filename)

        # Removing the tmp dir 
        shutil.rmtree(_tmp_dir)  

if __name__ == '__main__':
    # Defining the left and right elements
    _left_arr = [1, 5]
    _right_arr = [-1, 10]

    # Creating the object 
    obj = AnimateMergeSort(
        _left_arr, 
        _right_arr
    )

    # Animating 
    obj.animate_sorting(animation_speed=1.2)