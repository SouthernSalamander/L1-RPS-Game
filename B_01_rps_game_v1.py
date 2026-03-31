# functions go here

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

# Main routine starts here

# initialize game variables
mode = "regular"
rounds_played = 0


print("💎📄✂️ Rock / Paper / Scissors Game ✂️📄💎")
print()

# instructions

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ", "")

if num_rounds == "":
        mode = "infinite"
        num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if users are in infinite mode, increase round number
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)


# Game loop ends here

# Game History / Statistics area