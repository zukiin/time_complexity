names = ["Zuki", "Andy", "Azz", "Thale", "Beast", "Lele"]

class BigO:
    def __init__(self, input):
        self.input = input
        
    # O(n): Linear time
    # The runtime is dependent on the input size. If input is 2, then this is O(2), if input is 16 it is O(16).
    # Best case: name_to_find is at index 0 = O(1), worst case: name_to_find is at index -1 = O(n)
    def find_user_name(self, user_name):
        for name in names:
            if name == user_name:
                return f"Found '{user_name} @ index {names.index(name)}"
            else:
                return f"'{user_name}' doesn't exist here"
            

name_to_find = input("Enter your name \n")
# ------------------------------------------------#
big_o = BigO(names)
result = big_o.find_user_name(name_to_find)
print(result)
print("End of linear time \n\n\n")