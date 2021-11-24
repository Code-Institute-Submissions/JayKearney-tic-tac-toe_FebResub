
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