def generate_password():
    import string
    import random
    # INPUT: password length
    while True:
        try:
            user_length = int(input('Enter Password Length: '))
            if user_length >= 8:
                break
            else:
                print('Password must be at least 8 characters.')
        except ValueError:
            print('Wrong input, please enter a number.')

    # INPUT: exclude similar characters
    options = ['yes', 'no']
    while True:
        user_choice = input('Exclude Similar Characters? ').lower()
        if user_choice in options:
            break
        else:
            print('Invalid Input, Try Again.')

    # CHARACTER POOL
    char_pool = string.ascii_letters + string.digits + string.punctuation
    my_list = list(char_pool)

    # REMOVE SIMILAR CHARACTERS
    unwanted_list = ['O', '0', 'l', '1']
    filtered_pool = []

    for ch in my_list:
        if ch not in unwanted_list:
            filtered_pool.append(ch)

    # FINAL POOL
    if user_choice == 'yes':
        final_pool = filtered_pool
    else:
        final_pool = my_list

    # PASSWORD GENERATION
    password = ""
    for i in range(user_length):
        ch = random.choice(final_pool)
        password += ch

    # SAVE TO FILE
    with open("Password_Files.txt", "a") as file:
        file.write(password + '\n')
    return password