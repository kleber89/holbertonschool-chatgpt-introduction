#!/usr/bin/python3
import sys

# Iterar sobre los argumentos de la línea de comandos, omitiendo el primer elemento (nombre del archivo)
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
