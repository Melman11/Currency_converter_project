from coins import USD, ILS, EUR
import tkinter as tk
import subprocess
results_list = []


# asks the user what currency he wants to convert
def get_user_input():
    while True:  # validating the users input
        try:
            user_choice = input("Please choose an option (1/2):\n1. Dollars to Shekels\n2. Shekels to Dollars\n"
                                "3. Shekels to Euro")
            assert user_choice in ["1", "2", "3"]
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
    result = f"{value_to_convert} USD equals {converted_value} ILS"  # result object
    # appending to the result list
    results_list.append(result)
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
    result = f"{value_to_convert} ILS equals {converted_value} USD"  # result object
    # appending to the result list
    results_list.append(result)
    # printing the results
    print(f"{value_to_convert} Israeli new shekels equals {converted_value} United States Dollar.")


# converts ILS to EUR
def ils_to_eur():
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
    eur = EUR()
    # converting to ILS
    converted_value = eur.calculate(value_to_convert)
    result = f"{value_to_convert} ILS equals {converted_value} EUR"  # result object
    # appending to the result list
    results_list.append(result)
    # printing the results
    print(f"{value_to_convert} Israeli new shekels equals {converted_value} Euro's.")


# checks if user wants to keep playing
def keep_playing():
    while True:  # validating users input
        try:
            # asks the user if he wants to start over
            continue_playing = input("Do you want to start over? (Y/N) ")
            assert continue_playing.lower() in ["y", "yes", "n", "no"]
            if continue_playing.lower() in ["y", "yes"]:
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

    # *optional to also open the file in notepad*
    # filepath = "C:/Users/nivis/PycharmProjects/Currency_converter_project/results.txt"
    # notepad = f"notepad {filepath}"
    # subprocess.run(notepad, shell=True)


def display_file_content():
    file_path = "C:/Users/nivis/PycharmProjects/Currency_converter_project/results.txt"
    with open(file_path, "r") as file:
        text = file.read()
    # create a Tkinter window
    window = tk.Tk()
    window.title("File Content")
    # create a text widget and add it to the window
    text_widget = tk.Text(window)
    text_widget.pack()
    # insert the file content into the text widget
    text_widget.insert(tk.END, text)
    # mainloop
    window.mainloop()


def main():
    print("Welcome to currency converter")
    while True:
        # checking the users choice
        currency_choice = get_user_input()
        if currency_choice == "1":  # USD to ILS
            usd_to_ils()
        elif currency_choice == "2":  # ILS to USD
            ils_to_usd()
        elif currency_choice == "3":  # ILS to EUR
            ils_to_eur()

        # prints previous results
        print(f"Previous results: {results_list}")
        if not keep_playing():  # if the user choose to not start over
            end_screen()  # program terminated
            # display the file content using Tkinter
            display_file_content()
            break


main()
