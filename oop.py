class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def bark(self):
        print('Woof woof')
    
    def sleep(self):
        print('Zzzzzz')
    
    def eat(self):
        print('i am eating')


dog = Dog('bhutanese', 20, 'black')
petdog = Dog('pug', 10, 'white')
my_friend_dog = Dog('german shephard', 15, 'brown')

dog.say_age()
petdog.say_age()
my_friend_dog.say_age()



#task
