# Importing the main framework for sorting 
from algorithms.SelectionSort.SelectionSort import SelectionSort

# Importing animations constants 
from animations import (
    _arr, # Array to animate
    _cur_dir # Current directory
)

# Third party packages 
import matplotlib.pyplot as plt 

# Directory traversal 
import os
import shutil

# GIF building 
import imageio


class AnimateSelectionSort(SelectionSort):
    """
    Class used to animate the bubble sort algorithm
    """
    def __init__(self, arr):
        """
        Initializes the class
        """
        # Initializing the base class 
        super().__init__(arr)

    @staticmethod
    def plot_array(
        x: list, 
        y: list, 
        color: str,
        filename: str, 
        y_min: float, 
        y_max: float,
        title: str,
        check_index_min: int = None,
        check_index_cur: int = None,
        check_color: str = None,
        ):
        """
        A helper method for the animation of sorting. 

        Plots a barplot given x, y and other parameters
        """
        bar = plt.bar(x, y, color=color, edgecolor='black')
        bar.y_max = y_max
        bar.y_min = y_min

        if check_index_min is not None and check_index_cur is not None:
            bar[check_index_min].set_color(check_color)
            bar[check_index_min].set_edgecolor('black')

            bar[check_index_cur].set_color(check_color)
            bar[check_index_cur].set_edgecolor('black')
        
        plt.title(title)
        plt.xlabel('Array index')
        plt.ylabel('Array values')
        plt.show()

        plt.savefig(filename)
        plt.close()

    def animate_sorting(
        self, 
        animation_speed: float = 1,
        gif_dir: str = 'selection_sort_animation',
        gif_name: str = 'selection sort animation.gif',
        ):
        # Creating the temporary directory for frames
        _gif_dir = os.path.join(_cur_dir, gif_dir)
        if not os.path.exists(_gif_dir):
            os.mkdir(_gif_dir)

        # Creating the temporary directory for frames
        _tmp_dir = os.path.join(_gif_dir, 'tmp')
        if not os.path.exists(_tmp_dir):
            os.mkdir(_tmp_dir)

        # Extracting the length of array
        _n = self.n

        # Creating the x index 
        _x = [i for i in range(1, _n + 1)]

        # Infering the y limits 
        _y_min = min(self.arr) - 1
        _y_max = max(self.arr) + 1

        # List to store the filenames for later GIF creation
        filenames = []
        
        # Definin the initial filename
        filename = f'{_tmp_dir}/frame_0.png'
        filenames.append(filename)

        # Ploting the initial array
        self.plot_array(
            x=_x,
            y=self.arr,
            color='blue',
            filename=filename,
            y_min=_y_min,
            y_max=_y_max,
            title='Initial array'
        )

        # Reseting the sorted array
        arr_sorted = self.arr.copy()

        # Animating the sorting 
        _frame_iter = 1
        for i in range(_n):
            for j in range(i + 1, _n): 
                # Creating the filename
                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)

                # Ploting the array
                self.plot_array(
                    x=_x,
                    y=arr_sorted,
                    color='blue',
                    filename=filename,
                    y_min=_y_min,
                    y_max=_y_max,
                    title='Checking elements...',
                    check_index_min=i,
                    check_index_cur=j,
                    check_color='yellow'
                )

                # Incrementing the frame counter
                _frame_iter += 1

                # Extracting the elements to check 
                _ith_element = arr_sorted[i]
                _jth_element = arr_sorted[j]

                # Creating the filename for the comparison part
                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)

                if _jth_element < _ith_element:
                    # Switching the left and right elements
                    arr_sorted[j] = _ith_element
                    arr_sorted[i] = _jth_element

                    # Ploting the array
                    self.plot_array(
                        x=_x,
                        y=arr_sorted,
                        color='blue',
                        filename=filename,
                        y_min=_y_min,
                        y_max=_y_max,
                        title='Changing the elements',
                        check_index_min=i,
                        check_index_cur=j,
                        check_color='red'
                    )
                else: 
                    # Ploting the array
                    self.plot_array(
                        x=_x,
                        y=arr_sorted,
                        color='blue',
                        filename=filename,
                        y_min=_y_min,
                        y_max=_y_max,
                        title='Elements are in order',
                        check_index_cur=j,
                        check_index_min=i,
                        check_color='green'
                    )
                
                # Incrementing the iteration 
                _frame_iter += 1

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
    # Creating the object 
    obj = AnimateSelectionSort(_arr)

    # Animating 
    obj.animate_sorting(animation_speed=1.2)