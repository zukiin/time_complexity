names = ["Zuki", "Andy", "Azz", "Thale", "Beast", "Lele"]

class BigO:
    def __init__(self, input):
        self.input = input

    # O(1): Constant time. (example follows)
    # Runtime doesn't change no matter how big the input size grows because there's no iterations.
    # This is the best case, and probably cannot be optimized further than it is. Just clean your code.
    def print_user_name(self):
        print(f"Your name is {self.input}")

    # O(log n): Logarithmic
    # Typically reduces input size by half ("Logarithmically").
    # The number of operations you need to perform grows slowly.
    # Some problems can be optimized so they reach the best case, like Hash tables and arrays, not binary search.
    def binary_search(self, target):
        sorted_names = sorted(self.input) # Sort here because binary search works best with sorted lists
        lower, upper = 0, len(sorted_names) -1 # Sorted: names = ["Andy", "Azz", "Beast", "Lele", "Thale", "Zuki"]

        while lower <= upper:
            middle = (lower + upper) // 2
            mid_name = sorted_names[middle]

            if mid_name == target:
                return middle
            elif mid_name < target:
                lower = middle + 1
            else:
                upper = middle - 1

        return -1
    
name_to_find = input("Enter your name \n")
# ------------------------------------------------#
big_o = BigO(name_to_find)
big_o.print_user_name()

# ------------------------------------------------#
print("\n\n starting O(log n)")
big_o = BigO(names)
index = big_o.binary_search(name_to_find)

if index != -1:
    print(f"Found name '{name_to_find}' at position {index +1}") # Add 1 to index for natural numbers
else:
    print(f"'{name_to_find}' is not in the list.")
