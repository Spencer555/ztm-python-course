# object oriented programming everything in python is an object
# it is a paradgim - its a way for us to think about our code and structure it in a way its easier to maintain extend and write
#

# so if we are writing a drone delivery program we might write it in bits and pieces little obj that represent the real world e.g propellers, camera, flight path  etc

'''
before oop we wrote procedual code 
we were telling the machine to do what we wanted loops , if statements etc 

but with oop 
we were able to model real world object e.g if we were to code a car we can create for engine, etc and think in terms of real world models 


the blue print is what we call a class and this class can be instantiated meaning creating instance of that class or a new object 
'''

# use capitalized and CamelCase and the name should be singular not plural


class BigObject:  # Class
    pass
# the class is stored in memory
# the objects reference it


obj1 = BigObject()  # instantiate the class

print(type(obj1))  # we get class BigObject


# wizard game

class PlayerCharacter:

    # this is a class object attribute this is static not dynamic and all objects have access to it and it cant be modified and does not change accross instances
    membership = True

    # methods dunder or magic method
    # self refers to the class itself
    def __init__(self, name='anonymous', age=0):

        if age > 18:
            # it can be accessed as self.membership or PlayerCharacter.membership to access the class object attribute
            print(PlayerCharacter.membership)

            # init is a construtor method and this is called automatically anytime we instantiate a class
            self.name = name  # attribues
            # attributes are pieces of data that are dynamic so if we instantiate an object the attributes are unique to the object
            self.age = age

    def run(self):
        return (f'{self.name} is running')

    def shout(self, hello):
        return (f'{hello} is running')

    @classmethod
    # this is a class method so it can be used without instantiating
    # there are not used as often about 95% of the time but it can be used to instantiate an object over here
    # we use staticmethod were we care about class state or attributes
    def adding_things(cls, num1, num2):
        return num1 + num2
    # using it to instantiate an object so name is teddy age is sum of numbers
        # return cls('Teddy', num1 + num2)

    @staticmethod
    # it works the same way as classmethod but does have access to cls
    # we use staticmethod were we dont care about class state or attributes
    def adding_things(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('spencer')

# to add a property to player 1
player1.attack = 'kill mode activated'

print(player1.attack)

print(player1.run())

print(player1.shout('loud music'))


# to get the blueprint of the object
# print(help(player1))


# can be called without instantiating class
print(PlayerCharacter.adding_things(2, 3))


# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat('Mimi', 12)
cat_2 = Cat('Titi', 10)
cat_3 = Cat('Kiki', 9)


# 2 Create a function that finds the oldest cat

def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f'Oldest Cat is {oldest_cat(cat_1.age, cat_2.age, cat_3.age)} years old.')
