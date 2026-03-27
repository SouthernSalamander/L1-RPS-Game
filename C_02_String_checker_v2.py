
def string_checker(question, valid_ans=("yes", "no")):

    """Check that users enter a valid word / first
    letter of the word based on a list of options. Defaults to yes / no"""

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for var_item in valid_ans:
            # check if the user response is a word in the list
            if var_item == user_response:
                return var_item

            # check if the user response is the same as
            # the first letter of an item from the list
            elif user_response == var_item[0]:
                return var_item

        # print error if user does not enter something that is valid
        print(error)
        print()

rps_valid = ("rock", "paper", "scissors", "xxx")

while True:
    choose = string_checker("Choose? ", rps_valid)
    print(f"you chose {choose}")
