#1

edad=int(input("ingrese su edad "))

if edad>=18:
    print("es mayor de edad")

#2

nota=int(input("debe ingresar la nota "))

if nota>=6:
    print("aprobado")
else:
    print("desaprobado") 
 
#3

numero=int(input("ingrese un numero "))

if numero % 2 == 0:
    print("¡ha ingresado un numero par!")
else:
    print("¡por favor, ingrese un numero par!")

#4

edad=int(input("ingrese su edad "))

if edad >= 0 and edad < 12:
    print("eres un niño/a")
elif edad >= 12 and edad < 18:
    print("eres un adolescente")
elif edad >=18 and edad <30:
    print("eres un adulto/a joven") 
else:
    print("eres un adulto/a")

#5

edad=int(input("ingrese su edad "))

if edad >= 0 and edad < 12:
    print("eres un niño/a")
elif edad >= 12 and edad < 18:
    print("eres un adolescente")
elif edad >=18 and edad <30:
    print("eres un adulto/a joven") 
else:
    print("eres un adulto/a")

#6
import statistics,random
numeros_aleatorios = [random.randint(1, 100) for x in range(100)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")


if media > mediana > moda:
    print("sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("no tiene sesgo.")
else:
    print("tiene un sesgo diferente al esperado.")

#7

frase= input("ingrese una frase ")

if frase [-1].lower() in "aeiou":
    print (frase+ "!")
else:
    print(frase) 

#8  

nombre=input("ingrese su nombre ")
opcion=input("ingrese una opcion 1 para mayuscula,2 para minuscula,3 para primer letra en mayuscula ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("opcion no valida")

#9

magnitud= float(input("ingrese la magnitud del terremoto segun la escala de richter "))

if magnitud < 3:
    print("muy leve(imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("leve(ligaramente preceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado(sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte(puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte(puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10

def determinarestacion():
    print("Bienvenido al programa para determinar la estación del año.")
    print("Por favor, ingrese los siguientes datos:")
    

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = input("Ingrese el mes del año: ").lower()
dia = int(input("Ingrese el día del mes: "))

    
meses = { "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,"mayo": 5, "junio": 6, "julio": 7, "agosto": 8,"septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12 }
m = meses.get(mes, 0)

    # Clasificar la estación
if (m == 12 and dia >= 21) or (1 <= m <= 2) or (m == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (m == 3 and dia >= 21) or (4 <= m <= 5) or (m == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (m == 6 and dia >= 21) or (7 <= m <= 8) or (m == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (m == 9 and dia >= 21) or (10 <= m <= 11) or (m == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
else:
        estacion = "Fecha inválida"

print(f"Estación: {estacion}")