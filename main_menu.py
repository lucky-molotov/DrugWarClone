# menu.py
import character_MGMT,time,game_loop
player_character = None
class MenuItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.action = None

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        print("Main Menu:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item.name} - {item.description}")
        choice = input("Choose an option: ")
        return int(choice) - 1

def main_menu():
    
    
    while True:
        choice = None
        menu = Menu()
        item1 = MenuItem("New Game", "Starts a new game session with the current player character and an NPC loan shark.")
        item2 = MenuItem("Quit Game","Quits the game")
        menu.add_item(item1)
        menu.add_item(item2)
        choice = menu.display_menu()
        
        if choice == 0:
            game_loop.new_game()
        elif choice == 1:
            quit()
        else:
            print("Invalid choice. Please try again.")



def view_character(player_character):
    """
    Views the current character.

    This function attempts to print the current character's information.
    If the character has not been created yet, it prints an error message
    and goes back to the main menu.

    This function does not return anything, as it is used to display the
    character's information.
    """
    try:
        character_view = f"Name: {player_character.name}\nNickname: {player_character.nickname}\nAge: {player_character.age}"
        print(character_view)
    except AttributeError:
        print("Please create a character first.")
        main_menu()
    time.sleep(2)

def save_character(player_character):
    """
    Saves the current character.

    This function attempts to save the current character to a file.
    If the character has not been created yet, it prints an error message
    and goes back to the main menu.

    This function does not return anything, as it is used to save the
    character's information.
    """
    try:
        character_MGMT.PlayerCharacter.save_character(player_character)
        print("Character saved.")
    except AttributeError:
        print("Please create a character first.")
        main_menu()
    time.sleep(2)

def load_character():
    """
    Loads the current character.

    This function attempts to load the current character from a file.
    If the character has not been created yet, it prints an error message
    and goes back to the main menu.

    This function does not return anything, as it is used to load the
    character's information.
    """
    player_character = character_MGMT.PlayerCharacter.load_character()
    print("Character loaded.")
    time.sleep(2)  
    return player_character

def delete_character():
    """
    Deletes the current character.

    This function attempts to delete the current character from a file.
    If the character has not been created yet, it prints an error message
    and goes back to the main menu.

    This function does not return anything, as it is used to delete the
    character's information.
    """
    try:
        character_MGMT.PlayerCharacter.delete_character()
        print("Character deleted.")
    except AttributeError:
        print("Please create a character first.")
        main_menu()
    time.sleep(2)

def new_game(player_character):
    game_loop.newgame()



main_menu()