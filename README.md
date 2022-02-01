# Tic-Tac-Toe

Tic Tac Toe is a Python terminal game, which runs in Code Institute mock terminal on Heroku.

Users can try to beat the computer in this classic Tic Tac Toe game by selecting a row and a column.

![Responsive Mockup](https://github.com/JayKearney/tic-tac-toe/blob/main/views/images/responsive.png)

# How to play

ULTIMATE  Tic Tac Toe is based on the classic paper and pencil game. You can read more about in [Wikipedia]https://en.wikipedia.org/wiki/Tic-tac-toe

In this version, the player enters number 1 or 2 to choose between X or O. 

The computer will be the other letter.

The player can see the empty boxes and select a row and column to choose where the chosen letter will be placed.

The player has no control over what the computer bot chooses, therefore is more dynamic since is like playing with a real person.

The player and the computer take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

# Features

Heroku Deployed Project Running: Game starting:

Player is asked if they want to choosee between X or O:

![Start](https://github.com/JayKearney/tic-tac-toe/blob/main/views/images/start%20of%20program.png)

- Play against the computer
- Shows board
- Accepts user input

![You are O] ()

- Input validation and error- checking:

 - You have to enter both a letter (a,b or c) and number (1,2,3) and in that order

![Invalid Choice](https://github.com/JayKearney/tic-tac-toe/blob/main/views/images/invalid%20choice.png)

- Winner is displayed on the board and output message:

![Bot won](https://github.com/JayKearney/tic-tac-toe/blob/main/views/images/bot%20won.png)

# Process and Logic:

I had helped in a Game Development recently so was aware of the steps before starting to code and I also learned from my previous mistakes.

I started this project coding without thinking through it properly and there errors and code didn't work properly. Therefore I decided to stop and wrote the game logic and steps of what I wanted to achieve and how I would do it. I kept adding into it , always before starting to code a different section. 

Working this way made it much easier to translate it into code since I had a clear idea and steps of what to do. I have transcribed it below:


# THE LOGIC USED IN TIC-TAC-TOE
									

1. First of all, the user is asked to select a mark (X or O). Whichever one they select is assigned to userChoice and the other is assigned to the botMark.

2. Three lists with values [" ", " ", " "] are assigned to a,b and c. This serves as the board of the tic-tac-toe, with separators set to | for aesthetic purpose:

![Board](https://github.com/JayKearney/tic-tac-toe/blob/main/views/images/board.read.me.png)
     
3. User is asked to select a row [A, B, or C], and a column [1, 2 or 3], to place their mark. The selected row name is used as list name ["A" for a, and so on], and the selected column, subtracted by 1, is used as list index.

4. userChoice is set to selected row and column, and a check runs to see whether user has won with this move [checkWin()].

5. If they did not win, then the program checks to see if there are any winning spots on the board for the bot [playOffense()].

6. If none is found, it checks to see if player has any chances of winning in the next move, and if they do, it blocks. [playDefense()]

7. If none is found for that either, it checks for the best spot from which it would have the most advantage. [playRandom()]

8. It then checks if the bot/user has won. If yes, it declares the winner and exits, or else, it repeats the same steps.
 
 
A) Logic for checkwin() -  

A.1. First, it is checked if top-left corner is userChoice. it checks if all values of list a is userChoice are userChoice. If yes, it declares user as winner, else, it checks if index 0 of all lists, then declares winner if true.

A.2. If not, it checks if index 1 of all lists are userChoice. 

A.3 If falses, it checks if top-right corner is userChoice, and if true, if checks index 3 of all lists for userChoice. If yes, it declares winner, else if checks if the diagonal (that is a[2], b[1], c[0]) are userChoice. 

A.4. If none of them are true, it checks if all indexes of list b are userChoice. If yes, it declares winner.

A.5. Else, it checks if all indexes of list c are userChoice, and declares winner. 

A.6. If user has not won, it does the same checks with botMark to see if bot has won.


B) Logic for playOffense() -
   
B.1. It checks if the center of the board (B2 on the board, b[1] for list) is botMark. 
B.1.1. If yes, it checks if top-left is botMark and bottom-right is empty, i.e., a potential winning diagonal. It sets bottom-right to botMark. Else, it checks the opposite - i.e. if bottom-right is botMark and top-left is empty, and sets top-left to botMark
B.1.2. Else, it checks if top-right is botMark and bottom-left is empty, and if not it checks the vice-versa, and sets the empty position to botMark.
B.1.3. If neither of the corners are available for a win, it checks if top-middle is botMark, and bottom-middle empty, and then vice-versa, and sets empty position to botMark. 
B.1.4. If that proves to be impossible as well, it checks if the first spot of row B is botMark and last spot of row A is empty, and vice versa. Sets botMark in empty.

B.2. If previous conditions are false, it checks if top-right corner (A1 in board, a[0] in list) is botMark.
B.2.1. It checks if A2 is botMark and A3 is empty, and sets A3 to botMark. Else, if A3 is botMark and A2 is empty, A2 is set to botMark.
B.2.2. Else, it checks if B1 is botMark and C1 is empty, else it checks if C1 is botMark and B1 is empty, and sets empty to botMark.

B.3. If not, it checks top-right (A3 in board, a[2] in list) for botMark.
B.3.1 If yes, it checks if A2 is botMark and A1 is empty, and sets A1 to botMark if true.
B.3.2. Else, it checks if B2 is botMark and C2 is empty, or vice-versa, and sets the empty to botMark.

B.4. If not, it checks the bottom-right (C3 in board, c[2] in list) for botMark.
B.4.1. If yes, it checks if C2 is botMark and C1 is empty, and vice-versa, and sets the empty one to botMark.

B.5. If not, it checks the bottom-left (C1 in board, c[0] in list) for botMark.
B.5.1. If yes, it checks if B1 is botMark and A1 is empty, and sets A1 to botMark.


C) Logic for playDefense() -

It uses the same logic as playOffense, except, it checks if two spots are userChoice (instead of botMark) and sets the empty spot to botMark to block the potential winning combination for user. 


D) Logic for playRandom() - 

D.1. It checks if center is available, as that provides most winning combinations (4 combinations, and thus the greater probability of winning. If yes, it sets center(B2) as botMark.

D.2. If not, it checks if any of the corners are available, as it provides the second most winning combinations (2 combinations, excluding diagonals). The order it checks is (A1 in board, A3, C1, C3).

D.3. If none of the corners are available, it goes for the middles. They offer only 1 winning combination. The order is (A2, B1, B3, C2)

Deployed Project:

Heroku Main Deployment:

User Stories:
This is designed to be a one player game of Tic Tac Toe, to be played against the computer.

# Testing:

 - I have tested in [Online Python] https://www.online-python.com/
 - Tested it in my local terminal and the Code Institute Heroku Terminal

 # Validator Testing

 - Passed the code through a PEP8 linter and confirmed there are no problems: (pep8)

 # Bugs

- I had bugs at the beginning when trying to create the Board using a dictionary, when I had taken a different approach. I pivoted and wrote it in paper first. Bugs were fixed since code was changed.
- I also had indentation erros and wrong numbers entered that were fixed.
- Fixed No new lines error in pep8.
- Error if entering nothing during the initial mark choice (X or O): Fix:  Entered a try-except clause inside a while loop to capture any exceptions (invalid inputs) and run loop again in case of exceptions. Breaks out of loop in case no exceptions are found. 
- Error if entering invalid input or empty input during row and column choice: Fix: Entered a try-except clause inside while loop, just like the first bug's fix, and checked if input is in 1,2,3 (for column) or a,b,c (for rows). If true, the loop breaks, else it runs again.


# Unfixed Bugs

Large empty space on the top.

# Deployment

Used template from Code Institute to allow python backend application to have a pre-built front-end to allow ease of running for the user

Followed Code Institute instructions for Deployment

Enter \n for input before deploying

Updated requirements.txt file using terminal command: pip3 freeze > requirements.txt

Heroku uses this file to deploy used requirements.txt file to record dependencies

Heroku was used to deploy site:

Navigated to Heroku dashboard: https://dashboard.heroku.com/apps

Clicked on Create new app

Named app uniquely -set region to Europe

Clicked create app

Used Settings tab to set settings

Clicked Reveal Config vars - to set configuration variables - no private credentials needed to set up project as no CREDS.json file used

Variable PORT was set to 8000

Clicked Add buildpack to add further dependencies outside of requirements.txt file

Clicked python and Save changes

path: heroku/python

Clicked nodejs and Save changes

path: heroku/nodejs

Then used Deploy tab

Selected GitHub from deployment method

Clicked Connect to GitHub

Searched for GitHub Repository name

Clicked Search and Connect


# Credits

[A beginner's guide to Python variables](https://www.simplilearn.com/tutorials/python-tutorial/python-variables)

[Python functions](https://www.tutorialspoint.com/python/python_functions.htm)

Else if logic : Taken from Code institute

[Elif Game logic inspiration](https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/)

Python for Dummies Book

[Winning elif combinations](https://stackoverflow.com/questions/59625685/i-need-winning-combinations-for-tic-tac-toe-or-at-least-some-hints-tips)

[While true](https://realpython.com/python-while-loop/)

[Removed dictionary as Board](https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries-70ab8ab49a19)

Code Institute for the deployment terminal

Wikipedia for the details of the Tic Tac Toe game


