class Car:
    def __init__(self, make, model, year, color):
        self.make = make 
        self.model = model
        self.year = year 
        self.color = color 
        
    def drive(self):
        print("This car is driving.")
    def stop(self):
        print("This car is stopped.")
        
make = input("Enter the car make: ")
model = input("Enter the car model: ")
year = input("Enter the car year: ")
color = input("Enter the car color: ")


user_car = Car(make, model, year, color)

print(f"\nYour car is a {user_car.year} {user_car.color} {user_car.make} {user_car.model}.")

# Testing methods
user_car.drive()
user_car.stop()