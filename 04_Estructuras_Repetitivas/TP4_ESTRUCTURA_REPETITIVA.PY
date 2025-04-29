#1
for i in range (1,101):
    print(i)

#2

numero = int(input("introduce un numero entero: "))
cont = 0

while numero > 0:
    cont += 1
    numero = numero // 10
print("El numero tiene", cont, "digitos")   

#3

inicio = int(input("introduce un numero entero: "))
fin = int(input("introduce otro numero entero: "))

if inicio > fin :
    inicio,fin = fin,inicio

suma = 0
for i in range(inicio + 1,fin):
    suma += i

print("La suma de los numeros entre", inicio, "y", fin, "es", suma)     

#4

suma = 0

while True:
    num = int(input("introduce un numero entero: "))

    if num == 0: 
        break

    suma += num
print (f"La suma de los numeros es {suma}")

#5

import random

numaleatorio = random.randint(0,9)
intentos = 0
adivinado = False
print ("intenta adivinar el numero entre 0 y 9")

while not adivinado:
    num = int(input("ingrese un numero : "))
    intentos += 1
    if num == numaleatorio:
        print("felicidades adivinaste el numero en", intentos, "intentos")
        adivinado = True

#6

for i in range (100, -1, -2) :
    print (i) 

#7

suma = 0

for i in range(0, 100):
    suma += i
print(f"la suma de los numeros es {suma}")

#8

num = [1, 100]

for num in range(num[0], num[1] + 1):
    if num % 2 == 0:
        print(num, end=", ")
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

#9

num = [0, 100]
suma = 0
cantidad = 0    

for numeros in num: 
    suma += numeros
    cantidad += 1

media = suma / cantidad
print(f"La media de los numeros es {media}") 

#10

num = input("introduce un numero: ")

numero_invertido = num[::-1]

print("El numero invertido es", numero_invertido)
