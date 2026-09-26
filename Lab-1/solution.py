# Task 1: FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Task 2: Movie Budgets
movies = [
    ("Movie A", 100),
    ("Movie B", 250),
    ("Movie C", 150),
    ("Movie D", 300),
    ("Movie E", 80)
]

total_budget = sum(budget for title, budget in movies)
avg_budget = total_budget / len(movies)

print(f"Average Budget: {avg_budget:.2f}\n")

exceeded_count = 0
for title, budget in movies:
    if budget > avg_budget:
        exceeded_amount = budget - avg_budget
        print(f"{title} exceeded average by {exceeded_amount:.2f}")
        exceeded_count += 1

print(f"\nTotal movies above average: {exceeded_count}")

# Task 3: OOP Vehicle
class Vehicle:
    def start_engine(self):
        print("Vehicle engine started.")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a roar!")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started with a vroom!")

# Instantiation & Testing
v = Vehicle()
c = Car()
m = Motorcycle()

v.start_engine()
c.start_engine()
m.start_engine()
