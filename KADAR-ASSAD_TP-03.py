#Ej 1

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Su edad no puede ser menor que 0, vuelva a ejecutar e ingrese su edad correcta.")
elif edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")

#Ej 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ej 3

numero_par = int(input("Ingrese un número par: "))

if numero_par % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Ej 4

edad = int(input("Ingrese su edad: "))

if edad <= 12:
    print("Usted es niño/a.")
elif edad >= 12 and edad < 18:
    print("Usted es adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted es adulto/a joven.")
else:
    print("Usted es adulto/a.")

#Ej 5

password = input("Ingrese una contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ej 6
from statistics import mode, mean, median
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

print(f"La media es {media}, la moda {moda} y la mediana {mediana}.")

if media > mediana and mediana > moda:
    print("Existe un sesgo positivo ya que la media es mayor que la mediana y esta es mayor que la moda.")
elif media < mediana and mediana < moda:
    print("Existe un sesgo negativo la media es menor que la mediana y esta es menor que la moda.")
elif media == mediana == moda:
    print("No hay sesgos ya que la media, la moda y la mediana son iguales.")

#Ej 7
palabra = str(input("Ingrese una palabra: "))

if palabra[-1] in "aeiouAEIOU":
    palabra += "!"

print(palabra)

#Ej 8
name = str(input("Ingrese su nombre: "))
option = int(input("Si quiere su nombre en mayúsculas, ingrese 1 \n Si quiere su nombre en minúsculas ingrese 2 \n Si quiere su nombre con la primera letra en mayusculas, ingrese 3 \nIngrese la opción deseada: "))

if option == 1:
    print(name.upper())
elif option == 2:
    print(name.lower())
elif option == 3:
    print(name.title())
else:
    print("Usted ingresó un número no aceptado, vuelva a intentar.")

#Ej 9
mag_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if mag_terremoto < 3:
    print("Es muy leve.")
elif mag_terremoto >=3 and mag_terremoto < 4:
    print("Es leve.")
elif mag_terremoto >= 4 and mag_terremoto < 5:
    print("Es moderado.")
elif mag_terremoto >= 5 and mag_terremoto < 6:
    print("Es fuerte.")
elif mag_terremoto >= 6 and mag_terremoto < 7:
    print("Es muy fuerte.")
else:
    print("Es extremo.")

#Ej 10

hemisferio = str(input("¿En qué hemisferio te encontrás (N/S)? "))

month = int(input("Ingrese en que mes del año se encuentra (1-12): "))
day = int(input("Ingrese el día del mes en el que se encuentra (1-31): "))

if month < 0 or month > 12:
    print("Mes inválido. Vuelva a ejecutar.")

if day < 0 or day > 31:
    print("Día inválido Vuelva a ejecutar.")

date = month * 100 + day

if hemisferio == "n" or hemisferio == "N":
    if 1221 <= date <= 1231 or 101 <= date <= 320:
        estacion = "invierno"
    elif 321 <= date <=  620:
        estacion = "primavera"
    elif 621 <= date <= 920:
        estacion = "verano"
    elif 921 <= date <= 1220:
        estacion = "otoño"
elif hemisferio == "s" or hemisferio == "S":
    if 1221 <= date <= 1231 or 101 <= date <= 320:
        estacion = "verano"
    elif 321 <= date <=  620:
        estacion = "otoño"
    elif 621 <= date <= 920:
        estacion = "invierno"
    elif 921 <= date <= 1220:
        estacion = "primavera"

print(f"Usted está en {estacion}")

#Fin TP 3