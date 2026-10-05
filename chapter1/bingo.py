# imports and global vars
import random

MIN_NUM = 1
MAX_NUM = 10
# max_guess_count = 3


# generate a random num
def generate_random_num():
    return random.randint(MIN_NUM,MAX_NUM)


# get user input as guess
def get_user_input():
    print(f"ur number should be between {MIN_NUM}-{MAX_NUM}")
    while True:
        try:
            user_input = int(input("enter ur guess: "))
            if user_input not in range(1,11):
                print("Ur Number not valid!")
                continue
        except ValueError:
            print("Error: Enter a valid number")
        else:
            return user_input


# check guessed num
def check_guessed_num(userinput, randomnum):
    return userinput == randomnum
    

# main func for run app
def main():
    max_guess_count = 3
    random_num = generate_random_num()
    print(f"random num is {random_num}")
    while max_guess_count > 0 :
        user_input = get_user_input()
        if check_guessed_num(user_input, random_num):
            print("Bingooo!")
            break
        max_guess_count -= 1
        print(f"guesses left: {max_guess_count}")
        
    else:
        print("you couldnt guess the num. GameOver")
        
        
if __name__ == "__main__":
    main()