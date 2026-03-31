import random

# Compares user and comp choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # if the user and computer choice is the same, it's a tie
    if user == comp:
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        result = "lose"

    return result

# Check that users have entered a valid
# option based on a list
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

def int_check(question, exit_code=None):

    """Asks user for game goal and makes sure it's above or equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == exit_code:
            return response

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def instructions():

    """Prints instructions"""
    print("""
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
- Paper beats rock
- Rock beats scissors
- Scissors beats paper
    """)


# Main routine starts here

# initialize game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📄✂️ Rock / Paper / Scissors Game ✂️📄💎")
print()

# ask user if they want instructions and display
want_instructions = string_checker("Do you want to see the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ", "")

if num_rounds == "":
        mode = "infinite"
        num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n*** Round {rounds_played + 1} (Infinite Mode) ***"
    else:
        rounds_heading = f"\n*** Round {rounds_played + 1} of {num_rounds} ***"

    print(rounds_heading)
    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice: ", comp_choice)


    # get user choice
    user_choice = string_checker("Choose R / P / S: ", rps_list)
    print(f"User Choice: {user_choice}")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result} ")

    rounds_played += 1

    # if users are in infinite mode, increase round number
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area