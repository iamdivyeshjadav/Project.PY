import numpy as np

class DataAnalytics:
    def __init__(self):
        self._array = None

    @staticmethod
    def welcome_message():
        print("\nWelcome To The NumPy Analyzer!")
        print("========================================")

    def _has_array(self) -> bool:
        if self._array is None:
            print("Please Create An Array First.")
            return False
        return True

    def create_array(self):
        while True:
            print("\nSelect The Type Of Array To Create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            print("4. Go Back")
            try:
                choice = int(input("Enter Your Choice: "))
            except ValueError:
                print("Invalid Choice.")
                continue

            if choice == 1:
                try:
                    data = input("Enter the numbers separated by space: ")
                    self._array = np.array(data.split(), dtype=float)
                    print("\nArray Created Successfully:\n", self._array)
                except ValueError:
                    print("Error: Please Enter Numeric Values Only.")
            elif choice == 2:
                try:
                    rows = int(input("Enter The Number Of Rows: "))
                    cols = int(input("Enter The Number Of Columns: "))
                    data = input(f"Enter {rows*cols} Elements For The Array Separated By Space: ")
                    self._array = np.array(data.split(), dtype=float).reshape(rows, cols)
                    print("\nArray Created Successfully:\n", self._array)
                except ValueError:
                    print("Error: Ensure Data Perfectly Matches Dimensions.")
            elif choice == 3:
                try:
                    depth = int(input("Enter Depth: "))
                    rows = int(input("Enter Rows: "))
                    cols = int(input("Enter Columns: "))
                    data = input(f"Enter {depth*rows*cols} Elements Separated By Space: ")
                    self._array = np.array(data.split(), dtype=float).reshape(depth, rows, cols)
                    print("\nArray Created Successfully:\n", self._array)
                except ValueError:
                    print("Error: Ensure Data Perfectly Matches Dimensions.")
            elif choice == 4:
                break
            else:
                print("Invalid Choice.")

    def perform_indexing_slicing(self):
        if not self._has_array(): return

        while True:
            print("\nChoose An Operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            try:
                choice = int(input("Enter Your Choice: "))
            except ValueError:
                print("Invalid Choice.")
                continue

            if choice == 1:
                print(f"Current Array Shape: {self._array.shape}")
                idx = input("Enter Indices Separated By Space (e.g., '0 1'): ")
                try:
                    indices = tuple(map(int, idx.split()))
                    print(f"Value At Index {indices}: {self._array[indices]}")
                except Exception as e:
                    print(f"Indexing Error: {e}")
            elif choice == 2:
                if self._array.ndim != 2:
                    print("Slicing Demonstration Is Optimized For 2D Arrays In This Prompt Context.")
                    print("Current Array:\n", self._array)
                    continue
                try:
                    r_range = input("Enter The Row Range (Start:End): ")
                    c_range = input("Enter The Column Range (Start:End): ")

                    r_start, r_end = map(int, r_range.split(':'))
                    c_start, c_end = map(int, c_range.split(':'))

                    sliced = self._array[r_start:r_end, c_start:c_end]
                    print("\nSliced Array:\n", sliced)
                except ValueError:
                    print("Format Error. Please Use 'Start:End' Notation.")
            elif choice == 3:
                break
            else:
                print("Invalid Choice.")

    def perform_math(self):
        if not self._has_array(): return

        while True:
            print("\nChoose A Mathematical Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Matrix Multiplication / Dot Product (2D)")
            print("3. Go Back")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                data = input(f"Enter the numbers for addition ({self._array.size} numbers separated by space): ")
                try:
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Addition:\n", self._array + second_array)
                except ValueError:
                    print("Error: Arrays Must Have The Exact Same Shape Structure.")

            elif choice == 2:
                data = input(f"Enter the numbers for subtraction ({self._array.size} numbers separated by space): ")
                try:
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Subtraction:\n", self._array - second_array)
                except ValueError:
                    print("Error: Arrays Must Have The Exact Same Shape Structure.")

            elif choice == 3:
                data = input(f"Enter the numbers for multiplication ({self._array.size} numbers separated by space): ")
                try:
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Multiplication:\n", self._array * second_array)
                except ValueError:
                    print("Error: Arrays Must Have The Exact Same Shape Structure.")

            elif choice == 4:
                data = input(f"Enter the numbers for division ({self._array.size} numbers separated by space): ")
                try:
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nResult Of Division:\n", self._array / second_array)
                except ValueError:
                    print("Error: Arrays Must Have The Exact Same Shape Structure.")

            elif choice == 5:
                if self._array.ndim != 2:
                    print("Matrix Multiplication Requires A 2D Array.")
                    continue
                print(f"Your Array Shape Is {self._array.shape}. Second Array Must Have {self._array.shape[1]} Rows.")
                try:
                    r2 = int(input("Enter Columns For The Second Matrix: "))
                    data = input(f"Enter {self._array.shape[1] * r2} Numbers Separated By Space: ")
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape[1], r2)
                    print("\nResult Of Matrix Multiplication:\n", np.dot(self._array, second_array))
                except ValueError:
                    print("Dimension Mismatch Or Invalid Input.")
            elif choice == 4:
                break
            else:
                print("Invalid Choice.")

    def combine_split(self):
        if not self._has_array(): return

        while True:
            print("\nChoose An Option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                data = input("Enter the numbers of another array to combine separated by space: ")
                try:
                    second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
                    print("\nOriginal Array:\n", self._array)
                    print("Second Array:\n", second_array)
                    print("\nCombined Array (Vertical Stack):\n", np.vstack((self._array, second_array)))
                except ValueError:
                    print("Error: Second Array Must Match The Shape Of Your Original Array.")
            elif choice == 2:
                try:
                    splits = int(input("Enter Number Of Splits: "))
                    print("\nSplit Array:\n", np.array_split(self._array, splits))
                except ValueError:
                    print("Invalid Splits Number.")
            elif choice == 3:
                break
            else:
                print("Invalid Choice.")

    def search_sort_filter(self):
        if not self._has_array(): return

        while True:
            print("\nChoose An Option:")
            print("1. Search A Value")
            print("2. Sort The Array")
            print("3. Filter Values")
            print("4. Go Back")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                val = float(input("Enter The Value To Search: "))
                indices = np.where(self._array == val)
                print(f"Value Found At Indices: {indices}")
            elif choice == 2:
                order = input("Sort In Ascending Order? (Yes/No): ").strip().lower()
                if order == 'no':
                    sorted_arr = np.sort(self._array)
                    print("\nSorted Array (Descending):\n", np.flip(sorted_arr, axis=-1))
                else:
                    print("\nSorted Array (Ascending):\n", np.sort(self._array))
                print("(Sorting Applied Row-Wise.)")
            elif choice == 3:
                val = float(input("Enter A Value To Filter Numbers Greater Than It: "))
                print(f"\nFiltered Array (Values > {val}):\n", self._array[self._array > val])
            elif choice == 4:
                break
            else:
                print("Invalid Choice.")

    def compute_stats(self):
        if not self._has_array(): return

        while True:
            print("\nChoose An Aggregate/Statistical Operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Go Back")
            choice = int(input("Enter Your Choice: "))

            print("\nOriginal Array:\n", self._array)
            if choice == 1:
                print(f"\nSum Of Array: {np.sum(self._array)}")
            elif choice == 2:
                print(f"\nMean Of Array: {np.mean(self._array)}")
            elif choice == 3:
                print(f"\nMedian Of Array: {np.median(self._array)}")
            elif choice == 4:
                print(f"\nStandard Deviation Of Array: {np.std(self._array)}")
            elif choice == 5:
                print(f"\nVariance Of Array: {np.var(self._array)}")
            elif choice == 6:
                break
            else:
                print("Invalid Choice.")


def main():
    analyzer = DataAnalytics()
    DataAnalytics.welcome_message()

    while True:
        print("\nChoose An Option:")
        print("1. Create A Numpy Array")
        print("2. Slicing & Indexing Options")
        print("3. Perform Mathematical Operations")
        print("4. Combine Or Split Arrays")
        print("5. Search, Sort, Or Filter Arrays")
        print("6. Compute Aggregates And Statistics")
        print("7. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.perform_indexing_slicing()
        elif choice == 3:
            analyzer.perform_math()
        elif choice == 4:
            analyzer.combine_split()
        elif choice == 5:
            analyzer.search_sort_filter()
        elif choice == 6:
            analyzer.compute_stats()
        elif choice == 7:
            print("\nThank You For Using The NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid Choice, Please Try Again.")

if __name__ == "__main__":
    main()