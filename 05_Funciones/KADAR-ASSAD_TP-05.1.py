
#Ejercicio 1

array_multiplo4 = list(range(4,101,4))
print(array_multiplo4)

#Ejercicio 2

list = [1,2,3,4,5]
print(list[3])
print(list[-2])

#Ejercicio 3

empty_list = []
empty_list.append("not")
empty_list.append("empty")
empty_list.append("anymore")
print(empty_list)

#Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#Ejercicio 5

numeros = [8, 15, 3, 22, 7] #Crea una lista con 5 datos (posiciones del 0 al 4).
numeros.remove(max(numeros)) #Luego, busca el número más alto y lo quita de la lista.
print(numeros) #Finalmente, imprime la lista por consola.

#Ejercicio 6

list_ex_6 = list(range(10,31,5))
print(list_ex_6[0:2])

#Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "palio"
autos[2] = "fitito"

print(autos)

#Ejercicio 8

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Ejercicio 9

compras = [["pan", "leche"], ["arroz","fideos","salsa"],["agua"]]
    #A
compras[2].append("jugo")
    #B
compras[1][1] = "tallarines"
    #C
compras[0].remove("pan")
    #D
print(compras)


#Ejercicio 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)