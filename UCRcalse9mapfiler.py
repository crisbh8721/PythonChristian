resutado = list(map(lambda x:x**2,range(1,11)))
print(resutado)
pares = [list(filter(lambda x: x%2 ==0, resutado))]
print(pares)
palabras = ['melocotón', 'kiwi', 'uva', 'aguacate', 'mango',
 'fresa', 'ciruela', 'coco', 'plátano', 'limón',
 'piña', 'granada', 'tamarindo', 'guanábana', 'maracuyá',
 'durazno', 'naranja', 'higo', 'frambuesa', 'mora']
mayusculas = list(map(str.upper,palabras))
print(mayusculas)
palbras_5_o_menos_letras = [list(filter(lambda x: len(x) <= 5, palabras))]
print(palbras_5_o_menos_letras)
pares_cuadrados = list(map(lambda x:x**2,filter(lambda x: x%2==0,range(1,11))))
print(pares_cuadrados)