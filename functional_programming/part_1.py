# functional programming is all about sepration of concerns which oop does as well its all about packaging our code into seprate chunks so everything is well organized in each part of our code and each part is organized in a way that makes sense seperation of concers means each part concerns it self with one thing thing that is good at we dont combine both data and functions like we did in oop

'''
aims of functiona programming 
clear and understandable 
easy to extend 
easy to maintain 
memory efficient - becasue we are not storing all over the place 
DRY
'''


# the main pillar of functional programming is pure functions - where there is sepration between data of a program and the behavior of a program

# a pure function has two rules
# 1 given the same input it always returns the same output
# 2 a function should not produce side effects(things a function does that affect the outside world e.g print() or getting a variable outside the function)


# pure functions make your code less buggy and makes your life easier as a programmer it is more of a guide line not a strict path and impossible to have it everywhere but when u can use it

from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


# functions that allow us to think in a functional programming paradigm

# map, filter, zip and reduce


# map - takes a function and an iterable the data you want to work on
# to use with map function takes input and does something to it and return it
# map, filter, zip and reduce return a new list
def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1, 2, 3, 4, 5])))

# to view it we need to turn it into a list


# filter - to filter something out of a list

def filter_even(item):
    return item % 2 == 0


print(list(filter(filter_even, [1, 2, 3, 4, 5])))


# zip is to zip two things together
# and you gives it two or more lists and it returns a tuple of each pair in a list

my_list = [1, 2, 3, 4]
your_list = 10, 20, 30, 40

print(list(zip(my_list, your_list)))


# reduce - it takes a function and a sequence and works on it to return a single result

# reduce(accumulator, item, initial_value)
# if we dont give it anything the accumulator defaults to 0

rmy_list = [1, 2, 3, 4]
ryour_list = 10, 20, 30, 40


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, ryour_list, 0))


# exercise


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_word(item):
    return item.capitalize()


print('maps', list(map(capitalize_word, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()


print('zip', list(zip(my_numbers, my_strings)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_by_50(item):
    return item > 50


print('filter', list(filter(filter_by_50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

my_numbers.extend(scores)
print(my_numbers)


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers, 0))


# exercise
# use list comprehension to get duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


our_dict = {num: num*2 for num in [1, 2, 3]}

# duplicates = [item for item in some_list if item.count(item) > 1]
duplicates = list({item for item in some_list if some_list.count(item) > 1})

# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)


print(duplicates)
