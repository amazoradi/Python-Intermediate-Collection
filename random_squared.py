import random

# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.


random_num = [random.randrange(0, 49, 1) for rand in range(20)]

print(random_num)


sq_nums = [num**2 for num in random_num]

print("square", sq_nums)









# print(random_numbers)# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].