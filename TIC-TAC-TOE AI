import math  # Import the math module for infinity values

def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))  # Join the row elements with " | " and print
        print("-" * 5)  # Print a separator line

def check_winner(board):
    """
    Function to check if there's a winner.
    Returns 'X' or 'O' if there's a winner, otherwise None.
    """
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None  # No winner found

def check_full(board):
    """
    Function to check if the board is full (resulting in a draw).
    Returns True if the board is full, otherwise False.
    """
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm with Alpha-Beta Pruning to determine the best move.
    """
    winner = check_winner(board)
    if winner == 'O':  # AI is 'O'
        return 1
    elif winner == 'X':  # Human is 'X'
        return -1
    elif check_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    """
    Function to determine the best move for the AI using the Minimax algorithm.
    """
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    """
    Main function to handle the game loop.
    The human-player and AI take turns until there's a winner or the board is full.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize an empty board
    human_turn = True  # Human starts first

    while True:
        print_board(board)  # Print the current board state
        winner = check_winner(board)
        if winner:
            print(f"Winner: {winner}")
            break
        if check_full(board):
            print("Draw!")
            break

        if human_turn:
            # Get human player's move
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                human_turn = False
            else:
                print("Cell already taken, try again.")
        else:
            # Get AI's move
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                human_turn = True

if __name__ == "__main__":
    play_game()
