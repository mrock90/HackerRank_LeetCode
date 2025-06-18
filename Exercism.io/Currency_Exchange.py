"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    # Thought process:
    #The problem asks us to find how much foreign currency can be ontained
    # If 1 EUR costs 1.20 USD, then 120 USD will give 120 / 1.20 EUR
    # This is a direct dvidion of the budget by the exchange rate
    # The parameters are floats, and the return type is float, so standard division is appropriate
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    # Thought Process:
    # This is a simple calculation of the remaining funds
    # If you start with 'budget' and use 'exchange_value', the amount is the difference 
    # Both inputs are floats, and the return type is float, so direct subtraction is correct
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    # Thought Process:
    # We need to find the total Value from a given number of bills of a certain denomination
    # This is straightforward multiplication. If you have 5 bills of 10 units each, the total is 5 * 10 = 50
    # The problem specifies integer inputs and on integer return, so standard multiplication works perfectly
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    # Thought Process:
    # The key here is "whole bills" and "rounding down"
    # Python's integer dividion operator '//' is desigend precisely for this
    # For positive numbers, '//' performs division and then floors the result (rounds down to the nearest whole integer)
    # Example: 106.25 // 10 results in 10, not 10.625. This perfectly mataches the requirement
    # The result must be an int, which '//' already provides
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    # Thought process:
    # We need to find the remainder after dividing the 'anount' by the 'denomination'
    # Python's modulo operator '%' is the perfect tool for this
    # Example: 106.25 % 10 results in 6.25. This is the amount that is 'left over' after taking out the largest possible number of whole 10-unit bills
    # The return type is float, which '%' will correctly provide if 'amount' is a float
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Thought process:
    # Step-by-step calculation breadkdown:

    # Step1: Convert the spread percentage to a decimal
    # Rationale: The problem states "spread" is the percentage taken as an exchange fee, written as an integer
    # It needs to be converted to decimal by dividing it by 100
    spread_decimal = spread / 100.0 # Using 100.0 ensures float division

    # Step2: Calculate the adjuted exchange rate
    # Rationale: The problem explicitly states "if 1.00 EUR == 1.20 USD and the spread is 10, the actual exchange rate will be 1.00 EUR == 1.32 USD because 10% of 1.20 0.12, and this additional fee is added to the exchange
    # So, the fee amount is exchange_rate * spread, and thisiis added to the original rate
    adjusted_exchange_rate = exchange_rate + (exchange_rate * spread_decimal)

    # Step3: Calculate the total raw amount of foreign surrency Chandler can get with the adjusted rate
    # Rationale: This is the same logic as the 'exchange_money' function, but using the adjusted rate
    # This result mught be a float (e.g., 106.25 foreign units)
    total_foreign_currency_raw = budget / adjusted_exchange_rate

    # Step4: Determine the number of whoel bills Chandler can receive
    # Rationale: The problem states "Remember that the currency denomination is a whole number, and cannot be sub-divided." This means we need to take the floor of the division by denomination, just like in 'get_number_of_bills'
    # We can reuse the logic from 'get_number_of_bills' or implement it directly here
    number_of_whole_bills = int(total_foreign_currency_raw // denomination)

    # Step5: Calculate the totoal valye represented by these whole bills
    # Rationale: NOw that we have the count of whole bills, we multiply it by the denomination to get the total value that Chandler *actually* recieves, excluding any leftover
    # This is effectively using the logic from 'get_value_of_bills'
    value_of_received_bills = number_of_whole_bills * denomination

    # Step 6: Ensure the final return value is an integer
    # Rationale: The problem explicitly states "Returned value should be int type."
    # 'value_of_received_bills' should already be an integer due to the previous steps, but an explicit 'int()' conversion is good practice for safety, or if intermediate float results were kept. Here, it should naturally be an int
    return int(value_of_received_bills)
