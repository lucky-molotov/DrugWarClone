import message_events
from prettytable import PrettyTable

# Create a table with the desired columns and formatting
def player_hud(character, days, monies, debt, inventory):
    player_table = PrettyTable(['Days Left', 'Character Name', 'Current Monies','Debt Remaining'])
    character = character
    days = days
    monies = monies
    debt = debt

    # Add the data to the table
    player_table.add_row([str(days), str(character), str(monies), str(debt)])
    # Print the table
    print(player_table)

def inventory_hud():
    inventory_table = PrettyTable(['Name','Description','Value','Quantity','Grade'])

    print(inventory_table)
def actions_hud():
    actions_table = PrettyTable(['Action', 'Description'])
    # Add the data to the table
    actions_table.add_row(['Visit Loanshark','Consolodate Debt'])
    actions_table.add_row(['---------------','-------------------'])
    actions_table.add_row(['Visit Supplier', 'Buy and Sell Drugs'])
    actions_table.add_row(['---------------','-------------------'])

    print(actions_table)