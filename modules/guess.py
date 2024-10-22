# sys - import system module
'''
with sys u can use argv 
sys.argv allows you to get params passed in the terminal


they can be accessed by an index 

sys.argv[0] first item 
'''
import sys
import random 
# exercise
'''
create a guess game that allows you to set the start and end range 
and if u guess the num correct you will else you try again the values are passed thru the terminal 
'''


start_range = int(sys.argv[1])
end_range = int(sys.argv[2])



random_answer = random.randint(start_range, end_range)


while True:
    try:
        answer = int(input('Please choose a number that falls between these two'))

        if answer >= start_range and answer <= end_range:
                
            if random_answer == answer:
                print(f'you got the answer right {random_answer}')
                break
            
    except ValueError:
        print('Please enter a number')
        continue
