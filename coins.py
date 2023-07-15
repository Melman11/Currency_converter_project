# this file contains the value of the coins and the functions to calculate them
import requests


# USD currency class
# gets the USD to ILS exchange rate and calculate with the user input
class USD:
    # gives the current value of USD
    def get_value(self):
        # gets exchange rate from API
        try:
            url = 'https://v6.exchangerate-api.com/v6/eebeb3c6802d2aaa07f5c750/pair/USD/ILS'
            response = requests.get(url)
            rate = response.json()['conversion_rate']
            return rate
        # returns default value if API isn't available
        except:
            print("Could not get rate from API, using default rate...")
            return 3.52

    # calculate the USD value with the users input
    def calculate(self, user_input):
        return self.get_value() * user_input


# ILS currency class
# gets the ILS to USD exchange rate and calculate with the user input
class ILS:

    # gives the current value of ILS
    def get_value(self):
        # gets exchange rate from API
        try:
            url = 'https://v6.exchangerate-api.com/v6/eebeb3c6802d2aaa07f5c750/pair/ILS/USD'
            response = requests.get(url)
            rate = response.json()['conversion_rate']
            return rate
        # returns default value if API isn't available
        except:
            print("Could not get rate from API, using default rate...")
            return 0.28

    # calculate the ILS value with the users input
    def calculate(self, user_input):
        return self.get_value() * user_input


# EUR currency class
# gets the ILS to EUR exchange rate and calculate with the user input
class EUR:
    # gives the current value of EUR
    def get_value(self):
        # gets exchange rate from API
        try:
            url = 'https://v6.exchangerate-api.com/v6/eebeb3c6802d2aaa07f5c750/pair/ILS/EUR'
            response = requests.get(url)
            rate = response.json()['conversion_rate']
            return rate
        # returns default value if API isn't available
        except:
            print("Could not get rate from API, using default rate...")
            return 4.23

    # calculate the USD value with the users input
    def calculate(self, user_input):
        return self.get_value() * user_input