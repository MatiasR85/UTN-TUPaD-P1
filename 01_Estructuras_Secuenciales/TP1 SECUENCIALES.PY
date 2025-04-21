#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("hola mundo")


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre=input("¿como te llamas ?")

print(f"hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombrecompleto=input("¿como es tu nombre completo?")
edad=input("¿cuantos años tenes?")
pais=input("¿cual es actualmente tu pais de residencia?")

print(f"mi nombre completo es {nombrecompleto}, tengo {edad} años y vivo en {pais}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

import math

radio=float(input("ingrese el radio del circulo"))

area= math.pi*(radio**2)
perimetro= 2*math.pi*radio 

print("el area del circulo es ", area )
print("el perimetro del circulo es", perimetro) 

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos= int(input("ingrese la cantidad de segundos:" ))

horas= segundos//3600

segundos_restantes= segundos% 3600

print(f"{segundos} segundos son equivalentes a {horas} horas y {segundos_restantes} segundos.")

#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("ingrese el numero"))

for i in range(0,11):
    resultado= i* numero 
    print(numero,"x", i, "=", resultado) 


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1= int(input("ingrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))

print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 =
#𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)

peso= float(input("ingrese su peso (kg)"))
altura= float(input("ingrese su altura (m)"))

IMC= peso/ (altura**2 )

print("su IMC es", IMC)
 

 #9) ) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

C= float(input("ingrese la temperatura en grados celsuis"))

F= 9/5 * C + 32 

print(f"{C}grados celsius son equivalentes a {F} grados fahrenheint")

#10) ) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1= float(input("ingrese el primer numero"))
num2= float(input("ingrese el segundo numero"))
num3= float(input("ingrese el tercer numero"))

promedio=(num1+num2+num3)/3 

print( "el promedio es", promedio) 






