# its better to use png when you dev websites 
'''
we want a python script that runs like this from the command line 
python_scriptname images\ new\

# open the images folder and create a new folder called new
it loops thru all the images in images folder and converts it to jpeg and put it in new folder
'''


from PIL import Image
import sys 
import os 


# uses sys.argv to grab first and second arguments 


first_arg = sys.argv[1]
second_arg = sys.argv[2]


# check if new exists or not create it

if not os.path.exists(os.path.join(os.getcwd(), 'new')):
    os.makedirs('new')


# loop thru the entire folder and convert images to png


folder_path = os.path.join(os.getcwd(), 'images')
for file in os.listdir(folder_path):
    temp = Image.open(f'{folder_path}\{file}')
    new_filename = file.replace('.jpg', '.png')
    temp.save(f'new\{new_filename}', "png")
    



# save them to the new folder
