def print_board(board):
    """
    Función para imprimir el tablero de juego.

    Descripción:
    Esta función imprime el tablero de juego con el estado actual de las casillas.

    Parámetros:
    - board: lista de listas de cadenas de caracteres. Representa el tablero de juego.

    Devoluciones:
    No devuelve nada. Simplemente imprime el tablero en la consola.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Función para verificar si hay un ganador en el juego.

    Descripción:
    Esta función verifica si hay un ganador comparando las filas, columnas y diagonales del tablero.

    Parámetros:
    - board: lista de listas de cadenas de caracteres. Representa el tablero de juego.

    Devoluciones:
    Devuelve True si hay un ganador, False de lo contrario.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Función principal para ejecutar el juego Tic-Tac-Toe.

    Descripción:
    Esta función ejecuta el juego Tic-Tac-Toe, permitiendo a los jugadores realizar movimientos hasta que haya un ganador.

    Parámetros:
    No tiene parámetros.

    Devoluciones:
    No devuelve nada. Simplemente imprime el tablero final y el mensaje de quién ha ganado.
    """
    # Inicializar el tablero y el jugador actual
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    # Bucle principal del juego
    while not check_winner(board):
        # Imprimir el tablero y solicitar entrada del jugador
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            # Verificar si las coordenadas son válidas
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
            # Verificar si la casilla seleccionada ya está ocupada
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            # Actualizar el tablero con el movimiento del jugador
            board[row][col] = player
            # Cambiar al siguiente jugador
            if player == "X":
                player = "O"
            else:
                player = "X"
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

    # Imprimir el tablero final y el mensaje de ganador
    print_board(board)
    print("Player " + player + " wins!")

# Llamar a la función principal para iniciar el juego
tic_tac_toe()
