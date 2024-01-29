"""Classes_Objects"""

""" Python is object-oriented programming, same as C++, JAVA, e.g.,,
    - OOP is easy to be reused, saves computing storage
    - class is the blue print, and the objects are the realizations (instances) of the class
    - class defines the data attributes (variable) and procedures (methods) of the objects
"""
#DEMO EXAMPLE 
class Customer: # the name we created for this class 
    pass # creating an empty class w pass statmenet # the keyword, theres no actions here ; # if you dont put pass you will  get a syntax error 
cust_instance = Customer() #creating an instance from the customer class - this is directly calling the task, and encapsulized within
#^ difference between is the cust_ins line will ALWAYS be executed- could mess up follwoing lines; use below. line to not have so much control 
# to make an instance from the class, call the class and make an instance 

def cust_instance():
    cust = Customer() # instance_name = Customer() takes the instance from the customer. 
    return cust

cust_instance()


#Creating the Dog Class
class Dog: #Capitalized name for classes in Python
    
    def __init__(self, name, age): #Initializing name and age attributes for Dog.
        """ __init__ is an initializer method because it initializes the objects data; it is always executed when a class is created. 
        self parameter is REQUIRED as the first argument in each member method in the class. 
        self is a stand-in for object reference.
        """
        self.name = name  
        self.age = age
        self.treats = "Dental Chews" #set a default value for an attribute

    def sit(self): 
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over!")

    def update_treats(self, new_treat):
        self.treats = new_treat


def one_instance(): #Making an instance from a Class
    my_dog = Dog("Ollie", 4)  #self does not need an argument when it is called.
    print(f"My dog's name is {my_dog.name}")
    print(f"My dog's age is {my_dog.age}")
    """
    Notably, .treat doesn't exit in this instance, given update_treats() has not been called.
    """

def second_instance():
    dog_name = input("What's your dog's name?")
    dog_age = int(input("How old is your dog?"))
    your_dog = Dog(dog_name, dog_age)  
    your_dog.sit()
    your_dog.roll_over()

#To update an attribute's default value, either through a method or direct assignment
def third_instance():
    my_dog = Dog("Ollie", 4)
    my_dog.update_treats("Apple") #through a method
    print(f"{my_dog.name} loves {my_dog.treats}")

def fourth_instance():
    my_dog = Dog("ollie",4)
    my_dog.treats = "apple"
    print(f"{my_dog.name} loves {my_dog.treats}")

#fourth_instance()

""" Design Classes 
    - Class
    - Data Attributes - nouns
    - Methods - actions
    
In the Dog class case: 
    - Dog
    - Name, AGE
    - sit(), roll_over()
"""

# In-class exercises: 
"""
Make a class called Restaurant with two attributes, restaurant_name and cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information,
and another method called open_restaurant() that prints a message indicating that the 
restaurant is open.

Make 3 instances of the class, print two attributes individually and then call the two methods.
"""
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
    
    def describe(self):
        print(f"{self.restaurant_name} is a popular name in channelside.")
    
    def open_restaurant(self):
         print(f"{self.restaurant_name} is  open for business Monday through Saturday 8-4!")
    
def instance_one():
    restaurant_name = input("What is the name of the restaurant?")
    cuisine_type = input("What type of cuisine is this food:")
    restaurant_one = Restaurant(restaurant_name, cuisine_type)
    restaurant_one.describe()
    restaurant_one.open_restaurant()
    print(f"{restaurant_name} is the restaurant name and the type of food served is, {cuisine_type}")

instance_one()
