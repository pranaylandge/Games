import random

def name_to_number(name):
    if name =="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name =="paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error Wrong name!")
        return
    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number ==2:
        return "paper"
    elif number ==3:
        return "lizard"
    elif number ==4:
        return "scissors"
    else:
        print("Error Wrong number!")
        return
    
def reps(player_choice):
    print("\n")
    
    print("player chooses + player_choice")
    
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("computer chooses + comp_choise")
    
    difference = player_number - comp_number
    if difference == 0:
        print("Player and computer tie!")
    elif difference == 4 or difference == 3 or difference == -1 or difference == -2:
            print("Computer wins!")
    else:
            print("player wins!")
            
reps(input("Enter youer choise from below:- \n 1)rock \n 2)Spock \n 3)paper \n 4)lizard \n 5)scissors "))

    
    