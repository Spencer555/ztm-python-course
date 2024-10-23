import pyjokes 

joke = pyjokes.get_joke('en', 'neutral')

print(joke)

# virtual env - allow us to create a space to install packages for each projects on the same pc 

'''
usefull built in python modules

if u see anything beginning with capital its a class
'''

from collections import Counter, defaultdict, OrderedDict


li = [1,2,3,4,5,6,7]
# create a dictionary of the items and the num of times they appear
print(Counter(li))

sentence =  'blah blah blah thinking about python'
# we see which letter and num of occurance
print(Counter(sentence))


# default dict 

dictionary = {'a':1, 'b':2}

print(dictionary['c'])