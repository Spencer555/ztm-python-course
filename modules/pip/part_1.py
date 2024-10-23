from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')

print(joke)

# virtual env - allow us to create a space to install packages for each projects on the same pc

'''
usefull built in python modules

if u see anything beginning with capital its a class
'''


li = [1, 2, 3, 4, 5, 6, 7]
# create a dictionary of the items and the num of times they appear
print(Counter(li))

sentence = 'blah blah blah thinking about python'
# we see which letter and num of occurance
print(Counter(sentence))


# default dict

dictionary = {'a': 1, 'b': 2}

print(dictionary['c'])


dictionary = {'a': 1, 'b': 2}

# with default dict it does not throw error when key does not exist
# so if we search for something that does not exist we get 5 because the lambda retuns 5
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
dictionary_1 = defaultdict(
    lambda: 'default it does not exist', {'a': 1, 'b': 2})

print(dictionary['v'])


# ordered dictionary allows you to store things the way you inserted them
d1 = OrderedDict()

d1['a'] = 1
d1['b'] = 2


d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

# it returns true but if we change the order we get false
print(d1 == d2)


# datetime module
# to create time objects
print(datetime.time(5, 45, 2))

print(datetime.date.today())


# array package


# list in python  are sometimes called array but they are a little bit dynamic

# arrays take up less memory and perform a bit faster

# array(datatype_it_would_hold, data)
arr = array('i', [1, 2, 3])

print(arr)


# pros and cons of packages
# develop the skill to see that this package is really popular, this package is being maintained, this package or this has many stars or popular within the development comm so its a good library
# because it makes your product heavy
# before you import a library ask yourself could i just write this my self except it would be time consuming you dont have the expertise in ther area most of the time when working as a dev you are matching and pulling in diff libraries and making them work together alot of your work would involve reading this libraries reading docs b
