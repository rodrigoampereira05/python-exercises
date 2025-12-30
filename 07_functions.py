#Function 1
def greet():
    name = input("Your name: ")
    print(f"Hello, {name}")

greet()

#Function 2
def greet_2(name):
    print(f"Hello, {name}")
your_name = input("Your name: ")

greet_2(your_name)



#Function 3
def add(a, b):
    soma = a + b
    return soma

a = 5
b = 5

#print(add(a,b))
soma = add(a,b)
print(soma)
soma_2= add(10,a)
print(soma_2)



#Function 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

numero = int(input("Number: "))
result = is_even(numero)

if result:
    print("Even")
else:
    print("Odd")
