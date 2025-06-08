'''
# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3

frutas = precios_frutas.keys()

print(frutas)
'''
# Ejercicio 4

def mi_lista_contactos(contactos):
    for i in range (1,6):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = int(input("Ingrese el teléfono: "))
        contactos [nombre] = telefono

contactos = {}

mi_lista_contactos(contactos)

busqueda_telefono = str(input('Ingrese el nombre del contacto para saber su teléfono: '))
if busqueda_telefono in contactos:
    print(contactos[busqueda_telefono])
else:
    print("No se encontró el contacto.")
'''
# Ejercicio 5

entrada = str(input('Ingrese una frase: '))

palabras = entrada.split( )
palabras_unicas = set(palabras)
tupla_palabras = tuple(palabras)

print(f"Palabras únicas: {palabras_unicas}")

conteo_palabras = {}

for palabra in palabras_unicas:
    conteo_palabras[palabra] = tupla_palabras.count(palabra)

print(f"Recuento: {conteo_palabras}")
'''

def ingreso_alumnos (cant_alumnos=1,cant_notas=1):
    for i in range(1,cant_alumnos+1):
        alumno = input(f"Ingrese el alumno número {i}: ")
        dataset = {alumno}
        for i in range(1,cant_notas+1):
            notas = float(input(f"Ingrese la nota número {i}: "))
            dataset[alumno] = notas

dataset = {}

ingreso_alumnos(3,3)
print(dataset)
'''