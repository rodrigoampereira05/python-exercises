age = int(input("Write your age: "))

if age < 18:
    print("Under age")
elif 18 <= age < 65:
    print("Adult")
else:
    print("Senior")