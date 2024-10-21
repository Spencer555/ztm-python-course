# genarators - it allows us to generate a sequence of values over time
# range is a genrator a generator allows us to use a special keyword yield that can pause and resume functions


# a list creates a giant list of a 100 items in memory but range does it one at a time


from functools import reduce
from time import time
range(100)
list(range(100))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)

#     return result


# my_list = make_list(100)  # so this is taking up space

# but with range it does not create a giant list it gives you one value at a time so in memory it only holds one item without taking space in memeory
# iterable - any object we can loop thru __iter__
# iterate - is the act of taking an item from an iterable doing something to it then going to the next one

# and generators are iterable but not everything thats iterable are generators  a range is generator so its iterable and a list is an iterable but not a generator

# print(my_list)


def perfomance(func):
    def wrapper(*args, **kwargs):

        initial_time = time()
        result = func(*args, **kwargs)
        final_time = time()
        print(f'it took {final_time - initial_time} ms')
        return result
    return wrapper


# creating our own generator - we use yield
# yield pauses the function and comes back to it wen we do something to it called next
def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(1000):
    print(item)


g = generator_function(100)

next(g)
next(g)
print(next(g))


@perfomance
def long_time():
    print('1')
    for i in range(10000000):
        i*5


@perfomance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5


long_time()
long_time2()


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([1, 2, 3])


# mimic what a range does
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        # create an iterable
        return self

    def __next__(self):
        # to be able to call next on it like a range
        # we increase our current location by one and we return the num
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        # we raise a stop iteration if there is no more things to iterate over
        # if the current is greater than the self.last
        raise StopIteration


gen = MyGen(0, 100)

for i in gen:
    print(i)


# exercise - fibonacci number - possible interview
# first num is 0 second num is 1 then we add 0 + 1 to get 1 the third num then 1 + 1 to get the fourth num this grow exponentially

# so we are going to create a function fib that takes a num and this number is the index number of the fibonacii

# e.g. 20 so return all numbers to you get to the 20th fib
# so we set f1 to f2 and f3 to f2 in the iteration
def fib(num):
    f1 = 0
    f2 = 1

    for i in range(num):
        yield f1
        temp = f1
        f1 = f2
        f2 = temp + f2


for i in fib(20):
    print(i)


# with a list
def fib2(num):
    my_fib = []
    f1 = 0
    f2 = 1

    for i in range(num):
        my_fib.append(f1)
        temp = f1
        f1 = f2
        f2 = temp + f2

    return my_fib


print(fib2(20))


# lambda expressions

# lambda expressions in python are one thime anonymous function that you dont need more than once


# lambda param: action_to_take_on_param(param)


def multiply_by2(item):
    return item*2

# using lambda as multiply_by2


print(list(map(lambda item: item*2, [1, 2, 3, 4, 5])))


def results(item): return item * 3


print(results(2))


# lambda with reduce

ryour_list = 10, 20, 30, 40


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(lambda acc, item: acc + item, ryour_list, 0))


# lambda makes code really small but less readable and confusing to people

# exercise
# create a lambda that squares your list 1,2,3 returns 1,4,9

my_list = [5, 4, 3]


print(list(map(lambda item: item**2, my_list)))


# exercise 2
# list sorting  sort this based on second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]


a.sort(key=lambda key: key[1])

print(a)


# comprehensions
# list, set, dictionary
# a quick way to create the above instead of looping or appending

my_list = []

for char in 'hello':
    my_list.append(char)


print(my_list)


# list comprehension

# my_list = [param for param in iterable]

my_list1 = [char for char in 'hello']


my_list1 = [char ** 2 for char in range(100)]

# print(my_list1)


# generate only even numbers after squaring the numbers
my_list1 = [char ** 2 for char in range(100) if char % 2 == 0 and char > 0]
print(my_list1)


# they can get confusing and complicate code readability so it might be better to create a descriptive function

# with sets comprehension
# we change [] to {}


my_list2 = {char for char in 'hello'}
print(my_list2)


my_list2 = {char ** 2 for char in range(100)}
print(my_list2)


# generate only even numbers after squaring the numbers
my_list2 = {char ** 2 for char in range(100) if char % 2 == 0 and char > 0}

print(my_list2)


# dictionary
# with sets comprehension
# we change [] to {}

simple_dict = {'a': 1, 'b': 2}
# my_dict = {key:value**2 for key,value in simple_dict.items()}
my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}
print(my_dict)

# exercise item should be the key and item multiplied by 2 is the value
our_dict = {num: num*2 for num in [1, 2, 3]}

print(our_dict)
