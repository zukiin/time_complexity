from typing import List

names = ["Zuki", "Andy", "Azz", "Thale", "Beast", "Lele", "Martian", "Diko"]

class BigO:
    def __init__(self, input):
        self.input = input

    # O(n^2): Quadratic time
    # The easiest indicator is nested loops. If a single loop is O(n), 2 = O(n^2)
    # Basically, as the input size grows, the number of iterations/ operations grows quadratically. E.g., bubble sort & comparing elements
    # Exercise: Print all pairs of an array, don't print the duplicates.
    def print_pairs(self):
        for i in self.input:
            for j in self.input:
                if i == j:
                    pass
                else:
                    print(f"{i}-{j}")


    # Bubble sorting: the easiest but also not efficient sorting algorithm
    # Traverse a list comparing neighbor elements and swapping them if a > b
    def bubble_sort(self):
       names_list = self.input

       for i in range(len(names_list)):
           for j in range(len(names_list) - 1):
               if names_list[j] > names_list[j+1]:
                   names_list[j], names_list[j+1] = names_list[j+1], names_list[j]
       
       print(f"Sorted list: {names_list}")


    # Given 2 arrays, create a function that lets a user know whether the arrays contain any common elements
    # We return a Bool
    # The arrays can be sorted or unsorted. It doesn't matter. The time complexity is O(n^2).
    # The best case would be to find a common element at the first index of each while comparing.
    def check_for_common_elements(self, arr1, arr2) -> bool:
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i] == arr2[j]:
                    return True
        return False
    # Need to optimize this code. Can possibly be improved to O(n), but that's just time. What about space?


    # Exercise: find a pair of consecutive numbers in a given circular array 'arr' that equals a specified target
    # Assumptions: The array can grow in size. We return the numbers/ their indices if they exists, else an empty array
    # (cont.) We're looping. Since the array grows, we might not always know its size. Therefore, the other loop is a while.
    def number_pair_equal_to_target(self, arr1, target) -> List[int]:
        pair = []
        for i in range(len(arr1)-1):
            if arr1[i] + arr1[i + 1] == target:
                pair.append(i)
                pair.append(i + 1)    
        return pair



big_o = BigO(names)
# big_o.print_pairs()
# big_o.bubble_sort()

# array1 = ['z', 'e', 'b', 'r', 'a', 'i', 'a', 'n']
# array2 = ['l', 'i', 'o', 'n']
# result = big_o.check_for_common_elements(array1, array2)
# print(f"The result is {result}")

# Data set:
numbers = [1, 3, 4, 2, 5, 3]
target = 8 # Expected Result: [4,2]

print(f"Elements at indices {big_o.number_pair_equal_to_target(numbers, target)}")