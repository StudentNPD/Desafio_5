# Desafio ONG
# Crear un script llamado ong.py que contenga las siguientes funciones:
# ○ Una función que calcule el factorial.
# ○ Una función que calcule la productoria.
# ○ Una función que permita controlar los cálculos. Esta función se debe invocar de la siguiente manera:
# Output
# calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
#   El factorial de 5 es 120
#   La productoria de [4, 6, 7, 4, 3] es 2016
#   El factorial de 6 es 720

# ○ Una función que calcule el factorial
def calcular_factorial(fact_i):
    n = fact_i
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

# ○ Una función que calcule la productoria
def calcular_productoria(prod_i):
    productoria = 1
    for numero in prod_i:
        productoria *= numero
    return productoria

# ○ Una función que permita controlar los cálculos
def calcular(**kwargs):
    if 'fact_1' in kwargs:
        fact_1 = kwargs['fact_1']
        print(f"El factorial de {fact_1} es {calcular_factorial(fact_1)}")
    
    if 'prod_1' in kwargs:
        prod_1 = kwargs['prod_1']
        print(f"La productoria de {prod_1} es {calcular_productoria(prod_1)}")
    
    if 'fact_2' in kwargs:
        fact_2 = kwargs['fact_2']
        print(f"El factorial de {fact_2} es {calcular_factorial(fact_2)}")

# Invocar la función con los parámetros dados
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)