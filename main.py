print('Welcome to TicTacToe')


def contin():
    # Contains list of all valid inputs
    board1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    board2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    def display_board():  # Shows the board at each player's turn
        print("", board1[0], "|", board1[1], "|", board1[2], "      ", "a | b | c")
        print("---|---|---", "    ", "---|---|---")
        print("", board1[3], "|", board1[4], "|", board1[5], "      ", "d | e | f")
        print("---|---|---", "    ", "---|---|---")
        print("", board1[6], "|", board1[7], "|", board1[8], "      ", "g | h | i")

    def checkwin():  # Checks whether the game has been won or not
        if (
            (
                board1[0] == board1[1] == board1[2] == "X"
                or board1[0] == board1[1] == board1[2] == "O"
            )
            or (
                board1[3] == board1[4] == board1[5] == "X"
                or board1[3] == board1[4] == board1[5] == "O"
            )
            or (
                board1[6] == board1[7] == board1[8] == "X"
                or board1[6] == board1[7] == board1[8] == "O"
            )
            or (
                board1[0] == board1[3] == board1[6] == "X"
                or board1[0] == board1[3] == board1[6] == "O"
            )
            or (
                board1[1] == board1[4] == board1[7] == "X"
                or board1[1] == board1[4] == board1[7] == "O"
            )
            or (
                board1[2] == board1[5] == board1[8] == "X"
                or board1[2] == board1[5] == board1[8] == "O"
            )
            or (
                board1[0] == board1[4] == board1[8] == "X"
                or board1[0] == board1[4] == board1[8] == "O"
            )
            or (
                board1[2] == board1[4] == board1[6] == "X"
                or board1[2] == board1[4] == board1[6] == "O"
            )
        ):
            return True

    def game():  # Game is Played
        display_board()
        turn = 0  # turn counts the number of turn initially 0

        while True:
            x = input("X's turn. Enter your position: ")
            if x == "q":
                exit()
            while x not in board2:
                x = input("X's turn. Enter valid position: ")
            for i in range(0, len(board2)):
                if board2[i] == x:
                    board1[i] = board2[i] = "X"

            display_board()
            if checkwin():
                print("X won. Congratulations.")
                break

            turn += 1  # After X's turn 1 is added to turn
            if (
                turn == 9
            ):  # When 9 turns are completed and still noone has won the game.
                print("It's a tie match!!")
                break

            y = input("O's turn. Enter your position: ")
            if y == "q":
                exit()
            while y not in board2:
                y = input("O's turn. Enter valid position: ")
            for i in range(0, len(board2)):
                if board2[i] == y:
                    board1[i] = board2[i] = "O"

            display_board()
            if checkwin():
                print("O won. Congratulations.")
                break

            turn += 1  # Again after O's turn 1 is added to turn

    game()


if __name__ == "__main__":
    contin()
    while True:
        cont = input("Do you want to continue(Yes/No)?: ")
        if cont.upper() == "YES" or cont.upper() == "Y":
            contin()
        elif cont.upper() == "NO" or cont.upper() == "N":
            print("Thanks for playing!!")
            break
        else:
            print("Is that a Yes or a No?", end=" ")
