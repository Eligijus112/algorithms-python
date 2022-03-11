# Importing the ploting libraries
import matplotlib.pyplot as plt
import imageio

# OS traversal 
import os 


class BubbleSort:
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

        # Empty placeholder
        self.arr = []

        # Checking if the provided arr is of correct type 
        if isinstance(arr, list):
            self.arr = arr
        
        # Saving the length of array for further use 
        self.n = len(arr)

        # Saving the current file directory to memory 
        self.current_dir = os.path.dirname(os.path.realpath(__file__))

    def sort(self, save_intermediate: bool = False) -> None:
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
            # Intermediate results placeholder
            _intermediate_results = []

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

                    if save_intermediate:
                        _intermediate_results.append(self.arr_sorted.copy())

                if _cur_changes == 0:
                    break

            # Saving the stats to memory 
            self.intermediate_results = _intermediate_results
            self.n_iter = _n_iter

    @staticmethod
    def plot_array(
        x: list, 
        y: list, 
        color: str,
        filename: str, 
        y_min: float, 
        y_max: float,
        title_text: str,
        check_index: int = None,
        check_color: str = None,
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
        
        plt.title(title_text)
        plt.xlabel('Array index')
        plt.ylabel('Array values')
        plt.show()

        plt.savefig(filename)
        plt.close()

    def animate_sorting(
        self,
        animation_speed: float = 1
        ):
        """
        Creates a .gif about how the sorting took place
        """
        # Creating the temporary directory for frames
        _tmp_dir = os.path.join(self.current_dir, 'tmp')
        if not os.path.exists(_tmp_dir):
            os.mkdir(_tmp_dir)

        # Creating the directory for the final gif
        _gif_dir = os.path.join(self.current_dir, 'gifs')
        if not os.path.exists(_gif_dir):
            os.mkdir(_gif_dir)

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
                    check_color='yellow'
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
                        check_color='red'
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
                        check_color='green'
                    )
                
                # Incrementing the iteration 
                _frame_iter += 1

        # Build GIF
        with imageio.get_writer(os.path.join(_gif_dir, 'bubble_sort.gif'), mode='I', duration=animation_speed) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        
        # Remove files
        for filename in set(filenames):
            os.remove(filename)

        # Removing the tmp dir 
        os.rmdir(_tmp_dir)

if __name__ == '__main__':
    # Initial array
    a = [5, -1, 19, -6, 20, -10, 2]

    # Creating the object 
    obj = BubbleSort(a)

    # Animation method
    obj.animate_sorting(1.5)