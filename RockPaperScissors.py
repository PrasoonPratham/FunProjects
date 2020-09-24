from random import randint

list = ['r','p','s']

computer = list[randint(0,2)]

#Player var declared
player = False

#ASCII art for rock,paper and scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
line = "****************************************"

#Game Logic
while player == False:
    player = input("Rock, Paper, Scissors? (r/p/s)")
    if player == computer:
        print("Tie!")
    elif player == "r":
        if computer == "p":
            print(line)
            print("You lose!"+ paper)
            print("covers", rock)
            print(line)
        else:
            print(line)
            print("You win!" + rock) 
            print("smashes" + scissors)
            print(line)
    elif player == "p":
        if computer == "s":
            print(line)
            print("You lose!" + scissors) 
            print("cut" + paper)
            print(line)
        else:
            print(line)
            print("You win!" + paper) 
            print("covers"+ rock)
            print(line)
    elif player == "s":
        if computer == "Rock":
            print(line)
            print("You lose..." + rock )
            print("smashes" + scissors)
            print(line)
        else:
            print(line)
            print("You win!" + scissors) 
            print("cut" + paper)
            print(line)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = list[randint(0,2)]









# from random import randint

# #create a list of play options
# t = ["Rock", "Paper", "Scissors"]

# #assign a random play to the computer
# computer = t[randint(0,2)]

# #set player to False
# player = False

# while player == False:
# #set player to True
#     player = input("Rock, Paper, Scissors?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "cut", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose...", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("That's not a valid play. Check your spelling!")
#     #player was set to True, but we want it to be False so the loop continues
#     player = False
#     computer = t[randint(0,2)]