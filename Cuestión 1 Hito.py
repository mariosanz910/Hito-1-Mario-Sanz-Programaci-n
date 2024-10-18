# Establece el menú
print("MENÚ")
opcion = int(input("Elige una figura a representar: (1-Cuadrado//2-Rectángulo): "))

# Obtiene la opción del usuario y la lleva a cabo, cuadrado en este caso
if opcion == 1:
    lado = int(input("Dame el lado del cuadrado: "))
    area_cuadrado = lado * lado
    perímetro_cuadrado = 4 * lado
    print("El area es igual a:", area_cuadrado, "y el preímetro es igual a:", perímetro_cuadrado)
    for i in range(0,  lado):
        print("*" * lado)

# Rectángulo
if opcion == 2:
    altura = int(input("Dame la longitud de la altura del rectángulo: "))
    base = int(input("Dame la longitud de la base del rectángulo "))
    area_rectángulo = base * altura
    perímetro_rectángulo = (2 * base) + (2 * altura)
    print("El área el rectángulo es:", area_rectángulo, "y el perímetro es:", perímetro_rectángulo)
    for i in range(0,  altura):
        print("*" * base)




