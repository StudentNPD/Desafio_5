# filtro.py

import sys

def filtrar_precios(productos, umbral, condicion='mayor'):
    if condicion == 'mayor':
        return {p: pr for p, pr in productos.items() if pr > umbral}
    elif condicion == 'menor':
        return {p: pr for p, pr in productos.items() if pr < umbral}
    else:
        return None

def main():
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Uso: python filtro.py <umbral> [condicion]")
        sys.exit(1)
    
    umbral = int(sys.argv[1])
    condicion = sys.argv[2].lower() if len(sys.argv) == 3 else 'mayor'
    
    if condicion not in ['mayor', 'menor']:
        print("Lo sentimos, no es una operación válida")
        sys.exit(1)
    
    productos_filtrados = filtrar_precios(precios, umbral, condicion)
    productos_lista = ", ".join(productos_filtrados.keys())
    
    mensaje = "mayores" if condicion == 'mayor' else "menores"
    print(f"Los productos {mensaje} al umbral son: {productos_lista}")

if __name__ == "__main__":
    main()

