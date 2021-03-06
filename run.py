from random import randint
import sys


# Logic begins here
def main():
    # Defining some variables
    global empty
    empty = " "
    global a
    a = [empty, empty, empty]
    global b
    b = [empty, empty, empty]
    global c
    c = [empty, empty, empty]
    # ^^ Rows of the Tic Tac Toe board
    global win
    win = 0
    global userChoice
    global botMark
    while True:
        userChoice = userMarkChoose()
        # ^ Ask user's choice and set bot's mark accordingly
        if userChoice == 1:
            print("YOU ARE X!")
            userChoice = "X"
            botMark = "O"
            break
        elif userChoice == 2:
            userChoice = "O"
            botMark = "X"
            break
        else:
            print("\nInvalid choice, please try again!\n")
            continue

    while True:  # to keep the program looping until someone wins
        print("\n"*20 + "YOU ARE "+userChoice+"!\n\n\n         1   2   3")
        print("   a  ", *a, sep=" | ", end=" ")
        print("|")
        print("      ----------------")
        print("   b  ", *b, sep=" | ", end=" ")
        print("|")
        print("      ----------------")
        print("   c  ", *c, sep=" | ", end=" ")
        print("|")

        print("\n")
        if win == 1:
            print("\nCongratulations! User Won!")
            break
        elif win == 2:
            print("\nBot won! Better luck next time!")
            break
        elif win == 3:
            print("\nIt's a Draw!")
            break
        placeMark()
        # ^Setting user's choice in place.
        win = checkWin()
        if win == 0:
            playOffense()
        win = checkWin()
        # Checking again if anyone won

# Defining Functions


def userMarkChoose():  # Whether user wants X or O
    print ("Do you want to use X[1] or O[2]?")
    while True:
        try:
            choice = int(input("Your Choice (1/2): "))
            break
        except:
            continue
    return choice


def placeMark():
    global a
    global b
    global c
    row = ""
    while True:
        row = input("Please select a row [a, b, c]: ")
        if row == "" or row not in ["a", "b", "c"]:
            print("\nPlease enter a valid row.")
            continue
        else:
            break
    while True:
        try:
            col = int(input("Please select a column [1,2,3]: "))
            if col in [1, 2, 3]:
                break
            else:
                print("\nPlease enter a valid column.")
                continue
        except:
            print("\nPlease enter a valid column.")
            continue
    col = col-1
    if row.upper() == "A":
        if a[col] == empty:
            a[col] = userChoice
        else:
            print("Spot already taken. Please try again.")
            placeMark()
    elif row.upper() == "B":
        if b[col] == empty:
            b[col] = userChoice
        else:
            print("Spot already taken. Please try again.")
            placeMark()
    elif row.upper() == "C":
        if c[col] == empty:
            c[col] = userChoice
        else:
            print("Spot already taken. Please try again,")
    else:
        print("Oops. Invalid choice! Please try again. ")
        placeMark()


def checkWin():  # Did bot or user win
    win = 0
    if a[0] == userChoice:
        if a[1] == userChoice and a[2] == userChoice:
            win = 1  # 1 if user wins
        elif b[0] == userChoice and c[0] == userChoice:
            win = 1
        elif b[1] == userChoice and c[2] == userChoice:
            win = 1
    if a[1] == userChoice:
        if b[1] == userChoice and c[1] == userChoice:
            win = 1
    if a[2] == userChoice:
        if b[2] == userChoice and c[2] == userChoice:
            win = 1
        elif b[1] == userChoice and c[0] == userChoice:
            win = 1
    if b[0] == userChoice and b[1] == userChoice and b[2] == userChoice:
        win = 1
    if c[0] == userChoice and c[1] == userChoice and c[2] == userChoice:
        win = 1

    if win != 1:  # if user did not win, check for bot's win

        if a[0] == botMark:
            if a[1] == botMark and a[2] == botMark:
                win = 2  # 1 if user wins
            elif b[0] == botMark and c[0] == botMark:
                win = 2
            elif b[1] == botMark and c[2] == botMark:
                win = 2
        if a[1] == botMark:
            if b[1] == botMark and c[1] == botMark:
                win = 2
        if a[2] == botMark:
            if b[2] == botMark and c[2] == botMark:
                win = 2
            elif b[1] == botMark and c[0] == botMark:
                win = 2
        if b[0] == botMark and b[1] == botMark and b[2] == botMark:
            win = 2
        if c[0] == botMark and c[1] == botMark and c[2] == botMark:
            win = 2

    if empty not in a and empty not in b and empty not in c:
        win = 3

    return win


def playOffense():
    global a
    global b
    global c
    moved = False
    if not moved and b[1] == botMark:
        if a[0] == botMark and c[2] == empty:
            c[2] = botMark
            moved = True
        elif c[2] == botMark and a[0] == empty:
            a[0] = botMark
            moved = True
        elif a[2] == botMark and c[0] == empty:
            c[0] = botMark
            moved = True
        elif c[0] == botMark and a[2] == empty:
            a[2] = botMark
            moved = True
        # ^Checking if center-corner combinations can give win.
        elif a[1] == botMark and c[1] == empty:
            c[1] = botMark
            moved = True
        elif c[1] == botMark and a[1] == empty:
            a[1] = botMark
            moved = True
        elif b[0] == botMark and b[2] == empty:
            b[2] = botMark
            moved = True
        elif b[2] == botMark and b[0] == empty:
            b[0] = botMark
            moved = True
        # ^Checking if center-center can give bot win
    if not moved and a[0] == botMark:
        if a[1] == botMark and a[2] == empty:
            a[2] = botMark
            moved = True
        elif a[2] == botMark and a[1] == empty:
            a[1] = botMark
            moved = True
        elif b[0] == botMark and c[0] == empty:
            c[0] = botMark
            moved = True
        elif c[0] == botMark and b[0] == empty:
            b[0] = botMark
            moved = True
    # ^All upperleft corner combinations
    if not moved and a[2] == botMark:
        if a[1] == botMark and a[0] == empty:
            a[0] = botMark
            moved = True
        elif b[2] == botMark and c[2] == empty:
            c[2] = botMark
            moved = True
        elif c[2] == botMark and b[2] == empty:
            b[2] = botMark
            moved = True
    # ^All upperright combinations
    if not moved and c[2] == botMark:
        if c[1] == botMark and c[0] == empty:
            c[0] = botMark
            moved = True
        elif c[0] == botMark and c[1] == empty:
            c[1] = botMark
            moved = True
    # ^All bottomright combinations
    if not moved and c[0] == botMark:
        if b[0] == botMark and a[0] == empty:
            a[0] = botMark
            moved = True
    # ^All bottomleft combinations
    playDefense(moved)


def playRandom(moved):
    global a
    global b
    global c
    if not moved:
        if b[1] == empty:
            b[1] = botMark
        elif a[0] == empty:
            a[0] = botMark
        elif a[2] == empty:
            a[2] = botMark
        elif c[0] == empty:
            c[0] = botMark
        elif c[2] == empty:
            c[2] = botMark
        elif (a[0] == botMark or a[2] == botMark) and a[1] == empty:
            a[1] = botMark
        elif (a[0] == botMark or c[0] == botMark) and b[0] == empty:
            b[0] = botMark
        elif(a[2] == botMark or c[2] == botMark) and b[2] == empty:
            b[2] = botMark
        elif(c[2] == botMark or c[0] == botMark) and c[1] == empty:
            c[1] = botMark


def playDefense(moved):
    # Check if user has any winning combinations and block.
    global a
    global b
    global c
    if not moved and b[1] == userChoice:
        if a[0] == userChoice and c[2] == empty:
            c[2] = botMark
            moved = True
        elif a[1] == userChoice and c[1] == empty:
            c[1] = botMark
            moved = True
        elif a[2] == userChoice and c[0] == empty:
            c[0] = botMark
            moved = True
        elif b[0] == userChoice and b[2] == empty:
            b[2] = botMark
            moved = True
        elif b[2] == userChoice and b[0] == empty:
            b[0] = botMark
            moved = True
        elif c[0] == userChoice and a[2] == empty:
            a[2] = botMark
            moved = True
        elif c[1] == userChoice and a[1] == empty:
            a[1] = botMark
            moved = True
        elif c[2] == userChoice and a[0] == empty:
            a[0] = botMark
            moved = True
        # ^All combinations that involve the center checked.
    if not moved and a[0] == userChoice:
        if a[1] == userChoice and a[2] == empty:
            a[2] = botMark
            moved = True
        elif a[2] == userChoice and a[1] == empty:
            a[1] = botMark
            moved = True
        elif b[0] == userChoice and c[0] == empty:
            c[0] = botMark
            moved = True
        elif c[0] == userChoice and b[0] == empty:
            b[0] = botMark
            moved = True
            # ^Upperleft corner combinations checked
    if not moved and a[2] == userChoice:
        if a[1] == userChoice and a[0] == empty:
            a[0] = botMark
            moved = True
        elif b[2] == userChoice and c[2] == empty:
            c[2] = botMark
            moved = True
        elif c[2] == userChoice and b[2] == empty:
            b[2] = botMark
            moved = True
        # ^All Upper-right corner combinations checked
    if not moved and c[0] == userChoice:
        if b[0] == userChoice and a[0] == empty:
            a[0] = botMark
            moved = True
        elif c[1] == userChoice and c[2] == empty:
            c[2] = botMark
            moved = True
        elif c[2] == userChoice and c[1] == empty:
            c[1] = botMark
            moved = True
        # ^All Lowerleft corner combinations checked
    if not moved and c[2] == userChoice:
        if c[1] == userChoice and c[0] == empty:
            c[0] = botMark
            moved = True
        elif b[2] == userChoice and a[1] == empty:
            a[1] = botMark
            moved = True
        # ^All lower-right corner combinations checked
    if not moved and a[1] == userChoice:
        if c[1] == userChoice and b[1] == empty:
            b[1] = botMark
            moved = True
        if b[1] == userChoice and c[1] == empty:
            c[1] == empty
    playRandom(moved)
    # if there is nothing to defend, place at advantageous spot

if __name__ == "__main__":
    main()
