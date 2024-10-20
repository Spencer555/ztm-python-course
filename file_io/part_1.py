# file io file input output


my_file = open('test.txt')

# u can only read the file once it has and idea of a cursor once you open it returns a file object and the content of a file you can read by the end of the first read the cursor is at the end of the file so when you try to read you get nothing to get around it we do my_file.seek to move it back to the index we want
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)


# read lines - read line by line
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())


# readlines - read all lines
print(my_file.readlines())


# close the file you have opened but when using with u can skip it
my_file.close()


# a easier and better way to deal with files

print('easier way')
# default mode is r - read
# a - append - this appends to the end of the file
# w - write - when we write something to a file the cursor resets so if there is something there already existing we reset it, also it create the file if it does not exist
# r+ - read and write
with open('test.txt', mode='w') as file:
    file.write(
        'this is the life words rhyme the best but i cant spell well so i define success i sell well')


# file paths
'''

'''

with open('./app/sad.txt') as file:

    print(file.read())


# pathlib
# new inbuilt from python to help read files and works on all os u can read on your own and experiment


# one of the common patterns of working with file is to put them in a try catch block

try:
    with open('read.txt', mode='r') as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('machine has issues reading or writing or doing any operation')
    raise err
except FileNotFoundError as err:
    print('file does not exist')
    raise err
