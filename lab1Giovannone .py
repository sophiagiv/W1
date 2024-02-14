
import random
#try 2 
class Pet:
    cleanliness_max = 10
    food_reduce = 2
    food_max= 10
    food_warning = 3
    boredom_reduce = 2
    boredom_max = 10
    sounds = ['Tomagotchi!', 'Grrr...']

    def __init__(self,name):
        self.name = name 
        self.hygiene = random.randrange(Pet.cleanliness_max)
        self.food = random.randrange(Pet.food_max,)
        self.boredom = random.randrange(Pet.boredom_max)
        self.sounds = Pet.sounds

    def bathe(self):
        if self.hygiene < Pet.cleanliness_max:
            self.hygiene += 3
            if self.hygiene >= Pet.cleanliness_max:
                print(f"the pat is annoyed given the unnecessary baths")
        else:
            print(f"the pat is annoyed given the unnecessary baths")

    def clock_tick(self):
        self.boredom += 1
        self.food -= 1 


    def greet(self):    
        choiceSound = random.choice(self.sounds)
        print(f"{choiceSound} is the sound the pet already knows randomly chosen from list.")

    
    
    def teach(self, new_word):
        self.sounds.append(new_word) 
        print(f"{self,new_word} let me teach my new pet a word")


    def feed(self):
        meal = random.randint(0, min(self.food, self.food_max))
        if self.food > self.food_max:
            self.food = self.food_max
        else:
            self.food = meal 
        print(f"{self.name}")

    def mood(self):
        if self.food >= self.food_warning and (0 <= self.boredom_reduce <= self.boredom_max):
            print("Happy")
        elif self.food < self.food_warning:
            print("Hungry")
        else: 
            print("Bored")


class Cat(Pet):
    sounds = ['Meow']
    
    def rat(self, chasing):
        if chasing == "yes":
            print(f"{self.name} is chasing the rat")
        

    def mood(self):
        if self.food >= self.food_warning and (0 < self.boredom < 2):
            print("Happy")
        elif self.boredom >=2:
            print("Hungry")
        else: 
            print("Bored")

 # The two edits that I made were two variables name get_treat and get_reward as integars 
 # for my pet turtle that will either deserves a treat or needs to be a better pet
 # from the overall class Pet and two from the class that i made  

class turtle(Pet):
    get_treat = 0 
    get_reward = 4 
   
    def treat(self):
        if self.cleanliness_max == 8:
            print(f"{self.name}  deserves a treat ")
        
        elif self.get_treat >= self.get_reward:
            print(f"{self.name}  gets that treat ")
        else:
            self.get_treat += 1
            self.cleanliness_max -= 1 
            print(f" needs to be a better pet ")
    
    def type_treat(self):
        if self.get_treat == 2:
            print(f"my turtle gets peanutbutter ")
        
        if self.get_treat == self.get_reward:
            print("my pet gets this peanutbutter and celery ")


pet_instance = Pet("Luna")
cat_instance = Cat("Baby")
turtle_instance = turtle("Fred")





pet_instance.bathe()
pet_instance.clock_tick()
pet_instance.greet()
pet_instance.teach("talk")
pet_instance.feed()
pet_instance.mood()

cat_instance.rat('Baby')
cat_instance.clock_tick()
cat_instance.greet()
cat_instance.rat("yes")

turtle_instance.treat()





    
