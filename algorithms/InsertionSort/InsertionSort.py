# Importing the ploting libraries
import matplotlib.pyplot as plt
import seaborn as sns 
import imageio

# OS traversal 
import os 

class InsertionSort:
    def __init__(self, arr: list):
        # Checking type
        if not isinstance(arr, list):
            raise TypeError("Array must be a list")
        
        # Saving to memory 
        self.arr = arr
        self.n = len(arr)

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
        hide_index: list = None
        ):
        """
        A helper method for the animation of sorting. 

        Plots a barplot given x, y and other parameters
        """
        bar = plt.bar(x, y, color=color, edgecolor='black')
        bar.y_max = y_max
        bar.y_min = y_min

        if hide_index is not None: 
            # Making the bars invisible
            for i in hide_index:
                bar[i].set_color('white')
                bar[i].set_edgecolor('white')

        if check_index is not None:
            bar[check_index].set_color(check_color)
            bar[check_index].set_edgecolor('black')

            bar[check_index - 1].set_color(check_color)
            bar[check_index - 1].set_edgecolor('black')
        
        plt.title(title_text)
        plt.xlabel('Array index')
        plt.ylabel('Array values')
        plt.show()

        plt.savefig(filename)
        plt.close()

    def animate_sorting(self, animation_speed: float = 1):
        """
        Method to animate the insertion sort 
        """
        # Creating the empty "sorted" array with length of n 
        arr_sorted = [0] * self.n 

        # Saving the first element to the sorted array 
        arr_sorted[0] = self.arr[0]

        # Creating the x coordinates for the boxplot 
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
        filenames.append(filename)

        # Ploting the current sorted array 
        self.plot_array(
            _x, 
            arr_sorted, 
            color='blue',
            filename=filename,
            y_min=_y_min,
            y_max=_y_max,
            title_text='First iteration of the sorted array',
            hide_index=range(1, _n)
        )

        # Starting the animation frames
        _frame_iter = 1

        for i in range(1, self.n):
            # Extracting the current element in the raw array 
            _ith_element = self.arr[i]

            # Looping through the "sorted" part and putting the element where it 
            # belongs 
            j = i
            clause = True
            while j >= 1 and clause:

                # Creating the tmp array
                arr_sorted[j] = _ith_element

                # Creating the filename
                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)
                _frame_iter += 1

                # Ploting 
                self.plot_array(
                    _x, 
                    arr_sorted, 
                    color='blue', 
                    filename=filename, 
                    y_min=_y_min, 
                    y_max=_y_max, 
                    title_text='Checking...',
                    check_index=j, 
                    check_color='yellow',
                    hide_index=range(i + 1, _n)   
                )

                # Extracting the elements used for checking 
                _left_element = arr_sorted[j - 1]
                _right_element = arr_sorted[j]

                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)
                _frame_iter += 1

                if _left_element > _right_element:
                    arr_sorted[j - 1] = _right_element
                    arr_sorted[j] = _left_element

                    self.plot_array(
                        _x, 
                        arr_sorted, 
                        color='blue', 
                        filename=filename, 
                        y_min=_y_min, 
                        y_max=_y_max, 
                        title_text='Elements switched',
                        check_index=j, 
                        check_color='red',
                        hide_index=range(i + 1, _n)
                    )

                    j += -1
                else: 
                    self.plot_array(
                        _x, 
                        arr_sorted, 
                        color='blue', 
                        filename=filename, 
                        y_min=_y_min, 
                        y_max=_y_max, 
                        title_text='Elements are in order',
                        check_index=j, 
                        check_color='green',
                        hide_index=range(i + 1, _n)
                    )
                    clause = False

        # Build GIF
        with imageio.get_writer(os.path.join(_gif_dir, 'insertion_sort.gif'), mode='I', duration=animation_speed) as writer:
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
    obj = InsertionSort(a)

    # Animation method
    obj.animate_sorting(1.5)