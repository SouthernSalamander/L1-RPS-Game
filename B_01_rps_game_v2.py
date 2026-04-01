import random

# Compares user and comp choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # if the user and computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result

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
- Rock beats scissors
- Paper beats rock
- Scissors beats paper
    """)


# Main routine starts here

# initialize game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

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

    # get user choice
    user_choice = string_checker("Choose R / P / S: ", rps_list)
    print(f"User Choice: {user_choice}")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice: ", comp_choice)

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost/ game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔 It's a tie! 👔👔"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😢😢 You lose... 😢😢"
    else:
        feedback = "👍👍 You won! 👍👍"

    # Set up round feedback and output it user.
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if users are in infinite mode, increase round number
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here
if rounds_played > 0:

    print("\n🏁🏁🏁 Game Over! 🏁🏁🏁")

    # Game History / Statistics area

    # Calculate statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output game history
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        print("\n*** Game History ***")
        for item in game_history:
            print(item)

    # Output game statistics
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"👍Won: {percent_won:.2f}% \t "
          f"😢 Lost: {percent_lost:.2f}% \t "
          f"👔 Tied: {percent_tied:.2f}%")
else:
    print("\nChicken 🐔")
