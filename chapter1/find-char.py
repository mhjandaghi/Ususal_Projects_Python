# get user input
def get_user_input():
    user_input = input("Enter Ur Word: ")
    return user_input

# check count and compare
def check_max_char(user_input):
    max_char = " "
    for u in user_input:
        if user_input.count(u) > user_input.count(max_char):
            max_char = u
    return max_char, user_input.count(max_char)


# run the app
usr = get_user_input()
print(check_max_char(usr))

# Solve without methods
user_input = input("Enter Ur Word: ")
max_char = " "
max_count = 0

for u in user_input:
    count = 0
    for x in user_input:
        if x == u:
            count += 1
    if count > max_count:
        max_char = u
        max_count = count
            
print(max_char,max_count)

