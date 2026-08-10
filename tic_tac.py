# Tic Tac Toe Game
# 2 Player Console Game

def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, player):

    # Rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True

    if board[3] == player and board[4] == player and board[5] == player:
        return True

    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # Columns
    if board[0] == player and board[3] == player and board[6] == player:
        return True

    if board[1] == player and board[4] == player and board[7] == player:
        return True

    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # Diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True

    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


def play_game():

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    player = "X"

    for turn in range(9):

        display_board(board)

        print("Player " + player + "'s turn")

        while True:

            try:
                position = int(input("Enter position (1-9): "))

                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9.")
                    continue

                if board[position - 1] == "X" or board[position - 1] == "O":
                    print("This position is already occupied.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        board[position - 1] = player

        # Check winner
        if check_winner(board, player):
            display_board(board)
            print("Player " + player + " wins!")
            return

        # Change player
        if player == "X":
            player = "O"
        else:
            player = "X"

    # Draw
    display_board(board)
    print("Game Draw!")


# Main program
while True:

    print("===== TIC TAC TOE =====")

    play_game()

    again = input("Do you want to play again? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for playing!")
        break