class Cat:
    def __init__(self, name, species, age,home_location):
        self.name = name
        self.species = species
        self.age = age
        self.home_location = home_location

    def eat(self):
        print("I am eating")
       

    def sleep(self):
        print("I am sleeping")

    def hunt(self):
        print('Going to hunt')
    
    def introduction(self):
         print("Hi")
         print("My name is", self.name)
         print("My species is", self.species)
         print("I am " + self.age + " years old")
       
    
tiger=Cat ("billi","wild",20,"india")
tiger1= Cat("Jilli","wild",15,"Bhutan")
homepet= Cat("meow","domisticated",20,"Bhutan")
homepet1= Cat("meolw","domisticated",10,"Bhutan")

Cat_storage = [tiger,tiger1,homepet,homepet1]

for cat in Cat_storage:
    if cat.age> 18:
        print(cat.name, "can vote")
    
    else:
        print(cat.name,"cannot vote")
        
        
