# Inicializamos las variables necesarias a 0
saldo = 0

# Pedir el saldo inicial y asegurarse de que sea positivo
while True:
    saldo = float(input("Indique el saldo de la cuenta (debe ser un número positivo): "))
    if saldo >= 0:
        break
    else:
        print("Error, no puedes introducir una cantidad negativa, vuelva a intentarlo porfavor")

# Establecemos los contadores de ingresos y retiradas a 0
num_ingresos = 0
num_retiros = 0

# Menú principal
while True:
    print("--- Ingrese el número para seleccionar la opción ---")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    print("Recuerde que su saldo es", saldo)
    print("_________________________")

    # Leer la opción del menú
    opcion = int(input("Selecciona una opción (1-5): "))

    # Opción de ingreso con 1
    print("_________________________")
    if opcion == 1:
        ingreso = float(input("Introduce la cantidad a ingresar: "))
        if ingreso > 0:
            saldo += ingreso
            num_ingresos += 1
            print("Perfecto, tu saldo es ahora:", saldo)
        else:
            print("No puedes ingresar cantidades negativas o cero.")
    
    # Opción del retirada con 2
    elif opcion == 2:
        print("_________________________")
        retiro = float(input("Introduce la cantidad a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                num_retiros += 1
                print("Perfecto, tu saldo es ahora:", saldo)
            else:
                print("No puedes retirar más dinero del que tienes en tu cuenta.")
        else:
            print("No puedes retirar cantidades negativas o cero.")
    
    # Opción del saldo con 3
    elif opcion == 3:
        print("_________________________")
        print("Perfecto, tu saldo es ahora:", saldo)
    
    # Mostrar estadísticas con 4
    elif opcion == 4:
        print("_________________________")
        print("Estadísticas:")
        print("Ingresos realizados:", num_ingresos)
        print("Retiros realizados:", num_retiros)
    
    # Salir del programa con 5
    elif opcion == 5:
        print("_________________________")
        print("Gracias por utilizar nuestros servicios")
        break

    # Opción no válida
    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 5, fíjate en el menú")







