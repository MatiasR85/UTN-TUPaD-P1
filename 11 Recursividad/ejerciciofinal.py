#EJERCICIO1 
def factorial(n):
    resultado=1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(f"el factorial de 5 es {factorial(5)}")

for i in range(1, 11):
    print(f"el factorial de {i} es {factorial(i)}")

#EJERCICIO2

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1 
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)
    
#Inicio De programa 
# 0 1 1 2 3 5 8 13 21 34 55
num = int(input("Ingrese un numero: "))
print(f"el numero de fibonacci en la posicion {num} es {fibonacci(num)}") 

#EJERCICIO3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
# Inicio de programa
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))     
    
print(f"{base} elevado a {exponente} es {potencia(base, exponente)}") 

#EJERCICIO4


def decimal_a_binario(decimal):
    if decimal == 0: 
        return "0" 
    binario = "" 
    while decimal > 0: 
        binario = str(decimal % 2) + binario #
        decimal //= 2 
    return binario 

# Inicio de programa
numero_decimal = int(input("Ingrese un numero decimal: "))  
print(f"El numero {numero_decimal} en binario es {decimal_a_binario(numero_decimal)}") 

#EJERCICIO5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
# Inicio de programa
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")  
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

#EJERCICIO6

def suma_digitos(n):
    resultado = 0
    while n > 0:
        resultado += n % 10 
        n //= 10 
    return resultado

#inicio de programa
numero = int(input("Ingrese un numeros entero positivo: "))
if numero < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    print(f"la suma de los digitos del numero {numero} es {suma_digitos(numero)}") 

#EJERCICIO7

def contar_bloques(n):
    resultado = 0
    return resultado if n == 0 else n + contar_bloques(n - 1)

# Inicio de programa
  
print("Contador de bloques")
numero = int(input("Ingrese un numero: "))
print(f"El numero de bloques es {contar_bloques(numero)}") 

#EJERCICIO8

def contar_digitos(numero,digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    elif numero < 10:
        return 1 if numero == digito else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digitos(numero // 10, digito)
# Inicio de programa

n= int(input("Ingrese un numero entero positivo: "))
d = int(input("Ingrese el digito a contar: "))

print(f"el digito {d} aparece {contar_digitos(n, d)} veces en el numero {n}.")
