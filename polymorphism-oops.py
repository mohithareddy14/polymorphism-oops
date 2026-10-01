#Q1. Animal Sound (Method Overriding) Create a parent class Animal with a method sound(). Create child classes Dog, Cat, and Cow that override the sound() method. 
class Animal:
    def sound(self):
        print(" Animals makes a sound")
class Dog(Animal):
    def sound(self):
        print("Bow Bow...")
class Cat(Animal):
    def sound(self):
        print("meow..meow...")
class Cow(Animal):
    def sound(self):
        print("moos...moos")

Animal_method = [Animal(),Dog(),Cat(),Cow()]
for i in Animal_method:
    i.sound()

#Create a parent class Payment with a method pay(). Create child classes UPI, CreditCard, and Cash. Each class should implement its own pay() method. 
class payment:
    def pay(self):
        print("payment process")
class UPI(payment):
    def pay(self):
        print("payment through UPI")
class Creditcard(payment):
    def pay(self):
        print("payment through Credit card...")
class Cash(payment):
    def pay(self):
        print("payment through Cash....")
def payment_process(amount):
    amount.pay()
a=payment()
b=UPI()
c=Creditcard()
d=Cash()
payment_process(a)
payment_process(b)
payment_process(c)
payment_process(d)

#Create a parent class Employee with a method calculate_salary(). Create child classes FullTimeEmployee and PartTimeEmployee. 
class Employee:

    def calculate_salary(self):
        print("Salary calculation")


class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print("Full-Time Salary:", self.monthly_salary)


class PartTimeEmployee(Employee):

    def __init__(self, working_hours, hourly_rate):
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        salary = self.working_hours * self.hourly_rate
        print("Part-Time Salary:", salary)


full_time = FullTimeEmployee(30000)
part_time = PartTimeEmployee(80, 200)

full_time.calculate_salary()
part_time.calculate_salary()

# Create a parent class Shape with an area() method. Create child classes Circle, Rectangle, and Square. Calculate and display the area of each shape using method overriding. 
class Shape:

    def area(self):
        print("Area of shape")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        result = 3.14 * self.radius * self.radius
        print("Circle Area:", result)
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        result = self.length * self.breadth
        print("Rectangle Area:", result)
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        result = self.side * self.side
        print("Square Area:", result)
circle = Circle(5)
rectangle = Rectangle(10, 5)
square = Square(4)

circle.area()
rectangle.area()
square.area()

#Create a parent class Vehicle with a method start(). Create child classes Car, Bike, and Bus, each with a different implementation of start(). 
class vehicle:
    def start(self):
        print("vehicle is starting....")
class Car(vehicle):
    def start(self):
        print("Car staring with key")
class Bike(vehicle):
    def start(self):
        print("Bike starts with button...")
class Bus(vehicle):
    def start(self):
        print("Bus start with a key...")
def vehicle_type(types):
    types.start()
a=Car()
b=Bike()
c=Bus()

vehicle_type(a)
vehicle_type(b)
vehicle_type(c)


#Create a class Calculator with a method add() that accepts two or three numbers and returns their sum. 
class Calculator:
    def add(self,a,b,c=0):
        return a + b + c
a=Calculator()
print(a.add(5,10))
print(a.add(10,10,10))
print(a.add(20,20,20))

#Create three unrelated classes: EmailNotification, SMSNotification, and WhatsAppNotification. Each class should have a send() method. Create a function notify_user() that accepts any object and calls its send() method. 
class EmailNotification:
    def send(self):
        print("message send to Email")
class SMSNotification:
    def send(self):
        print("message send to SMS")
class WhatsappNotification:
    def send(self):
        print("message send to Whatsapp")
def notify_user(applications):
    applications.send()
a=EmailNotification()
b=SMSNotification()
c=WhatsappNotification()
notify_user(a)
notify_user(b)
notify_user(c)

#Create a parent class Bank with a method interest_rate(). Create child classes SBI, HDFC, and ICICI, each returning a different interest rate. Display the interest rate using a common function. 
class Bank:
    def interest_rate(self):
        print("bank interest...")
class SBI(Bank):
    def interest_rate(self):
        print("SBI interest is 5%")
class HDFC(Bank):
    def interest_rate(self):
        print("HDFC interest is 4%")
class ICICI(Bank):
    def interest_rate(self):
        print("ICIC interest is 6%")
bank_process=[Bank(),SBI(),HDFC(),ICICI()]
for i in bank_process:
    i.interest_rate()

#Create a list, tuple, string, and dictionary. Use the same built-in functions len() and type() on all four objects. Explain how the same function works with different object types. 
list=[20,30,40,60]
tuple=(10,20,30,40)
string="polymorphism"
Dictionary={"name": "Geetha", "age":21}

print("List")
print("length:",len(list))
print("type:",type(list))

print("Tuple")
print("length:",len(tuple))
print("type:",type(tuple))


print("string")
print("length:",len(string))
print("type:",type(string))

print("Dictionary")
print("length:",len(dictionary))
print("type:",type(Dictionary))


#Create a parent class Food with a method prepare(). Create child classes Pizza, Burger, and Biryani. Each class should provide its own preparation process. Call prepare() using a common function that accepts different food objects. 
class Food:
    def prepare(self):
        print("food preparation")
class pizza(Food):
    def prepare(self):
        print("Preparing pizza:Add topping and bake")
class Burger(Food):
    def prepare(self):
        print("Preparing Burger: add vegetables and grill")
class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani:cook rice with spices and chicken")
def food_preparation(items):
    items.prepare()
item1=pizza()
item2=Burger()
item3=Biryani()
food_preparation(item1)
food_preparation(item2)
food_preparation(item3)

#Create a class Book with attributes pages. Overload the + operator using __add__() to add the pages of two books. Expected output: Book 1 pages: 150 Book 2 pages: 200 Total pages: 350 
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,others):
        return self.pages + others.pages
Book1=Book(150)
Book2=Book(200)
print("Total pages:",Book1+Book2)


#Create a clacss Product with an attribute price. Overload the > operator using __gt__() to compare the prices of two products. Display which product has the higher price. 
class Product:
    def __init__(self,price):
        self.price=price
    def __gt__(self,other):
       return self.price > other.price
product1=Product(500)
product2=Product(200)

print("product1:",product1.price)
print("product2:",product2.price)

if product1 > product2:
    print("product1 has the  higher price")
else:
    print("product2 has the higher price")


#Create three classes: Audio, Video, and Podcast. Each class should have a play() method. Create a function play_media() that accepts any object and calls its play() method without checking its class. 
class Audio:
    def play(self):
        print("audio...")
class Video:
    def play(self):
        print("video....")
class Podcast:
    def play(self):
        print("podcast....")
def Play_media(playlist):
    playlist.play()
a=Audio()
b=Video()
c=Podcast()

Play_media(a)
Play_media(b)
Play_media(c)

#Create a parent class Employee with a class method company_info(). Create child classes Developer and DataAnalyst that override the class method. Call the method using both child classes and explain the output. 
class Employee:
    @classmethod
    def company_info(self):
        print("Employee Company")
class Developer(Employee):
    @classmethod
    def company_info(self):
       print("developer company info")
class DataAnalyst(Employee):
    @classmethod
    def company_info(self):
        print("DataAnalyst company info")
Developer.company_info()
DataAnalyst.company_info()



#Create classes Electronics, Clothing, and Grocery. Each class should have a method calculate_discount() with a different discount calculation. Create a common function to calculate and display the final price for different products. 
class Electronics:
    def calculate_discount(self,price):
        return price * 0.10

class Clothing:
    def calculate_discount(self,price):
        return price * 0.05

class Grocery:
    def calculate_discount(self,price):
        return price * 0.05

def calculate_final_price(product,price):
    discount = product.calculate_discount(price)
    final_price = price - discount

    print("original price:",price)
    print("Discount:",discount)
    print("final prices:",final_price)

a=Electronics()
b=Clothing()
c=Grocery()

calculate_final_price(a,1000)
calculate_final_price(b,1000)
calculate_final_price(c,1000)


#Create a parent class Ride with a method calculate_fare(). Create child classes BikeRide, CarRide, and AutoRide. Each ride should calculate its fare based on distance and its own rate per kilometer. Display the fare using a common function.
class Ride:
    def calculate_fare(self, distance):
        return 0


class BikeRide(Ride):
    def calculate_fare(self, distance):
        return distance * 10


class CarRide(Ride):
    def calculate_fare(self, distance):
        return distance * 20


class AutoRide(Ride):
    def calculate_fare(self, distance):
        return distance * 15


def display_fare(ride, distance):
    fare = ride.calculate_fare(distance)
    print("Fare:", fare)


bike = BikeRide()
car = CarRide()
auto = AutoRide()

display_fare(bike, 10)
display_fare(car, 10)
display_fare(auto, 10)

#Create a parent class Doctor with a method treat_patient(). Create child classes Cardiologist, Dentist, and Neurologist. Each doctor should provide a different treatment description. Use polymorphism to call the methods. 
class Doctor:
    def treat_patient(self):
        print("Doctor is treating the patient")


class Cardiologist(Doctor):
    def treat_patient(self):
        print("Cardiologist treats heart-related problems")


class Dentist(Doctor):
    def treat_patient(self):
        print("Dentist treats teeth-related problems")


class Neurologist(Doctor):
    def treat_patient(self):
        print("Neurologist treats nervous-system-related problems")


doctors = [
    Cardiologist(),
    Dentist(),
    Neurologist()
]

for doctor in doctors:
    doctor.treat_patient()


#Create classes CSVFile, JSONFile, and TextFile. Each class should have a read_file() method. Create a common function process_file() that accepts different file objects and calls the appropriate method. 

class CSVFile:
    def read_file(self):
        print("Reading CSV file")


class JSONFile:
    def read_file(self):
        print("Reading JSON file")


class TextFile:
    def read_file(self):
        print("Reading Text file")


def process_file(file):
    file.read_file()


csv = CSVFile()
json = JSONFile()
text = TextFile()

process_file(csv)
process_file(json)
process_file(text)

#Q19. Custom Data Types Create a class Distance with attributes km and meters. Overload the + operator to add two distance objects and return the total distance in normalized kilometers and meters. Example: Distance 1: 2 km 500 meters Distance 2: 3 km 800 meters Total: 6 km 300 meters 
class Distance:
    def __init__(self, km, meters):
        self.km = km
        self.meters = meters

    def __add__(self, other):
        total_meters = self.meters + other.meters
        total_km = self.km + other.km

        if total_meters >= 1000:
            total_km += total_meters // 1000
            total_meters = total_meters % 1000

        return Distance(total_km, total_meters)


distance1 = Distance(2, 500)
distance2 = Distance(3, 800)

total = distance1 + distance2

print("Distance 1:", distance1.km, "km", distance1.meters, "meters")
print("Distance 2:", distance2.km, "km", distance2.meters, "meters")
print("Total:", total.km, "km", total.meters, "meters")

# Complete Polymorphism Challenge Create a class Employee and child classes Manager, Developer, and Tester. Each employee should have: • A work() method with a different implementation. • A calculate_bonus() method with a different implementation. • A display_details() method to display employee information. 

class Employee:
    def work(self):
        print("Employee is working")

    def calculate_bonus(self):
        print("Employee bonus")

    def display_details(self):
        print("Employee details")


class Manager(Employee):
    def work(self):
        print("Manager manages the team")

    def calculate_bonus(self):
        print("Manager bonus: 20%")

    def display_details(self):
        print("Manager: Geetha")


class Developer(Employee):
    def work(self):
        print("Developer writes code")

    def calculate_bonus(self):
        print("Developer bonus: 15%")

    def display_details(self):
        print("Developer: Ravi")


class Tester(Employee):
    def work(self):
        print("Tester tests the software")

    def calculate_bonus(self):
        print("Tester bonus: 10%")

    def display_details(self):
        print("Tester: Anu")


employees = [
    Manager(),
    Developer(),
    Tester()
]

for employee in employees:
    employee.display_details()
    employee.work()
    employee.calculate_bonus()
    print()