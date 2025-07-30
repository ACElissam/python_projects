import random
import config


def check_winnings(columns, lines, bet, values):
    """
    Calculate the winnings based on the slot machine results.

    This function checks each line of the slot machine columns to see if there are
    matching symbols. If a line has matching symbols, it calculates the winnings
    based on the bet and the value of the symbol.

    Args:
        columns (list): A list of columns, where each column contains symbols for each row
        lines (int): The number of lines to check for winnings
        bet (int): The amount bet per line
        values (dict): A dictionary mapping symbols to their values

    Returns:
        int: The total winnings from the spin
    """
    winnings = 0
    winning_lines = []
    lost_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                lost_lines.append(line + 1)
                # If any symbol in the line does not match, break out of the loop
                break
        
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines, lost_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random slot machine spin.

    This function creates a slot machine spin by randomly selecting symbols
    for each column and row based on the provided symbol distribution.

    Args:
        rows (int): Number of rows in the slot machine
        cols (int): Number of columns in the slot machine
        symbols (dict): Dictionary mapping symbols to their count/frequency

    Returns:
        list: A list of columns, where each column is a list of symbols
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(colums):
    """
    Display the slot machine results in a formatted grid.

    This function prints the slot machine spin results in a visual format
    with symbols separated by vertical bars (|) to represent the slot machine grid.

    Args:
        colums (list): A list of columns, where each column contains symbols for each row
    """
    for row in range(len(colums[0])):
        for i, column in enumerate(colums):
            if i != len(colums) - 1:
                print(column[row], end="  |  ")
            else:
                print(column[row], end="")
        print()


def deposit():
    """
    Set the function to deposit money
    This function will ask the user to input an amount to deposit
    It will validate the input to ensure it is a positive integer
    If the input is valid, it will return the amount deposited
    If the input is invalid, it will prompt the user to try again
    Returns:
        int: The amount deposited by the user
    """
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"You have successfully deposited ${amount}.")
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return amount


def get_number_of_lines():
    """
    get_number_of_lines():

    This function prompts the user to enter the number of lines they want to bet on.
    It validates the input to ensure it is a positive integer and does not exceed MAX_LINES.
    Returns:
        int: The number of lines the user wants to bet on.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{config.MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= config.MAX_LINES:
                print(f"You have chosen to bet on {lines} lines.")
                return lines
            else:
                print(f"Please enter a number between 1 and {config.MAX_LINES}.")
        else:
            print("Invalid input. Please enter a numeric value.")


def get_bet():
    """
    get_bet():

    This function prompts the user to enter a bet amount.
    It validates the input to ensure it is a positive integer and within the range of MIN_BET and MAX_BET.
    Returns:
        int: The bet amount chosen by the user.
    """
    while True:
        bet = input(f"Enter your bet amount (${config.MIN_BET}-${config.MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if config.MIN_BET <= bet <= config.MAX_BET:
                print(f"You have placed a bet of ${bet}.")
                return bet
            else:
                print(
                    f"Please enter a bet between ${config.MIN_BET} and ${config.MAX_BET}."
                )
        else:
            print("Invalid input. Please enter a numeric value.")


def spin(balance):
    """
    Execute a single spin of the slot machine.

    This function handles the complete spin process including getting the number of lines,
    bet amount, validating sufficient balance, performing the spin, calculating winnings,
    and returning the net result (winnings minus total bet).

    Args:
        balance (int): The player's current balance

    Returns:
        int: The net result of the spin (winnings - total_bet)
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is ${balance}"
            )
        else:
            break
    print(
        f"You are betting ${total_bet} on {lines} lines. Your total bet is currently equal to ${total_bet}."
    )
    print(balance, lines)
    slots = get_slot_machine_spin(config.ROWS, config.COLS, config.SYMBOLS_COUNT)
    print_slot_machine(slots)
    winnings, winnig_lines,lost_lines = check_winnings(slots, lines, bet, config.SYMBOL_VALUES)
    print(f"You won ${winnings}")
    print(
        f"You won on lines {', '.join(map(str, winnig_lines))}"
        if winnig_lines
        else f"You lost with lines {', '.join(map(str, lost_lines))}"
    )
    return winnings - total_bet


def main():
    """
    Main function that runs the slot machine game.

    This function controls the overall game flow including initial deposit,
    game loop for spins, balance management, and game termination conditions.
    The game continues until the player quits or runs out of money.
    """
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}.")
        answers = input("Press Enter to spin or 'q' to quit: ")
        if answers.lower() == "q":
            print(f"Thank you for playing! Your final balance is ${balance}.")
            break
        balance += spin(balance)
        if balance <= 0:
            print("You have run out of money! Game over.")
            break
    print(f"Your final balance is ${balance}. Thank you for playing!")


main()
"""
To add documentation to a function, simply write a multi-line comment
using triple quotes right after defining the function.
===============================================

To view the documentation, use the help() function or display the __doc__ attribute of the function.
===============================================
Example:
help(deposit)
or
print(deposit.__doc__)
"""
