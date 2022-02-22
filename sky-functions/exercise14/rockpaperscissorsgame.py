import random

def welcome_message():
    welcome = 'Welcome to the battlefield! \n Choose your weapon!'
    print(welcome)


def player_input():
    player_choice = input("R, P or S? ")
    if player_choice == 'R':
        print("Your weapon is ROCK!")
    elif player_choice == 'P':
        print("Your weapon is PAPER!")
    elif player_choice == 'S':
        print("Your weapon is SCISSORS!")
    else:
        print("Error in selection")
        return player_input()


def computer_input():
    choice = random.randint(0, 3)
    if choice == 0:
        print("The computer's weapon is ROCK!")
    elif choice == 1:
        print("The computer's weapon is PAPER!")
    elif choice == 2:
        print("The computer's weapon is SCISSORS!")


def comparing_moves():
    if (player_move == computer_move):
        print("It's a tie!")
    elif (player_move == 'P' and computer_move == 0):
        print("You win!")
    elif (player_move == 'S' and computer_move == 1):
        print("You win!")
    elif (player_move == 'R' and computer_move == 2):
        print("You win!")
    else:
        print("Computer wins!")

# THE COMPARISON RULES RETURN AN ERROR: EG, USER=PAPER, COMPUTER=SCISSORS BUT 'IT'S A TIE' CAME UP.


hello = welcome_message()
player_move = player_input()
computer_move = computer_input()
result = comparing_moves()




# Would this need to be an overarching loop with everything above nested within??
# def play_again():
#     again = input("Play again? (y/n): ")
#     return hello

#
# for x in play_again() == "n":
#     break


