
from random import randint
import sys

    
#Create a dictionary


def printBoard(board):
    print(board['top-left'] + '|'+board['top-center']+'|'+board['top-right'])
    print('-+-+-')
    print(board['mid-left'] + '|'+board['mid-center']+'|' + board['mid-right'])
    print('-+-+-')
    print(board['lower-left'] + '|'+board['lower-center']+'|' + board['lower-right'])

def player_input():

    value = ""

    while not (value == "X" or value == "O"):
        value = input("Please pick a value 'X' or 'O': ")
    return (value)

def goes_first():
    if random.randint(0,1) == 0:
        return "Computer"
    else:
        return "Player"

def empty_check(board, position):
    """Check if a space is empty
            board(list)
            position(int): Between 1 and 9
    """
    return board[position] == " "

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
