# built in module you dont need to know everything you can google them

import random 

print(random.random()) # generate random num bet 0 and 1
print(random.randint(1,10)) #generate random num 1 and 10 
print(random.choice([1,2,3,4,5])) #chose a random num from the array

my_list = [1,2,3,4,5]
random.shuffle(my_list) #shuffle list in place
print(my_list)


# sys - import system module 
'''
with sys u can use argv 
sys.argv allows you to get params passed in the terminal


they can be accessed by an index 

sys.argv[0] first item 
'''
import sys 


first = sys.argv[1]
last = sys.argv[2]

print(f'hiiii! {first} {last}')


