import os
os.system("cls")

import random

print("Bienvenido al jueguito de los numeros")

num1 = int(input("Ingrese el limite inferior:\n"))
num2 = int(input("Ingrese el límite superior:\n"))

valor_radom = random.randint(num1, num2)

if valor_radom % 2 != 0:
    if valor_radom + 1 in range(num1, num2):
        valor_par = valor_radom + 1
    elif valor_radom + 1 not in range(num1, num2):
        valor_par = valor_radom - 1
    
else:
    valor_par = valor_radom
print(f"valor par {valor_par}")
intento1 = int(input("Ingrese su primer intento: \n"))

if intento1 != valor_par:
    if intento1 > valor_par:
        pista1 = "El numero ingresado es mayor"
    else:
        pista1 = "El número ingresado es menor"
    print(f"Fallaste\nPista: {pista1}")
    intento2 = int(input("Ingrese su segundo intento:\n"))
    if intento2 != valor_par:
        if abs(intento1 - valor_par) > abs(intento2 - valor_par):
            pista2 = "Tu segundo intento estuvo más cerca"
        else:
            pista2 = "Tu primer intento estuvo más cerca"
        print(f"Fallaste otra vez xd\nPista: {pista2}")
        intento3 = int(input("Prueba una última vez:\n"))
        if intento3 != valor_par:
            print("Perdiste jaja")
        else:
            print(f"Ganaste, el número era {valor_par}")
    else:
        print(f"Ganaste, él número era {valor_par}")
else:
    print(f"Ganaste, él valor era {valor_par}")



#print(f"valor random: {valor_radom}")
#print(f"valor par: {valor_par}")