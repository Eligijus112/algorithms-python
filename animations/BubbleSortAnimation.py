# Importing the main framework for sorting 
from algorithms.BubbleSort.BubbleSort import BubbleSort

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


class AnimateBubbleSort(BubbleSort):
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
        check_index: int = None,
        check_color: str = None,
        vertical_line_index: int = None,
        ):
        """
        A helper method for the animation of sorting. 

        Plots a barplot given x, y and other parameters
        """
        bar = plt.bar(x, y, color=color, edgecolor='black')
        bar.y_max = y_max
        bar.y_min = y_min

        if check_index is not None:
            bar[check_index].set_color(check_color)
            bar[check_index].set_edgecolor('black')

            bar[check_index + 1].set_color(check_color)
            bar[check_index + 1].set_edgecolor('black')
        
        if vertical_line_index is not None:
            plt.axvline(x=vertical_line_index + 0.5, color='red', label='Max coordinate to be checked')
            plt.legend()

        plt.title(title)
        plt.xlabel('Array index')
        plt.ylabel('Array values')
        plt.show()

        plt.savefig(filename)
        plt.close()

    def animate_sorting(
        self,
        animation_speed: float = 1,
        gif_dir: str = 'bubble_sort_animation',
        gif_name: str = 'bubble sort animation.gif',
        ):
        """
        Creates a .gif about how the sorting took place
        """
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
        self.arr_sorted = self.arr.copy()

        # Animating the sorting 
        _frame_iter = 1
        for i in range(self.n - 1):
            _cur_changes = 0

            for j in range(self.n - i - 1): 
                # Creating the filename
                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)

                # Ploting the array
                self.plot_array(
                    x=_x,
                    y=self.arr_sorted,
                    color='blue',
                    filename=filename,
                    y_min=_y_min,
                    y_max=_y_max,
                    title='Checking elements...',
                    check_index=j,
                    check_color='yellow',
                    vertical_line_index=self.n - i
                )

                # Incrementing the frame counter
                _frame_iter += 1

                # Extracting the elements to check 
                left_element = self.arr_sorted[j]
                right_element = self.arr_sorted[j + 1]

                # Creating the filename for the comparison part
                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)

                if right_element < left_element:
                    # Incrementing the changes counter
                    _cur_changes += 1

                    # Switching the left and right elements
                    self.arr_sorted[j] = right_element
                    self.arr_sorted[j + 1] = left_element

                    # Ploting the array
                    self.plot_array(
                        x=_x,
                        y=self.arr_sorted,
                        color='blue',
                        filename=filename,
                        y_min=_y_min,
                        y_max=_y_max,
                        title='Changing the elements',
                        check_index=j,
                        check_color='red',
                        vertical_line_index=self.n - i
                    )
                else: 
                    # Ploting the array
                    self.plot_array(
                        x=_x,
                        y=self.arr_sorted,
                        color='blue',
                        filename=filename,
                        y_min=_y_min,
                        y_max=_y_max,
                        title='Elements are in order',
                        check_index=j,
                        check_color='green',
                        vertical_line_index=self.n - i
                    )
                
                # Incrementing the iteration 
                _frame_iter += 1
            
            # If no changes were made this means that the array is sorted
            if _cur_changes == 0:
                break

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
    obj = AnimateBubbleSort(_arr)

    # Animating 
    obj.animate_sorting(animation_speed=1.2)