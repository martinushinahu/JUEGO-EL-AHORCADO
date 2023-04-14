import random

# Lista de palabras para elegir al azar
palabras = ["gato", "perro", "elefante", "jirafa", "tigre", "leon"]

# Elegir una palabra al azar de la lista de palabras
palabra_secreta = random.choice(palabras)

# Convertir la palabra secreta en una lista de caracteres
palabra_secreta_lista = list(palabra_secreta)

# Crear una lista de guiones para mostrar al jugador
guiones = ["_"] * len(palabra_secreta)

# Inicializar las vidas del jugador
vidas = 6

# Función para pedirle al usuario que ingrese una letra
def pedir_letra():
    letra = input("Ingresa una letra: ").lower()
    # Verificar que la letra ingresada sea válida
    while len(letra) != 1 or not letra.isalpha():
        letra = input("Ingresa una letra válida: ").lower()
    return letra

# Función para verificar si la letra ingresada por el jugador está en la palabra secreta
def verificar_letra(letra, palabra_secreta_lista, guiones):
    if letra in palabra_secreta_lista:
        # Reemplazar los guiones correspondientes por la letra
        for i in range(len(palabra_secreta_lista)):
            if palabra_secreta_lista[i] == letra:
                guiones[i] = letra
        return True
    else:
        return False

# Función para imprimir la lista de guiones
def imprimir_guiones(guiones):
    print(" ".join(guiones))

# Función para verificar si el jugador ha ganado
def verificar_victoria(guiones):
    if "_" not in guiones:
        return True
    else:
        return False

# Imprimir la lista de guiones al comienzo del juego
imprimir_guiones(guiones)

# Ciclo principal del juego
while vidas > 0:
    letra = pedir_letra()
    if verificar_letra(letra, palabra_secreta_lista, guiones):
        # Si la letra está en la palabra secreta, imprimir la lista de guiones actualizada
        imprimir_guiones(guiones)
        if verificar_victoria(guiones):
            print("¡Has ganado!")
            break
    else:
        # Si la letra no está en la palabra secreta, disminuir las vidas del jugador
        vidas -= 1
        print("Letra incorrecta. Te quedan", vidas, "vidas.")
else:
    # Si el jugador ha perdido todas las vidas, imprimir un mensaje de derrota
    print("¡Has perdido! La palabra secreta era", palabra_secreta)
