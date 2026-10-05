# import and global variables
import random
USER_CHOICES = ("rock", "paper", "scissor") # tuple is not changeable


# create function to get user input
def get_user_input():
    user_input = input("Enter your choice (rock, paper, scissor): ").lower()
    while user_input not in USER_CHOICES:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissor): ").lower()
    return user_input


# create function to get pc input
def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print(f"pc choice was: {pc_choice}")
    return pc_choice
    

# compare and determine which one is the winner
def determine_winner(user_choice, pc_choice):
    if user_choice == pc_choice:
        print("It's a tie!") 
    elif (user_choice == "rock" and pc_choice == "scissor") \
        or (user_choice == "paper" and pc_choice == "rock") \
        or(user_choice == "scissor" and pc_choice == "paper"):
        print("You win!") 
    else:
        print("PC wins!") 
    

# create a main function as a runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)
    print("end of program")

# make an iteration for doing the game as much as we need
answer = 'y'
while answer == "y":
    main()
    answer = input("do u want to continue? (y/n): ")