import random 
# Vampire class that stores a list of vampires(coven)
class Vampire:
    ''' Every day at sunset the vampire leaves the coffin to search for blood 
    if they dont drink blood and get back to their coffins before sunrise they die 
    ''' 
    coven = []
    vampire_names = ['Dracula', 'Abel', 'Damien', 'Darkness']
    in_coffin = False
    drank_blood_today = False 

    def __init__(self):
        '''Every vampire has a name, age, an in_coffin boolean, and a drank_blood_today boolean. 
        Also creates a new vampire '''
        random.seed(3)
        self.name = random.choice(self.vampire_names)
        random.seed(3)
        self.age = random.randint(66, 466)
        # self.in_coffin = False
        # self.drank_blood_today = False 
    
    def __str__(self): 
        return f''' Name: {self.name}\n Age: {self.age}\n In Coffin: {self.in_coffin}\n Drank Blood today: {self.drank_blood_today}\n '''
    
    def drink_blood(self): 
        ''' sets vampire drank_blood_today boolean to true '''
        self.drank_blood_today = True 
        
        
    @classmethod
    def show_coven(cls): 
        full_coven = [] 
        for item in Vampire.coven:
            full_coven.append(item)
             # show each item in coven 
        return len(full_coven)
        # cls.coven = coven
    # @classmethod
    # def sunset(cls):
    #     for vampire in cls.coven:
    #         vampire.in_coffin = False
    #         vampire.drank_blood_today = False
    @classmethod
    def sunset(cls): 
        '''# sets drank_blood_today and in_coffin to false 
        for all the vampires in the coven''' 
        for vampire in cls.coven: 
            vampire.drank_blood_today = False 
            vampire.in_coffin = False 


    # def sunrise(self): 
    #     if self.drank_blood_today: 
    #         Vampire.coven.pop(self.coven.index(Vampire))
    @classmethod 
    def sunrise(cls): 
        ''' removes vampires from coven if they havent drank blood '''
        new_coven = [] 
        for vampire in cls.coven: 
            if vampire.drank_blood_today and vampire.in_coffin == False:  
                new_coven.append(vampire) 
        cls.coven = new_coven 

  
    @classmethod
    def print_coven(cls): 
        return f'{cls.coven}'

    @classmethod
    def create(cls): 
        ''' This will create a new Vampire ''' 
        # cls.name = random.choice(cls.vampire_names)
        # cls.age = random.randint(66, 466)
        new_vampire = Vampire() 
        cls.coven.append(new_vampire) 
        return new_vampire

    @classmethod 
    def go_home(cls): 
        cls.in_coffin = True 


# drink_blood  
# sets vampire drank_blood_today boolean to true 



# sunset @classmethod 
# sets drank_blood_today and in_coffin to false for all the vampires in the coven 

# go_home 
# sets a vampires in_coffin boolean to true 
vampire1 = Vampire.create() 
vampire2 = Vampire.create() 

# print(Vampire.coven) # show vampires in initial coven 
# print(vampire1) # show vampire 

# Vampire.show_coven()
vampire1.drink_blood() # make vampire 1 drink blood 
# print(Vampire.coven) # show new coven 

# for item in Vampire.coven: # show each item in coven 
#     print(item) 

print(Vampire.show_coven())
Vampire.sunset() 
vampire1.drink_blood()
vampire1.go_home() 
Vampire.sunrise() 

print(Vampire.show_coven())

# vampire1.go_home() 

# vampire2.drink_blood()
# # vampire1.new_day() 
# # vampire1.go_home() 
# # Vampire.sunrise()
# print(vampire1)
# print(vampire2)
# # Vampire.sunset() 
# Vampire.sunrise()
# vampire2.drink_blood() 
# print(vampire1)
# print(vampire2)
# print(Vampire.coven)


# Vampire.create() 
# Vampire.sunset()
# vampire1.drink_blood() 
# vampire3.go_home() 
# vampire2.drink_blood()
# Vampire.sunrise() 
# print(vampire1)
# print(vampire2)
# print(vampire3)


