# expresiones = [
#     not False,
#     not 3 == 5,
#     33/3 == 11 and 5 > 2,
#     True or False,
#     True*5 == 2.5*2 or 123 >= 23,
#     12 > 7 and True < False
# ]

# print(expresiones)
# print (False==False) 

# nombre = "Juan Carlos"
# edad = 15

# puntos = [nombre != "****" and
#  10< edad < 18 and
#  3<= len(nombre) < 10 and
#  edad * 4 > 40
 
#   ]


# print(puntos)


# a = 10
# b = -5
# c = "Hola"
# d = [1, 2, 3]
# e= (4,5,6)

# print(a * 5)  
# print(a - b)    
# print(c + "Mundo")   
# print(c * 2)        
# print(c[-1])        
# print(c[1:])    
# print(d + d)       
# print(e[1])
# print(e+(7,8,9))



    # numero_1 = 9
    # numero_2 = 3
    # numero_3 = 6
    # media = (numero_1 + numero_2 + numero_3) / 3
    # print("la nota media es", media)


# A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:
# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total
# Ejemplos:
# nota_1 = 10
# nota_2 = 7
# nota_3 = 4
# nota_final = float((nota_1)*0.15 + (nota_2)*0.35 + (nota_3)*0.50)
# print(round(nota_final,2))

#  La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

# 🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

matriz = [ 
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

# matriz[0].append(sum(matriz[0][:]))
# matriz[1].append(sum(matriz[1][:]))
# matriz[2].append(sum(matriz[2][:]))
# matriz[3].append(sum(matriz[3][:]))
# print(matriz)

 
# n = 0
# while n <= 5: 
#     n += 1
#     print("N vale ", n)

# else: 
#         print('Se acabo lo que se daba')
# # while True:
# #     print('NO VENGO DE ABAJO')

# numeros =  [1,2,3,4]
# # numeros.insert(0,'casa')
# numeros[:0] = ['casa']
# print(numeros)



# matriz[0].append(sum(matriz[0]))
# matriz[1].append(sum(matriz[1]))
# matriz[2].append(sum(matriz[2]))
# matriz[3].append(sum(matriz[3]))
# print(matriz)

# valor1=1
# valor2=2
# valor3='pepe'

# if valor1 > valor2:
#     print(valor1)
#     if valor1 < valor2:
#         print(valor2)

# print(valor3)

# if valor1 < valor2:
#     print(valor1)
# else:
#         print(valor2)

# print(valor3)

# edad = int(input("Por favor ingrese su edad: \n"))
# if edad >= 18:
#     print('Eres mayor de edad')
# else:
#     print('Eres menor de edad')

# Un curso se ha dividido en dos grupos: A y B, de acuerdo al nombre y a una preferencia (Marvel o Capcom). 
# El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N 
# y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla 
# el grupo que le corresponde.
# nombre = str(input("Por favor ingrese su nombre: \n"))
# nombre = nombre.lower()
# preferencia = str(input("Por favor ingrese su preferencia: \n"))
# preferencia = preferencia.lower()
# if nombre < 'm' and preferencia == 'marvel':
#     print('Eres del grupo A')

# elif nombre > 'n' and preferencia == 'capcom':
#      print('Eres del grupo B')

# else: 
#     print('Eres del grupo B')

# nombre = str(input("Por favor ingrese su nombre: \n"))
# nombre = nombre.lower()
# preferencia = str(input("Por favor ingrese su preferencia: \n"))
# preferencia = preferencia.lower()
# if (nombre < 'm' and preferencia == 'marvel') or (nombre > 'n' and preferencia == 'capcom'):
#     print('Eres del grupo A')

# else: 
#     print('Eres del grupo B')

# contraseña = 'aurora2021' 
# contraseña_user = input('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# elif contraseña != contraseña_user:
#     print('su contraseña no es válidad, tiene 2 intentos más')
# contraseña_user = input ('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# elif contraseña != contraseña_user:
#     print('su contraseña no es válidad, tiene 1 intentos más')
# contraseña_user = input ('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# else:
#     print('usted ha bloqueado su contraseña')

# contraseña = 'aurora2021' 
# contraseña_user = input('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# else:
#      print('su contraseña no es valida, tiene 2 intentos')
#      contraseña_user = input ('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# else:
#      print('su contraseña no es valida, tiene 1 intentos')
#      contraseña_user = input ('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# else:
#     print('usted ha bloqueado su contraseña')

# contraseña = 'aurora2021' 
# contraseña_user = input('Ingrese su contraseña:').lower()
# if contraseña == contraseña_user:
#     print('su contraseña es válida')
# elif contraseña != contraseña_user:
#     print('su contraseña no es válidad, tiene 2 intentos más')
#     contraseña_user = input ('Ingrese su contraseña:').lower()
#     if contraseña == contraseña_user:
#         print('su contraseña es válida')
#     elif contraseña != contraseña_user:
#         print('su contraseña no es válidad, tiene 1 intentos más')
#         contraseña_user = input ('Ingrese su contraseña:').lower()
#         if contraseña == contraseña_user:
#             print('su contraseña es válida')
#         else:
#             print('usted ha bloqueado su contraseña')


# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

# a = float(input('ingrese valor a:'))
# b = float(input('ingrese valor b:'))
# if b==0:
#     print('error, no puede dividir entre cero, intente de nuevo')
#     a = float(input('ingrese valor a:'))
#     b = float(input('ingrese valor b:'))
#     if b==0:
#         print('error, vuelve a secundario')
#     else: 
#         print('su resultado es:',a/b)
# else:
#     print('su resultado es:',a/b)

# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
#  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


# eleccion_pizza=(input('Vegetariana o No Vegetariana?:')).lower()
# vegetarianos= [
# ('Pimiento'.lower()),
# ('Tofu'.lower())
# ]
# no_vegetarianos = [
# ('Peperoni'.lower()),
# ('Jamon'.lower()),
# ('Salmon'.lower())
# ]
# if eleccion_pizza == "vegetariana":
#     print('elija UN INGREDIENTE entre las siguientes opciones para su pizza:' ,vegetarianos)
#     ingrediente_pizza=(input('')).lower()
#     print('Su pizza es' ,eleccion_pizza, 'y sus ingredientes son: mozzarella, salsa de tomate,',ingrediente_pizza )
# else:
#     print('elija UN INGREDIENTE entre las siguientes opciones para su pizza:' ,no_vegetarianos)
#     ingrediente_pizza=(input('')).lower()
#     print('Su pizza es' ,eleccion_pizza, 'y sus ingredientes son: mozzarella, salsa de tomate,',ingrediente_pizza )

# eleccion_pizza=(input('Vegetariana o No Vegetariana?:')).lower()
# vegetarianos= '''
# Pimiento
# Tofu
# '''
# no_vegetarianos = '''
# Peperoni
# Jamon
# Salmon
# '''
# if eleccion_pizza == "vegetariana":
#     print('elija UN INGREDIENTE entre las siguientes opciones para su pizza:' ,vegetarianos)
#     ingrediente_pizza=(input('')).lower()
#     print('Su pizza es' ,eleccion_pizza, 'y sus ingredientes son: mozzarella, salsa de tomate,',ingrediente_pizza )
# else:
#     print('elija UN INGREDIENTE entre las siguientes opciones para su pizza:' ,no_vegetarianos)
#     ingrediente_pizza=(input('')).lower()
#     print('Su pizza es' ,eleccion_pizza, 'y sus ingredientes son: mozzarella, salsa de tomate,',ingrediente_pizza )

# num=5
# while num > 0:
#     print(num)
#     num-=1
# print("terminó el conteo")

num=0
while num <= 5:
    num+=1
    print('num vale',num)



  
    
