# import module
from tabulate import tabulate
# Creamos la tabla con listas vacías al comienzo
articulo = [[], [], []]
n = int(input("Ingresa nuevamente la cantidad: "))

# Leemos los datos y los agregamos a la tabla
for i in range(n):
    print("Ingrese el lector del codigo de barras sobre el articulo", i + 1)
    codigo = input("Identificador: ")
    nombre = input("Nombre: ")
    precio = int(input("Precio: "))
    articulo[0].append(codigo)
    articulo[1].append(nombre)
    articulo[2].append(precio)
    
# Ahora mostremos los valores en la tabla
for i in range(n):
    head = ["Identificador", "Nombre", "Precio"]
    '''print("Mostrando los datos de la persona", i + 1)
    print("Identificador:", articulo[0][i])
    print("Nombre:", articulo[1][i])
    print("Precio:", articulo[2][i])'''
    print(tabulate(articulo[i], headers=head, tablefmt="grid"))
