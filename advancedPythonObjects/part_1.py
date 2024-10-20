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


from typing import Any


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


'''
always test your assumptions know how things are working so u can explain it to people
e.g we learnt about self 
is that what you expected then if there is a mismatch we probe further
'''

# def run(self): add this to a class to know about self
#     return self


# encapsulation - its the binding of data and functions that manipulates that data into one object so that we keep everything in this box so that users or code or other machine can interact with them

# e.g. we have functions that act on our class and also the class constains data  giving us more control and functionality and allow us mimic real world


# abstraction
# hiding info and giving access to only what is necessary
# e.g info that the user or machine is interested in everything else we hide
# e.g player1.run() #we dont see how it working we only get the results we dont get access to everything the same is for built in function

len('fdfsf')  # we dont need to know how the len works intenally all we need to know is it returns the length of the parameter given to it


# publiv vs private vars
class PlayerChar:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and i am {self.age} years old')


# the idea of of abstraction is we hide info and give access to info that is only needed so ideally we should not have access to init and methods this is where a private variable comes in but in python there is not true private variable so we use underscore a convention to tell other programmers not to change it because its a private variable self._age instead of self.age
# secondly dont write your own dunder method __ a double underscore variable because if u are doing that you are doing something wrong and going to overwrite something it's also a convention to let people know you should not touch this or midify it

# so if we try to override using
player1 = PlayerChar('andrei', 100)

player1.name = 'spencer'  # it still does not affect the main code


# inheritance passing values of one class to the other parent to  hild
# we have users and thier subclasses
# users
# wizards
# archers


class User:

    #  if we dont have any variables or attribute we want to assign to the user the init is not important
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        User.attack(self)  # to include parent attack method
        print(f'attacking with arrows of arrows left :{self.num_arrows}')


wizard1 = Wizard('Merlin ', 50)
archer1 = Archer('Robin', 30)

# now the wizard and archer have the sign in and the attack unique to thier individual classes
print(wizard1.attack())
print(archer1.attack())


# to check if something is an instance of a class
# isinstance(instance, Class)
print(isinstance(wizard1, Wizard))  # true
# wizard1 is an instance of user too because its inheriting from it
print(isinstance(wizard1, User))  # true


# everything in python inherits from the base object clase in python so anythings checked against it as an instance returs true

# so underneath the hood out
# class User is class User(object):
print(isinstance(wizard1, object))


# polymorphisim - poly means many and morphism means form so polymorphism refers to many forms

# methods belongs to object and we use the self keyword to act on object that got instantiated and pythons idea or polymorphisim refers to the way object classes can share the same method name but those method names can act differently based on what object calls them

# e.g attack is shared between user and archer but they both have different effects even though the share the same method names

# even with one function when we call both of them we still get different results  this is a demonstration of polymorphism  and even if the user class has an attack method the one in the subclass overrites it but if u want to use the parent class User attack method
# User.attack(self)
def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

# or
for char in [wizard1, archer1]:
    char.attack()


'''
the four pillars of oop 
encapsulation
abstraction
inheritance 
polymorphism

all u need to know is these exist u dont implement them its just like you are coding and u realise you are coding that way using these concepts
'''


# excercises
class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat(Pets):
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat


class Milly(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
simon = Cat('Simon', 10)
sally = Cat('Sally', 4)
milly = Cat('Milly', 5)

my_cats.append(simon)
my_cats.append(sally)
my_cats.append(milly)

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)


# 4 Output all of the cats walking using the my_pets instance

my_pets.walk()


# super used to pass values from parent to child

class User:
    def __init__(self, email):
        self.email

    #  if we dont have any variables or attribute we want to assign to the user the init is not important
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        # calling the init of the user from here
        # this one way and another way is super
        # User.__init__(self, email)
        # we pass the parent variables to it
        super().__init__(email)

        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.email} attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        User.attack(self)  # to include parent attack method
        print(f'attacking with arrows of arrows left :{self.num_arrows}')


# introspection - the ability to determine the type of object at runtime(when the code is running) this lets us know what the code is doing
# e.g dir gives you all the methods and attributes of the wizard1
print(dir(wizard1))


# dunder methods -it allows us to modify our classes and understand how python built in functions and methods work
# len and most other inbuild functions are implemented using dunder methods they allow us to use python specific functions on objecs created through our class

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dict = {
            'name': 'spencer',
            'has_pets': False
        }

    # to modify what the str does use this in only special cases when you want your class to behave a specific way this editing works only in the object it does not affect things outside the object

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):  # delete
        print('deleted')

    def __call__(self):  # u can now call the actual object e.g action_figure() u just add bracket to the instance
        print('yess??')

    def __getitem__(self, i):
        return self.dict[i]

    def __bool__(self):
        return True

    def __dir__(self):
        return (dir(Toy))

    def __type__(self):
        return type(self)

    # exercise- by reading python documentation add 3 more dunder method of your chosing to this class


action_figure = Toy('red', 0)

print(action_figure.__str__())  # this is the same as str(action_figure)


print(action_figure())
print(action_figure['name'])
print(action_figure.__bool__())
print(action_figure.__dir__())
print(action_figure.__type__())

# exercise - create a super list using class SuperList

# add code that allows us to access through index etc just like python


class SuperList(list):

    def __len__(self):
        return 1000

    def __call__(self):
        return self


super_list1 = SuperList()

print(len(super_list1))

for i in range(20):
    super_list1.append(i)


print(super_list1())
print(super_list1[0])


# to check if superlist is subclass of list
print(issubclass(SuperList, list))


# multiple inheritance
class MyUser:
    def sign_in(self):
        print('logged in user')


class TheWizard(MyUser):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class TheArcher(MyUser):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def arrow(self):
        print(f'attacking with arrow of {self.arrows} arrows left')

    def run(self):
        print('run really fast')

# multiple inheritance
# it can get complicated real fast try not to use it ofter


class HybridBorg(TheWizard, TheArcher):

    def __init__(self, name, power, arrows):
        # we have to pass the variables of each class too to avoid errors
        TheArcher.__init__(self, name, arrows)
        TheWizard.__init__(self, name, power)


hybridBorg1 = HybridBorg('spencer', 10000, 29)

print(hybridBorg1.sign_in())
print(hybridBorg1.arrow())
print(hybridBorg1.attack())

# MRO - Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


#     A
#    /  \
#   /    \
#   B     C
#   \     /
#    \   /
#      D

'''
D inherits from B and C 
and B and C inherits from A


mro is a rule which python follows to determine when you run a method which one should be run when you have such complicated  inheritance structure
'''

print(D.num)

print(D.mro())  # to see the mro of the class

# we get one because it goes D B C A


# showing how complicate mro can get
# guess what the mro would be

# you are never goinh to get tested on this but if u are writing code that the inheritance look like this you are writing bad code
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print('\n')
print(M.__mro__)
