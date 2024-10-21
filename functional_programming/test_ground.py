
# lambda expressions

# lambda expressions in python are one thime anonymous function that you dont need more than once


# lambda param: action_to_take_on_param(param)

def multiply_by2(item):
    return item*2

# using lambda as multiply_by2

print(list(map(lambda item: item*2, [1, 2, 3, 4, 5])))




results = lambda item : item *3

print(results(2))


# lambda with reduce
from functools import reduce

ryour_list = 10, 20, 30, 40


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(lambda acc, item: acc + item , ryour_list, 0))


# lambda makes code really small but less readable and confusing to people

# exercise 
# create a lambda that squares your list 1,2,3 returns 1,4,9

my_list = [5,4,3]


print(list(map(lambda item : item**2 ,my_list)))


# exercise 2
# list sorting  sort this based on second value
a = [(0,2), (4,3), (9,9), (10,-1)]


a.sort(key=lambda key: key[1])

print(a)