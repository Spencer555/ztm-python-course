# modules - each .py file is a module
from utility import divide, multiply
from shopping.shopping_cart import buy
# pychache is generated anytime we run a file with import statements it caches anything we import and saved as .pyc the python c interpreter so nextime we run it it loads the compiled version .pyc instead of the otherfile making things faster
# print(divide(10,2))


# a package is a level up a package is a folder containing modules 
# __init__.py shows the folder is a package
# in programming when something exits with code 0 it means everything worked successfully with no errors
# print(buy('bread'))


# when the file from the actual file the __name__ = __main__
# the name __main__ is given to the file we run
# so if u see that line it means we want to run the module only when it is being run from the main file

# __name__ or __main__


'''
the reason why python is soo popular is because of developers keep sharing code as modules so we dont keep reinventing the wheel
'''

if __name__ == '__main__':
    print(divide(25, 5))
    print(multiply(5, 5))
    print(buy('egg'))



# python package index or pypi 
# check if something exist in built in module before u use pypi 


'''
u can read on project who is worked on it what lincese it has and how recent it has been worked on 

e.g we want to work with csv 

we go to google python csv built in 
'''
