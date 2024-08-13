# Alertas Telemáticas

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

# cálculo de promedio
promedio = sum(velocidad) / len(velocidad)
#print(promedio)
lista = []

# recorre la lista con el método enumarate que extrae el valor y el index en elque se encuentra
for index, item in enumerate(velocidad):
    if item > promedio:
        lista.append(index)

print(f'\nLas posiciones que son mayor al promedio {promedio} son: \n {lista}')