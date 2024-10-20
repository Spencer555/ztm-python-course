# an error that crashes our program is called an exception
# error handling is handling exceptions that crash our program

'''
types of error in python 
type error
syntax error
name
there are alot refer to documentation
'''

# without the semicolon its a syntax error


def hooo():
    # 1 + name #name error
    return 1


def hoooo(num):

    while True:

        try:
            age = int(input('pls enter your age: '))
            print(age)
            10/age
        except ZeroDivisionError:
            print('please enter a valid number that not zero')

        except ValueError:
            print('please enter a valid number')

        else:
            print('thank you')
            break
        finally:
            print('this runs no matter the outcome')


hoooo('fdsf')


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        # or u can use multiple erros
        # except (TypeError , ZeroDivisionError) as err:
        return print(f'pls enter numbers {err}')


print(sum('1', 2))

# sometimes  errors are so severe we want to stop our code when the appear in this case we use raise keyword
# raise name_of_err
# e.g raise ValueError
# errors are unavoidable in coding what your job is as aprogrammer is to anticipate and handle them
