import random


class RandomizedSet:

    def __init__(self):
        # List stores the actual values
        self.nums = []

        # Dictionary stores:
        # value -> index in the list
        self.index_map = {}

    def insert(self, val: int) -> bool:

        # If value already exists
        if val in self.index_map:
            return False

        # Add value to the end of the list
        self.nums.append(val)

        # Store its index
        self.index_map[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:

        # If value does not exist
        if val not in self.index_map:
            return False

        # Get index of the value we want to remove
        remove_index = self.index_map[val]

        # Get the last element
        last_value = self.nums[-1]

        # Move last element to the position of
        # the element we want to remove
        self.nums[remove_index] = last_value

        # Update the index of the last element
        self.index_map[last_value] = remove_index

        # Remove the last element
        self.nums.pop()

        # Remove the value from dictionary
        del self.index_map[val]

        return True

    def getRandom(self) -> int:

        # Return a random element
        return random.choice(self.nums)


# -----------------------------------
# INPUT / TEST
# -----------------------------------

mySet = RandomizedSet()

print(mySet.insert(1))       # True

print(mySet.remove(2))       # False

print(mySet.insert(2))       # True

print(mySet.getRandom())     # 1 or 2

print(mySet.remove(1))       # True

print(mySet.insert(2))       # False

print(mySet.getRandom())     # 2