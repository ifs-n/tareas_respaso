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


print(f"valor random: {valor_radom}")
print(f"valor par: {valor_par}")