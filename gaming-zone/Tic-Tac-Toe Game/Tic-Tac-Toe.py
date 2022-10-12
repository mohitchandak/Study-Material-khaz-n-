board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

initBoard = [
    ["0,0", "0,1", "0,2"],
    ["1,0", "1,1", "1,2"],
    ["2,0", "2,1", "2,2"],
]

winner = "-"


def isBoardFull():
    numDash = 9
    for i in board:
        for j in i:
            if j != "-":
                numDash = numDash - 1
    return numDash


def printBoard():
    for i in board:
        print(i, end="\n")
    print("\n")


def checkWin():
    # Check horizontal win
    winner = "-"

    for i in board:
        winner = i[0]
        for j in i:
            if j != winner:
                winner = "-"
                break
        if winner != "-":
            return winner

    # Check vertical win
    winner = "-"

    for i in range(3):
        winner = board[0][i]
        for j in range(0, 3):
            if winner != board[j][i]:
                winner = "-"
                break
        if winner != "-":
            return winner

    # Check diagonal win
    winner = board[0][0]

    for i in range(3):
        for j in range(3):
            if winner != board[i][i]:
                winner = "-"
                break
    if winner != "-":
        return winner

    winner = board[0][2]

    for i in range(3):
        for j in range(3):
            if i + j == 2:
                if winner != board[i][j]:
                    winner = "-"
                    break
    if winner != "-":
        return winner


def startGame():

    print(f"👏👏\tWelcome to the Tic-Tac-Toe Game\t👏👏\n\n")

    for i in initBoard:
        print(i)

    print("\n")

    player1Name = str(input("Enter your name : (player 1 - x) : "))
    player2Name = str(input("Enter your name : (player 2 - o) : "))

    print("\n")

    for i in range(0, 9):
        player1Place = str(input(f"Enter your position : ({player1Name}) : "))
        player1Place = player1Place.split(",")

        if board[int(player1Place[0])][int(player1Place[1])] == "-":
            board[int(player1Place[0])][int(player1Place[1])] = "x"
        else:
            print("Invalid Position!!!")

        printBoard()

        winner = checkWin()
        if winner == "x":
            print(f"Player : {player1Name} with symbol 'x' is the winner!!!")
            printBoard()
            break
        elif winner == "o":
            printBoard()
            print(f"Player : {player2Name} with symbol 'o' is the winner!!!")
            break
        elif isBoardFull() == 0:
            print("Game Tied!!!\n")
            break

        player2Place = str(input(f"Enter your position : ({player2Name}) : "))
        print("\n")
        player2Place = player2Place.split(",")

        if board[int(player2Place[0])][int(player2Place[1])] == "-":
            board[int(player2Place[0])][int(player2Place[1])] = "o"
        else:
            print("Invalid Position!!!")

        printBoard()

        winner = checkWin()
        if winner == "x":
            print(f"Player : {player1Name} with symbol 'x' is the winner!!!\n")
            printBoard()
            break
        elif winner == "o":
            print(f"Player : {player2Name} with symbol 'o' is the winner!!!\n")
            printBoard()
            break
        elif isBoardFull() == 0:
            print("Game Tied!!!\n")
            break


if __name__ == "__main__":
    startGame()
