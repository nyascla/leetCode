import os

# Directorio del que quieres listar los archivos
directorio = '/ruta/al/directorio'

# Lista para almacenar los nombres de los archivos
archivos = os.listdir(directorio)

# Imprimir los nombres de los archivos
for archivo in archivos:
    print(archivo)

if __name__ == "__main__":
    print("here")