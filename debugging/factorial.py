#!/usr/bin/python3
import sys

def factorial(n):
    # Si el número es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    
    # Inicializar el resultado como 1
    result = 1
    
    # Calcular el factorial usando un bucle while
    while n > 1:
        result *= n
        n -= 1  # Reducir n en cada iteración
    
    return result

# Verificar si se proporciona un argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <numero>")
    sys.exit(1)

# Convertir el argumento a entero y calcular el factorial
try:
    num = int(sys.argv[1])
    result = factorial(num)
    print("El factorial de", num, "es:", result)
except ValueError:
    print("Por favor, proporcione un número entero válido como argumento.")
    sys.exit(1)
