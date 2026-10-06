# get user input
def get_user_input():
    user_input = input("Enter Ur Word: ")
    return user_input


# check the palindrome
def check_palindrome_word(user_input):
    rev_word = ""
    for char in user_input[::-1]:
        rev_word += char
        
    return rev_word == user_input


# run the app
def main():
    user_word = get_user_input()
    print(check_palindrome_word(user_word))
    
main()
