import os
os.system("cls")

PRECIO_PLAN = 80000
PRECIO_RADIO = 12000

try:
    print("Bienvenido a la CLinica Davila")
    print("Ingrese sus datos para calcular el valor de su plan")
    edad = int(input("Ingrese su edad:\n"))
    if edad <= 0:
        edad = int(input("Ingrese una edad válida:\n"))
    quintil = int(input("Ingrese su quintil (1 a 5):\n"))
    if quintil not in range (1, 6):
        quintil = int(input("Ingrese un quintil válido:\n"))

    if edad <= 25 and quintil in range(1, 3):
        descuento_plan = PRECIO_PLAN * 0.18
    elif edad <= 25 and quintil in range(3, 5):
        descuento_plan = PRECIO_PLAN * 0.12
    elif edad in range(26, 46) and quintil in range(1, 3):
        descuento_plan = PRECIO_PLAN * 0.12
    elif edad in range(26, 46) and quintil in range(3, 5):
        descuento_plan = PRECIO_PLAN * 0.08
    else:
        descuento_plan = PRECIO_PLAN * 0

    if quintil in range(1, 4):
        descuento_radio = PRECIO_RADIO * 0.1
    else:
        descuento_radio = PRECIO_RADIO * 0

    if edad <= 45:
        descuento_radio2 = PRECIO_RADIO * 0.05
    else:
        descuento_radio2 = PRECIO_RADIO * 0

    preciofinal_plan = PRECIO_PLAN - descuento_plan
    precioradio_final = PRECIO_RADIO - descuento_radio - descuento_radio2

    print(f"Precio plan dental: ${preciofinal_plan}")
    print(f"Precio radiografia: ${precioradio_final}")

except:
    print("Uno de los datos ingresados no era correcto")


