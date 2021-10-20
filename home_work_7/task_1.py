from random import randint


class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self, nums):
        s = ""
        for i in range(len(self.nums)):
            for a in range(len(self.nums[i])):
                s += f'{self.nums[i][a]:02}'
            s += "\n"
        return s

    def __add__(self, other):
        nums = [
            [self.nums[i][a] + other.nums[i][a] for a in range(len(self.nums[i]))]

                 for i in range(len(self.nums))]
        return Matrix(nums)

a = Matrix([[randint(0, 50) for _ in range(10)] for _in range(10)])
b = Matrix([[randint(0, 50) for _ in range(10)] for _in range(10)])
print(a)
print(b)
print(a + b)



