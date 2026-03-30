# functions go here

def int_check(to_check):

    """Asks user for game goal and makes sure it's above or equal to 13"""

    while True:

        #check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                return "invalid"
            else:
                return response

        except ValueError:
            return "invalid"

while True:
    rounds_number = int_check(input("Number of rounds? "))

    if rounds_number == "infinite":
        print("infinite mode selected")
        break
    elif rounds_number == "invalid":
        print("Please enter an integer that is 1 or more")
    else:
        print(f"round number selected: {rounds_number}")
        break

print("\nProgram continues...")