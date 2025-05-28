#1 
def saludo_de_bienvenida():
    print("hola mundo")
    return saludo_de_bienvenida
#Programa Pricinpial

saludo_de_bienvenida()

#2
def saludar_usuario(nombre): 
    return "Hola ",nombre

#Programa Principal

nombre= input("Introduce tu nombre: ")
print(saludar_usuario(nombre))  

#3
def informacion_personal(nombre, apellido,edad,residencia):
    return f"Hola {nombre} {apellido}, tienes {edad} años y vives en {residencia}."


# Programa Principal
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ") 
residencia = input("Introduce tu lugar de residencia: ")


print(informacion_personal(nombre, apellido, edad, residencia)) 

#4
def calcular_area_circulo(radio):
    return 3.14159 * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * 3.14159 * radio

#Programa Principal

radio = float(input("Introduce el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

#5

def segundos_a_horas(segundos):
    return segundos // 3600 

#Programa Principal

segundos = int(input("Introduce el número de segundos: ")) 
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

#6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Programa Principal
numero = int(input("ingrese un numero : " )) 
print(f"Tabla de multiplicar del {numero}:")
tabla_multiplicar(numero)   

#7
def opereaciones_basica(a,b):
    return a + b, a - b, a * b, a / b
 
#Programa Principal 

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma, resta, multiplicacion, division = opereaciones_basica(a, b) 
print("la suma es :", suma)
print("la resta es :", resta)
print("la multiplicacion es :", multiplicacion)
print("la division es :", division) 

#8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Programa Principal
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: ")) 
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

#9

def celsius_a_fahrenheint(celsius):
    return (celsius * 9/5 ) +32 

#Programa Principal

celsius = float(input("ingrese la temperatura de grado celsius "))

fahrenheint = celsius_a_fahrenheint(celsius)
print (f"{celsius}°C Equivale a {fahrenheint}°F")

#10
def calcular_promedio(a , b , c):
    return (a + b + c) / 3 

#Programa Principal 

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))

promedio = calcular_promedio(num1,num2,num3 )

print (f"el promedio de {num1}, {num2}, {num3} es el {promedio}")