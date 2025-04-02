import random

def get_choices ():
    players_choices=input("enter your choice")
    option= ["rock","paper","scissors"]
    computer_choices= random.choice(options)
    choice={"player":players_choices,"computer":computer_choices}

    return computer_choices

choices= get_choices() 
print (choices) 