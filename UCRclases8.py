from dataclasses import replace

palabras1 = ["manzana","pera","zanahoria","sandia","papaya"]
longitud_palabra = [len(palabra) for palabra in palabras1]
print(longitud_palabra)
mayuscula = [palabra.upper() for palabra in palabras1]
print(mayuscula)
# Crear una lista con los cubos de los números del 1 al 10.
cubos = [i**2 for i in range(1,20)]
print(cubos)
# Generar una lista con los números impares del 1 al 20.
impares = [i for i in range(1,20) if (i%2 !=0)]
print(impares)
# Convertir una lista de strings a minúsculas.
palabras2 = ['MANZANA', 'PERA', 'ZANAHORIA', 'SANDIA', 'PAPAYA']
minúsculas = [palabra.lower() for palabra in palabras2]
print(minúsculas)
# Filtrar los nombres que empiezan con la letra "A".
nombres = ['andrés', 'carlos', 'david', 'esteban', 'fernando',
 'gabriel', 'hugo', 'ignacio', 'julio', 'luis',
 'mario', 'natalia', 'oscar', 'paula', 'quintin',
 'rafael', 'sofía', 'teresa', 'ulises', 'vanesa']
nombres_que_empiezan_con_la_letra_A = [name for name in nombres if name.startswith("a")]
print(nombres_que_empiezan_con_la_letra_A)
# Crear una lista de los primeros 10 múltiplos de 3.
primeros_10_múltiplos_de_3 = [i*3 for i in range(1,11)]
print(primeros_10_múltiplos_de_3)
# Dada una lista de palabras, obtener su longitud.
palabras3 = ['melocotón', 'kiwi', 'uva', 'aguacate', 'mango',
 'fresa', 'ciruela', 'coco', 'plátano', 'limón',
 'piña', 'granada', 'tamarindo', 'guanábana', 'maracuyá',
 'durazno', 'naranja', 'higo', 'frambuesa', 'mora']
longitud_palabras = [len(palabra) for palabra in palabras3]
print(longitud_palabras)
# Crear una lista de números del 1 al 100 que sean divisibles por 5 y 7.
divisibles_por_5_y_7 = [x for x in range(1,100) if x%5==0 and x%7==0]
print(divisibles_por_5_y_7)
# Reemplazar los espacios por guiones en una lista de frases.
nombres1 = ['andrés fernández', 'carlos méndez', 'david ramírez', 'esteban gómez', 'fernando lópez',
 'gabriel sánchez', 'hugo martínez', 'ignacio rodríguez', 'julio villalobos', 'luis torres',
 'mario pérez', 'natalia morales', 'oscar cruz', 'paula jiménez', 'quintin solano',
 'rafael vega', 'sofía herrera', 'teresa castro', 'ulises valverde', 'vanesa navarro']
espacios_por_guiones = [nombre.replace(" ","-") for nombre in nombres1]
print(espacios_por_guiones)
# Crear una lista de booleanos que indiquen si los números del 1 al 10 son pares.
pares = [x for x in range(1,11) if x%2==0]
print(pares)
# Dada una lista de temperaturas en Celsius, convertirlas a Fahrenheit.
temperaturas_celsius = [-10, -5, 0, 5, 10,15, 20, 25, 30, 35,40, 45, 50, 55, 60,65, 70, 75, 80, 85]
celsius_a_Fahrenheit = [celsius*9/5+32 for celsius in temperaturas_celsius]
print(celsius_a_Fahrenheit)