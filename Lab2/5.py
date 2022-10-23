def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        print("Nie dzielimy przez zero!")
        exit()
    return x / y
def power(x,y):
    return pow(x,y)

print("Jaką operację chcesz wykonać?")
print("1) dodawanie")
print("2) odejmowanie")
print("3) mnożenie")
print("4) dzielenie")
print("5) potęgowanie")
while True:
    wybor = input("Wpisz numer operacji: ")
    if wybor not in ('1', '2', '3', '4', '5'):
        print("Zły kod operacji")
    if wybor in ('1', '2', '3', '4', '5'):
        num1 = float(input("Podaj argument 1: "))
        num2 = float(input("Podaj argument 2: "))
        if(wybor == '1'):
            print(add(num1, num2))
        elif(wybor == '2'):
            print(subtract(num1, num2))
        elif(wybor == '3'):
            print(multiply(num1, num2))
        elif(wybor == '4'):
            print(divide(num1, num2))
        elif (wybor == '5'):
            print(power(num1, num2))

    next = input("Powtórzyć operacje? Tak/nie ")
    if next == "nie":
         break
else:
    print("Błąd")