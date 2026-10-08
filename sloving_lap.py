age : str =(input("Enter your age: "))
day : str= input("Enter the day: ")
student : str= input("Are you a student? (yes/no): ")

age =int(age)

if age < 0 or age >100:
    print("Invalid age")
    exit()
    

valid_days : list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if day not in valid_days:
    print("Invalid day")
    exit()

if age < 5:
    price = 0
elif age <= 12:
    price = 6
elif age <= 59:
    price = 10
else:
    price = 7


if day == "Friday" and price > 0:
    price += 2

if student == "yes" and price > 0:
    price = price * 0.8

if price == 0:
    print("Ticket price: Free")
else:
    print(f"Ticket price: ${price:.2f}")
