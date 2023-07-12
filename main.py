from coins import USD, ILS

results_list = []


# asks the user what currency he wants to convert
def get_user_input():
    while True:  # validating the users input
        try:
            user_choice = input("Please choose an option (1/2):\n1. Dollars to Shekels\n2. Shekels to Dollars\n")
            assert user_choice in ["1", "2"]
            return user_choice

        except ValueError:
            print("Invalid choice, please try again.")
        except AssertionError:
            print("Invalid choice, please try again.")


# converts USD to ILS
def usd_to_ils():
    while True:  # validating the users input
        try:
            # asks for an amount
            value_to_convert = float(input("Please enter an amount to convert: "))
            assert type(value_to_convert) is float
            break
        except ValueError:
            print("Invalid choice, please try again.")
        except AssertionError:
            print("Invalid choice, please try again.")
    usd = USD()
    # converting to ILS
    converted_value = usd.calculate(value_to_convert)
    results_list.append(converted_value)
    # printing the results
    print(f"{value_to_convert} United States Dollar equals {converted_value} Israeli new shekels.")


# converts ILS to USD
def ils_to_usd():
    while True:  # validating users input
        try:
            # asks for an amount
            value_to_convert = float(input("Please enter an amount to convert: "))
            assert type(value_to_convert) is float
            break
        except ValueError:
            print("Invalid choice, please try again.")
        except AssertionError:
            print("Invalid choice, please try again.")
    ils = ILS()
    # converting to USD
    converted_value = ils.calculate(value_to_convert)
    results_list.append(converted_value)
    # printing the results
    print(f"{value_to_convert} Israeli new shekels equals {converted_value} United States Dollar.")


# checks if user wants to keep playing
def keep_playing():
    while True:  # validating users input
        try:
            # asks the user if he wants to start over
            continue_playing = input("Do you want to start over? (Y/N) ")
            assert continue_playing.lower() in ["y", "n"]
            if continue_playing.lower() == "y":
                print("++++++++++++++++")
                print("Currency converter")
                return True  # program continues
            else:
                return False  # program terminated
        except ValueError:
            print("Invalid choice, please try again.")
        except AssertionError:
            print("Invalid choice, please try again.")


# prints the end screen
# prints all previous results
# writes all results to a text file
def end_screen():
    print("++++++++++++++++\nThanks for using the currency converter\n++++++++++++++++")
    print(f"All the previous results: {results_list}")
    text_file = open("results.txt", "w+")
    text_file.write(f"All the results: {results_list}")
    text_file.close()


def main():
    print("Welcome to currency converter")
    while True:
        # checking the users choice
        currency_choice = get_user_input()
        if currency_choice == "1":  # USD to ILS
            usd_to_ils()
        elif currency_choice == "2":  # ILS to USD
            ils_to_usd()

        # prints previous results
        print(f"Previous results: {results_list}")
        if not keep_playing():  # if the user choose to not start over
            end_screen()  # program terminated
            break


main()
