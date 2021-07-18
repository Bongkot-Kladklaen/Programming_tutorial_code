def celsius_to_fah(celsius):
    return (celsius * 9 / 5) + 32

def temperature_tabel():
    for c in range(0,101,5):
        f = celsius_to_fah(c)
        print("{}c = {}F".format(c, f))

def menu():
    print("1. convert Celsius to Fharenheit")
    print("2. display temperature table")
    n = input("enter choice: ")
    if n == '1':
        celsius = float(input("enter degree in Celsius: "))
        print("{}C = {}F".format(celsius, celsius_to_fah(celsius)))
    elif n == "2":
        temperature_tabel()

menu()