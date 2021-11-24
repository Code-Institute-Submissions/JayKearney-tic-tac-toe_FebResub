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






#def empty_check(board, position):
    """Check if a space is empty
            board(list)
            position(int): Between 1 and 9
    """
    #return board[position] == " "

#def user_choice(board):
    """Player to choose position. Must be in range of 1-9 where a space is empty
            return(int): Valid position number
    """
    #position = 0
    #while position not in [1,2,3,4,5,6,7,8,9] or not empty_check(board, position):
        #position = int(input('Choose a position (1-9): '))
    #return position

#def place_marker(board, marker, position):
    """Place the marker of the player in the corresponding position on the board
            board(list)
            marker(string): Either 'X' or 'O'
            position(integer): Between 1 and 9
    """
    #loop through dictionary 
    
    #board[position] = marker   




#main

def main():
    print("Welcome to Tic Tac Toe")

    person, computer = '',''

    while True:
        # Set up the board
        board = { 'top-left': ' ', 'top-center': ' ', 'top-rigt': ' ',
                 'mid-left': ' ', 'mid-center': ' ', 'mid-right': ' ',
                 'lower-left': ' ', 'lower-center': ' ', 'lower-right': ' '} 
        player = player_input()

        # Determine who will go first
        turn = goes_first()
        print(turn + " will go first")
