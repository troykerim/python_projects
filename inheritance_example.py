# Parent class
class Animal():
    # This code below would be boilerplate code we would have to rewrite if inheritance was not being used.
    alive = True 
    
    def eat(self):
        print("This animal is eating.")
    def sleep(self):
        print("This animal is sleeping.")
        
# Child class 
class Rabbit(Animal): 
    def run(self):
        print("This rabbit is running.")

# Child class 
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.") 

# Child class 
class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

print()

rabbit.run()
fish.swim()
hawk.fly()