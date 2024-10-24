import random

# Inicializar las variables a 0 y crear las necesarias
puntuacion_usuario = 0
puntuacion_maquina = 0
jugando = True

# Programa del juego, se establece una variable que comprobará si se está jugando o no

# El final

while puntuacion_usuario or puntuacion_maquina < 3:
    opcion_maquina = random.randint(1, 3)
    opcion = int(input("Elige entre estas opciones: (1-Piedra//2-papel//3-Tijera), cualquier otra opción no será válida: "))
    if opcion == 1:
        if opcion_maquina == 1:
            print("Empate")
        if opcion_maquina == 2:
            print("La máquina eligió papel, perdiste")
            puntuacion_maquina = puntuacion_maquina + 1
            print("Tu puntaje:", puntuacion_usuario, "Puntaje de la máquina:", puntuacion_maquina)
            if puntuacion_maquina == 3:
                print("La máquina ganó, lo siento")
        if opcion_maquina == 3:
            print("Ganaste, la máquina eligió tijeras")
            puntuacion_usuario = puntuacion_usuario + 1
            print("Tu puntaje:", puntuacion_usuario, "Puntaje de la máquina:", puntuacion_maquina)
            if puntuacion_usuario == 3:
                print("Muy bien, ganaste")
    if opcion == 2:
        if opcion_maquina == 1:
            print("Ganaste, la máquina eligió piedra")
            puntuacion_usuario = puntuacion_usuario + 1
            print("Tu puntaje:", puntuacion_usuario, "Puntaje de la máquina:", puntuacion_maquina)
            if puntuacion_usuario == 3:
                print("Muy bien, ganaste")
        if opcion_maquina == 2:
            print("Empate")
        if opcion_maquina == 3:
            print("Perdiste, la máquina eligió tijeras")
            puntuacion_maquina = puntuacion_maquina + 1
            print("Tu puntaje:", puntuacion_usuario, "Puntaje de la máquina:", puntuacion_maquina)
            if puntuacion_maquina == 3:
                print("La máquina ganó, lo siento")
    if opcion == 3:
        if opcion_maquina == 1:
            print("Perdiste, la máquina eligió piedra")
            puntuacion_maquina = puntuacion_maquina + 1
            print("Tu puntaje:", puntuacion_usuario, "Puntaje de la máquina:", puntuacion_maquina)
            if puntuacion_maquina == 3:
                print("La máquina ganó, lo siento")
        if opcion_maquina == 2:
            print("La máquina eligió papel, ganaste")
            puntuacion_usuario = puntuacion_usuario + 1
            print("Tu puntaje:", puntuacion_usuario, "Puntaje de la máquina:", puntuacion_maquina)
            if puntuacion_usuario == 3:
                print("Muy bien, ganaste")
        if opcion_maquina == 3:
            print("Empate")






