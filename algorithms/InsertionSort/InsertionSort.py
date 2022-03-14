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
        y_true: list,
        color: str,
        filename: str, 
        title_text: str,
        original_entry_index: int = None,
        original_entry_check_color: str = None,
        check_index_left: int = None,
        check_index_right: int = None,
        check_color: str = None,
        hide_index: list = None
        ):
        """
        A helper method for the animation of sorting. 

        Plots a barplot given x, y and other parameters
        """
        fig = plt.figure(figsize=(12, 10))
        plt.title(title_text)

        # Ploting the original array
        plt.subplot(2, 1, 1)
        bar1 = plt.bar(x, y_true, color='blue', edgecolor='black')
        if original_entry_index is not None:
           bar1[original_entry_index].set_color(original_entry_check_color)
           bar1[original_entry_index].set_edgecolor('black')

        plt.xlabel("Array index")
        plt.ylabel("Original array values")
        plt.title(title_text, fontsize=20)

        plt.subplot(2, 1, 2)
        plt.ylim(min(y_true) - 1, max(y_true) + 1)
        bar2 = plt.bar(x, y, color=color, edgecolor='black')

        if hide_index is not None: 
            # Making the bars invisible
            for i in hide_index:
                bar2[i].set_color('white')
                bar2[i].set_edgecolor('white')

        if check_index_left is not None:
            bar2[check_index_left].set_color(check_color)
            bar2[check_index_left].set_edgecolor('black')

        if check_index_right is not None:
            bar2[check_index_right].set_color(check_color)
            bar2[check_index_right].set_edgecolor('black')

        plt.xlabel("Array index")
        plt.ylabel("Array value")
        plt.title("Sorted array")

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

        # List to store the filenames for later GIF creation
        filenames = []
        
        # Definin the initial filename
        filename = f'{_tmp_dir}/frame_0.png'
        filenames.append(filename)

        # Ploting the current sorted array 
        self.plot_array(
            x=_x, 
            y=arr_sorted, 
            y_true=self.arr,
            color='blue',
            filename=filename,
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
            while j > 0 and clause:
                # Creating the filename
                filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
                filenames.append(filename)
                _frame_iter += 1

                # Ploting 
                self.plot_array(
                    x=_x, 
                    y=arr_sorted, 
                    y_true=self.arr,
                    color='blue', 
                    filename=filename, 
                    original_entry_index=i,
                    original_entry_check_color='yellow',
                    title_text='Checking...',
                    check_index_right=j - 1,
                    check_color='yellow',
                    hide_index=range(i, _n)   
                )

                # Extracting the jth element to check. This entry is already in the list
                _jth_element = arr_sorted[j - 1]

                if _ith_element < _jth_element:
                    if j != 0:
                        j += -1
                    else: 
                        clause = False
                else: 
                    clause = False

            # Shifting all the elements from the jth coordinate to the right 
            arr_sorted[(j + 1):(i + 1)] = arr_sorted[j:i]  
            
            # Placing the number to the right coordinate
            arr_sorted[j] = _ith_element

            filename = f'{_tmp_dir}/frame_{_frame_iter}.png'
            filenames.append(filename)
            _frame_iter += 1

            self.plot_array(
                    x=_x, 
                    y=arr_sorted, 
                    y_true=self.arr,
                    color='blue', 
                    filename=filename, 
                    original_entry_index=i,
                    original_entry_check_color='yellow',
                    title_text='Added the element here',
                    check_index_left=j, 
                    check_color='red',
                    hide_index=range(i + 1, _n)   
                )

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