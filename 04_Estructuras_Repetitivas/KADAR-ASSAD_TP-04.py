#Ejercicio 1

for i in range (0,101):
    print(i)

#Ejercicio 2

num = int(input("Ingrese un número entero: "))
print(f"La cantidad de dígitos de {num} es {len(str(num))}")

#Ejercicio 3

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

count = x + 1
sum = x + 1

for i in range (x+1,y-1):
    count += 1
    sum = sum + count
print(sum)

#Ejercicio 4

num = int(input("Ingrese un número entero o 0 para finalizar el programa: "))
sumatoria = num
while num != 0:
    num = int(input(f"La suma acumulada al momento es {sumatoria}, ingrese otro número distinto de 0 para finalizar: "))
    sumatoria += num
print(f"Fin del programa. La sumatoria total es {sumatoria}.")

#Ejercicio 5
import random
num = random.randint(0,9)
#print(num)   se utiliza para probar el juego
contador = 1
print("Adivine el número del 0 al 9: ")
num_adiv = int(input())

while num_adiv != num:
    print("El número es incorrecto, intentelo nuevamente: ")
    contador += 1
    num_adiv = int(input(""))

print(f"¡Felicitaciones! El número era {num}. Lo adivinaste en {contador} intentos.")

#Ejercicio 6
num = 101
for i in range (1,101):
    num = num - 1
    print(num)
#Ejercicio 7

x = 0
y = int(input("Ingrese un número: "))

count = x + 1
sum = x + 1

for i in range (x+1,y):
    count += 1
    sum = sum + count
print(sum)

#Ejercicio 8
pares = 0
impares = 0
negativo = 0
positivo = 0
contador = 1

for i in range (1,101):
    print(f"Ingrese el número {contador}:")
    num = (int(input()))
    contador += 1

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivo += 1
    else:
        negativo += 1

print("Programa finalizado")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivo}")
print(f"Cantidad de números negativos: {negativo}")

#Ejercicio 9

contador = 1
sum_acum= 0
num_solicitados = 10

for i in range (1,num_solicitados+1):
    print(f"Ingrese el número {contador}: ")
    num = int(input())
    contador += 1
    sum_acum += num

print(f"La media de los números solicitados es {sum_acum/num_solicitados}")

#Ejercicio 10

invertido = 0

print("Escribe un número y lo devolveré invertido: ")
num = int(input())

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10

print(f"El número que elegiste invertido es {invertido}")
