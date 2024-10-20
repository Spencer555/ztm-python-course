# genarators - it allows us to generate a sequence of values over time
# range is a genrator a generator allows us to use a special keyword yield that can pause and resume functions


# a list creates a giant list of a 100 items in memory but range does it one at a time

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
# 3 generators performance
# fix translator service
