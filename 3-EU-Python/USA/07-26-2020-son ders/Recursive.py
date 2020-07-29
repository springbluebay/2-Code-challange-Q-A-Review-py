import os

# Sum of a list

# def sumNums(nums):
#     total=0
#     for i in nums:
#         total+=i
#     return total
# print(sumNums(lst))

lst = [1,5,3,6,4,3,9,7]
def sum_recursive(nums):
    if len(nums) == 0:
        return 0

    last_num = nums.pop()
    return last_num + sum_recursive(nums)
# print(sum_recursive(lst))








# Factorial Numbers
# 5! = 5 x 4 x 3 x 2 x 1 = 120

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))












# Fibonacci Sequence
# Integers:   0, 1, 2, 3, 4, 5, 6, 7
# Fibonacci:  0, 1, 1, 2, 3, 5, 8, 13


def fibonacci(n):
    if n == 0 or n==1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

clear = lambda : os.system("clear")

clear()

lst_2 = list(range(10))
for i in range(10):
    print(fibonacci(i),end=" ")
print()