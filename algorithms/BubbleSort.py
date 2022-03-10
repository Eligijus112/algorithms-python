# Importing the ploting libs
import matplotlib.pyplot as plt
import imageio

# OS traversal 
import os 


class BubbleSort:
    def __init__(self, arr: list):
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
            # Starting the number of comparisons counter
            _n_comparisons = 0
            
            # Intermediate results placeholder
            _intermediate_results = []

            # Traversing the whole array from left to right and comparing each element with its adjacent element
            # In every iteration, we decrease the maximum right element that we check 
            for i in range(self.n - 1):
                for j in range(self.n - i - 1): 
                    left_element = self.arr_sorted[j]
                    right_element = self.arr_sorted[j + 1]

                    # Incrementing the comparison number
                    _n_comparisons += 1

                    if right_element < left_element:
                        # Switching the left and right elements
                        self.arr_sorted[j] = right_element
                        self.arr_sorted[j + 1] = left_element

                    if save_intermediate:
                        _intermediate_results.append(self.arr_sorted.copy())

            # Saving the stats to memory 
            self.n_comparisons = _n_comparisons
            self.intermediate_results = _intermediate_results

    def animate_sorting(
        self,
        animation_speed: float = 1
        ):
        """
        Creates a .gif about how the sorting took place
        """
        # Creating the tmp dir for gifs
        _tmp_dir = os.path.join(self.current_dir, 'tmp')
        if not os.path.exists(_tmp_dir):
            os.mkdir(_tmp_dir)

        # Creating the directory for the final gif 
        _gif_dir = os.path.join(self.current_dir, 'gifs')
        if not os.path.exists(_gif_dir):
            os.mkdir(_gif_dir)
        _n = self.n

        # Creating the x index 
        _x = [i for i in range(1, _n + 1)]

        # Infering the y limits 
        _y_min = min(self.arr) - 1
        _y_max = max(self.arr) + 1

        filenames = []

        # Ploting the initial array 
        bar = plt.bar(_x, self.arr, color='blue', edgecolor='black')
        bar.y_max = _y_max
        bar.y_min = _y_min
        plt.title('Initial array')
        plt.xlabel('Array index')
        plt.ylabel('Array values')
        plt.show()
        filename = f'{_tmp_dir}/frame_0.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.close()

        # Reseting the sorted array
        self.arr_sorted = self.arr.copy()

        # Animating the sorting 
        _frame_iter = 1
        for i in range(self.n - 1):
            for j in range(self.n - i - 1): 
                # Ploting the initial array
                bar = plt.bar(_x, self.arr_sorted, color='blue', edgecolor='black')
                bar.y_max = _y_max
                bar.y_min = _y_min
                plt.xlabel('Array index')
                plt.ylabel('Array values')

                # Highlighting the current element
                bar[j].set_color('yellow')
                bar[j].set_edgecolor('black')

                bar[j + 1].set_color('yellow')
                bar[j + 1].set_edgecolor('black')
                plt.title('Checking elements...')

                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)
                plt.savefig(filename)
                plt.close()
                _frame_iter += 1

                # Extracting the elements to check 
                left_element = self.arr_sorted[j]
                right_element = self.arr_sorted[j + 1]

                if right_element < left_element:
                    # Switching the left and right elements
                    self.arr_sorted[j] = right_element
                    self.arr_sorted[j + 1] = left_element

                    # Ploting the array
                    bar = plt.bar(_x, self.arr_sorted, color='blue', edgecolor='black')
                    bar.y_max = _y_max
                    bar.y_min = _y_min
                    plt.xlabel('Array index')
                    plt.ylabel('Array values')

                    # Setting the colors to red 
                    plt.title("Switching the elements")
                    bar[j].set_color('red')
                    bar[j].set_edgecolor('black')

                    bar[j + 1].set_color('red')
                    bar[j + 1].set_edgecolor('black')

                    filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                    filenames.append(filename)
                    plt.savefig(filename)
                    plt.close()
                else: 
                    bar = plt.bar(_x, self.arr_sorted, color='blue', edgecolor='black')
                    bar.y_max = _y_max
                    bar.y_min = _y_min
                    plt.xlabel('Array index')
                    plt.ylabel('Array values')

                    # Setting the colors to green 
                    plt.title("Elements are in order")
                    bar[j].set_color('green')
                    bar[j].set_edgecolor('black')

                    bar[j + 1].set_color('green')
                    bar[j + 1].set_edgecolor('black')

                    filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                    filenames.append(filename)
                    plt.savefig(filename)
                    plt.close()
                
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
    a = [5, -1, 19, -6, 20, -10]

    # Creating the object 
    obj = BubbleSort(a)

    # Animation method
    obj.animate_sorting(1.5)