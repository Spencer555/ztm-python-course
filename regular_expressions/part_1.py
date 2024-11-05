import re

string = 'search inside of this text please!'


print('search' in string)


# search if this exist in the string
a = re.search('this', string)
# if it does not find anything it return snone


# this returns a match object and tell us the span it occurs start index to end index

print(a.span())
# tells you where the string occurs as a tuple


print(a.start())
# where the text start

print(a.end())
# where the text ends

print(a.group())
# return sthe part of the string where there was the match

# a pattern we want to check for
pattern = re.compile('this')


# using the pattern to do the search

b = pattern.search(string)
print(b.group())


# finds all the instances of the the term u are looking for
pattern.findall(string)


# the exact string we are searching not just a part of it
pattern.fullmatch(string)


# the if there is a match or the term we are searching for is contained in a string
pattern.match(string)

# just google or read docs u use as need arise you dont memorize it
