# debugging - fixing your code mistakes
'''
tips 
linting - using ide to show issues with code red underline, or yellow or any color it allows us to find these errors before we run the code 

ide/ editors - the show errors with highlighting auto formatting etc


read errors - learn to read errors to know where the issues is comming from and understand them

if u see an error u have never seen b4 go to the documentation and read about it 

then pdb - python debugger
'''

import pdb


def add(num1, num2):
    # this is lets us go thru the code step by step to see where the issue is from
    # print(num1, num2)
    pdb.set_trace()  # set trace is the most usefull pdb command
    # in the pdb shell step is used to step thru the code line by line
    # continue - lets you continue thru the code untill u return something
    # w shows us the context of the current line
    t = 4*5
    return num1 + num2


add(4, 'string')
