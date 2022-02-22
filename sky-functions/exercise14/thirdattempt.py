import random

def welcome():
    print('Welcome to the battlefield! \n Choose your weapon!')
    return


def player_choice():
    player_choice = str(input("R, P or S? "))
    if player_choice == 'r':
        print("Your weapon is ROCK!")
    elif player_choice == 'p':
        print("Your weapon is PAPER!")
    elif player_choice == 's':
        print("Your weapon is SCISSORS!")
    return


def computer_move():
    computer_choice = random.randint(0,3)
    if computer_move == 0:
        print("The computer's weapon is ROCK!")
    elif computer_move == 1:
        print("The computer's weapon is PAPER!")
    elif computer_move == 2:
        print("The computer's weapon is SCISSORS!")
    return


while True:
    if (player_choice() == 'p' and computer_move == 1) or (player_choice() == 'r' and computer_move() == 0) or (player_choice() == 's' and computer_move() == 2):
        print("It's a tie!")
    elif (player_choice() == 'r' and computer_move() == 2):
        print("You win!")
    elif (player_choice() == 'p' and computer_move() == 0):
        print("You win!")
    elif (player_choice() == 's' and computer_move() == 1):
        print("You win!")
    elif computer_move():
        print("Computer wins!")
    break


welcome()
player_choice()
computer_move()
print("Thank you for playing!")