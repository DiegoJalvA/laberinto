import random


laberinto = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.'],
    ['#', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E']
]


def mostrar_laberinto():
    for fila in laberinto:
        print(' '.join(fila))


def encontrar_jugador():
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 'S': 
                return i, j
    return None


def mover_jugador(x, y, nx, ny):
    if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and laberinto[nx][ny] != '#':
        if laberinto[nx][ny] == 'E':
            return True  
        laberinto[x][y] = '.'
        laberinto[nx][ny] = 'S'
    return False


def jugar():
    print("¡Bienvenido al Laberinto!")
    mostrar_laberinto()

    movimientos = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    x, y = encontrar_jugador()

    while True:
        movimiento = input("\nMover (w: arriba, s: abajo, a: izquierda, d: derecha): ").lower()
        if movimiento in movimientos:
            dx, dy = movimientos[movimiento]
            if mover_jugador(x, y, x + dx, y + dy):
                print("\n¡Has encontrado la salida! ¡Ganaste!")
                break
            x, y = encontrar_jugador()
            mostrar_laberinto()
        else:
            print("Movimiento inválido. Usa w, a, s o d.")

jugar()
