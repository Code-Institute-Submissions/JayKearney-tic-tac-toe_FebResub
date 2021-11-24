Introduction:

This command line project is a Tic Tac Toe game.

Deployed Project:

Heroku Main Deployment:

User Stories:
This is designed to be a one player game of Tic Tac Toe, to be played against the computer.


Credits:

Tutorial Used for Software to make ASCII


Deployment steps:

Used template from Code Institute to allow python backend application to have a pre-built front-end to allow ease of running for the user

Followed Code Institute instructions for Deployment

"Enter \n for input before deploying"

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
