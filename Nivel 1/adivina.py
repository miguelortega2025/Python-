""" Enunciado — "Adivina el número"
Crea un programa adivina.py con estas reglas:

El programa "piensa" un número secreto entre 1 y 20 (puedes fijarlo tú, por ejemplo secreto = 7).

Le pide al usuario que adivine el número.

Por cada intento:

Si el número es menor que el secreto → "Muy bajo 🔽"

Si es mayor → "Muy alto 🔼"

Si es igual → "¡Correcto! 🎉" y el programa termina.

El usuario tiene un máximo de 5 intentos. Si se acaban, muestra:
"Se acabaron los intentos. El número era 7."

Al final, muestra cuántos intentos usó (si ganó). """

#Ejercicio 2 - Adivina
import random

secreto = random.randint(1,20)
max_intentos = 5
intento = 0
adivino = False 
while intento < max_intentos: 
    try:
        numero = int(input("Adivina el numero (1-20): "))
        if numero < 1 or numero > 20: 
            print ("El numero debe estar entre 1 y 20")
            continue
        intento += 1
        if numero < secreto:
            print("Muy bajo ")
        elif numero > secreto: 
            print("Muy alto ")
        else:
            print(f"¡Correcto! Lo lograste en {intento} intentos.")
            adivino = True
            break
    except ValueError: 
        print("Debes escribir un número")

if not adivino: 
    print(f"Se acabaron los intentos. El numero era {secreto}.")
