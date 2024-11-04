import message_events
from prettytable import PrettyTable

# Create a table with the desired columns and formatting
def player_hud(character, days, debt):
    player_table = PrettyTable(['Days Left', 'Character Name', 'Debt Remaining'])
    character = character
    days = days
    debt = debt
    # Add the data to the table
    player_table.add_row([str(days), character, str(debt)])
    # Print the table
    print(player_table)
def actions_hud():
    actions_table = PrettyTable(['Action', 'Description'])

    # Add the data to the table
    actions_table.add_row(['Visit Loan Shark','Visit the Shark'])

    print(actions_table)