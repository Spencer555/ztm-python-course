# decorators
'''
@name the look like this 
in python functions are first class citizens meaning the can be passed around like variables, and can be passed as arguments to functions 
'''


from time import time


def hello():
    print('hellooooo')


# if we delete hello  we can still call greet because it still pointing to the function  so we delete hello but we dont delete the entire function because greet is pointing to it
greet = hello

del hello
print(greet())


# We can pass functions as variables

def meet(greet):
    greet()
    print('nice to meet your')


meet(greet)


# decorators are only possible because of these abilites of functions to act like first class citizens underneath the hood they are using this

# decorators supercharge our function  a function that wraps another function and enhances it


# higher order function  or HOC - a function that accepts another function or a function that returns another function if it does any of these its a higher order function
def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func()


# a decorator
# as long as the the function accepts a function, having a wraper function calling the function and returing the wrapper function its a decorator
# can be used for logging and authentications


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("***********")
        func(*args, **kwargs)
        print("***********")

    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)
    print('helloooo')


hello('fdf')


# underneath the hood all decorator is doing is
# taking the function as and argument and assigning it to a variable and calling that variable
# a = my_decorator(hello)
# a()

# practical applications of decorators


def perfomance(func):
    def wrapper(*args, **kwargs):

        initial_time = time()
        result = func(*args, **kwargs)
        final_time = time()
        print(f'it took {final_time - initial_time} ms')
        return result
    return wrapper


@perfomance
def long_time():
    for i in range(100000):
        i*5


long_time()


# exercise

# create an @authenticated decorator that only allows the function to run is user1 has valid set True:

user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        return print('Not allowed to run function')

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
