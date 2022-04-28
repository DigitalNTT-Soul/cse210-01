# Author: Dylan Ruppell
# Assignment: W02 Ponder and Prove

# little bit of scaffolding/debug code
def checkpoint(*output):
    in_dev = False
    if in_dev: print("Debug Checkpoint: ", output)

#main body of the code
boardstate = [1,2,3,4,5,6,7,8,9]


def display_board():
    checkpoint(1101, boardstate)
    print("\n{}|{}|{}\n-+-+-\n{}|{}|{}\n-+-+-\n{}|{}|{}\n".format(*boardstate))

def menu(turn):
    checkpoint(1201, turn, boardstate)

    # who's turn is it
    player = ['x','o'][turn % 2]

    # what square has the player chosen?
    choice = input(player + '\'s turn to choose a square (1-9): ')

    # input validation
    try:
        choice = int(choice) - 1
        if not (choice >= 0 and choice <= 8):
            print("The value you have entered is invalid. Please enter a digit *between 1 and 9*.")
            return turn
    except ValueError:
        print("The value you have entered is invalid. Please enter a *digit* between 1 and 9.")
        return turn
    
    if type(boardstate[choice]) is int:
        boardstate[choice] = player
        display_board()
        return turn + 1
    elif type(boardstate[choice]) is str:
        print("That space is already occupied, please try again.")
        return turn

def win_checker():
    checkpoint(1301, boardstate)
    # First Column
    if (boardstate[0] == boardstate[3] and boardstate[3] == boardstate[6]):
        return boardstate[0]
    # Second Column
    elif (boardstate[1] == boardstate[4] and boardstate[4] == boardstate[7]):
        return boardstate[1]
    # Third Column
    elif (boardstate[2] == boardstate[5] and boardstate[5] == boardstate[8]):
        return boardstate[2]
    # First Row
    elif (boardstate[0] == boardstate[1] and boardstate[1] == boardstate[2]):
        return boardstate[0]
    # Second Row
    elif (boardstate[3] == boardstate[4] and boardstate[4] == boardstate[5]):
        return boardstate[3]
    # Third Row
    elif (boardstate[6] == boardstate[7] and boardstate[7] == boardstate[8]):
        return boardstate[6]
    # \ Diagonal
    elif (boardstate[0] == boardstate[4] and boardstate[4] == boardstate[8]):
        return boardstate[0]
    # / Diagonal
    elif (boardstate[2] == boardstate[4] and boardstate[4] == boardstate[6]):
        return boardstate[0]
    # Nobody's won yet
    else:
        return False

def main():
    checkpoint(1000)
    turn = 0
    display_board()
    while turn < 9:
        checkpoint(1001)
        turn = menu(turn)
        win_state = win_checker()
        if win_state:
            print("Congratulations, " + win_state +"! Good game. Thanks for Playing!")
            return
        elif turn == 9:
            print("Tie game! Nice job and Thanks for Playing!")
            return

main()