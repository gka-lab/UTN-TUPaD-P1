#Funciones

import math

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje} "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje} "))
    return n

def leer_positivo_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje} "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje} "))
    return n
'''
def pedido_de_datos_numericos(mensaje, cant_mensajes, min = 1, max = float("Inf")): 
    for i in range (cant_mensajes):
        x = 0
        list[x] = float(input(f"{mensaje} "))
        x += 1
        while n < min or n > max:
            n = int(input(f"{mensaje} "))
    return n
'''

#Ej 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Ej 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Ej 3
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ej 4
def calcular_area_circulo(radio):
    area = radio**math.pi    
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

#Ej 5
def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return horas

#Ej 6
def tabla_multiplicar(numero):
    multiplicador = 1
    while multiplicador < 11:
        print(f"{numero} x {multiplicador} = {numero*multiplicador}")
        multiplicador = multiplicador + 1

#Ej 7
def operaciones_basicas(a,b):
    a = leer_entero_validado("Ingrese un número mayor a 0: ", 1)
    b = leer_entero_validado("Ingrese otro número mayor a 0: ", 1)
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} x {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

#Ej 8
def calcular_imc(peso,altura):
    imc = peso / altura**2
    print(f"El índice de masa muscular que usted posee es de {imc}.")

#Ej 9
def celcius_a_fahrenheit(celcius):
    fahrenheit = (9/5) * celcius + 32
    print(f"{celcius} grados Celcius equivalen a {fahrenheit} grados Fahrenheit")
    
#Ej 10
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es {promedio}.")

#Programa principal

#Ej 1
imprimir_hola_mundo()

#Ej 2
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Ej 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia =input("Ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

#Ej 4
radio = leer_entero_validado("Ingrese el radio de un círculo: ",1)
print(f"El área del círculo es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}")

#Ej 5

segundos = leer_entero_validado("Ingrese una cierta cantidad de segundos: ")
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} hora/horas.")

#Ej 6
numero = leer_entero_validado("Ingrese un número: ")
tabla_multiplicar(numero)

#Ej 7

operaciones_basicas(0,0)

#Ej 8

peso = leer_positivo_decimal_validado("Ingrese su peso: ", 1)
altura = leer_positivo_decimal_validado("Ingrese su altura en CM: ", 1)
calcular_imc(peso,altura)

#Ej 9

celcius = leer_positivo_decimal_validado("Ingrese la temperatura en celcius: ",1)
celcius_a_fahrenheit(celcius)

#Ej 10

a = leer_positivo_decimal_validado("Ingrese el primer número: ")
b = leer_positivo_decimal_validado("Ingrese el segundo número: ")
c = leer_positivo_decimal_validado("Ingrese el tercer número: ")

calcular_promedio(a,b,c)
