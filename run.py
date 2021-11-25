from random import randint
import sys

# Defining some variables
empty = " "
a = [empty, empty, empty]
b = [empty, empty, empty]
c = [empty, empty, empty]
# ^^ Rows of the Tic Tac Toe board
win = 0

# Defining Functions


def userMarkChoose():  # Whether user wants X or O
    print ("Do you want to use X[1] or O[2]?")
    choice = int(input("Your Choice (1/2):\n "))
    return choice


def placeMark():
    global a
    global b
    global c
    row = input("Please select a row [a,b,c]:\n ")
    col = int(input("Please select a column [1,2,3]:\n "))
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
            c[0] = botMark




