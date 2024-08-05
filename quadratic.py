names = ["Zuki", "Andy", "Azz", "Thale", "Beast", "Lele", "Martian", "Diko"]

class BigO:
    def __init__(self, input):
        self.input = input

    # O(n^2): Quadratic time
    # The easiest indicator is nested loops. If a single loop is O(n), 2 = O(n^2)
    # Basically as the input size grows, the number of iterations/ operations grows quadratically. E.g., bubble sort
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

big_o = BigO(names)
# big_o.print_pairs()

big_o.bubble_sort()