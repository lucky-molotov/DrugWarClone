# menu.py
import character_MGMT,time,game_test
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
        item1 = MenuItem("Create Character", "Creates a new character.")
        item2 = MenuItem("View Character", "Views the current character's information.")
        item3 = MenuItem("Save Character", "Saves the current character to a file.")
        item4 = MenuItem("Load Character", "Loads the current character from a file.")
        item5 = MenuItem("Delete Character", "Deletes the current character from a file.")
        item6 = MenuItem("New Game", "Starts a new game session with the current player character and an NPC loan shark.")

        menu.add_item(item1)
        menu.add_item(item2)
        menu.add_item(item3)
        menu.add_item(item4)
        menu.add_item(item5)
        menu.add_item(item6)

        choice = menu.display_menu()

        if choice == 0:
            player_character = create_character()
        elif choice == 1:
            view_character(player_character)
        elif choice == 2:
            save_character(player_character)
        elif choice == 3:
            loaded_character = load_character()
            player_character =character_MGMT.PlayerCharacter(loaded_character[0], loaded_character[1], loaded_character[2], loaded_character[3])
            print(player_character)
        elif choice == 4:
            delete_character()
        elif choice == 5:
            new_game(player_character)
        else:
            print("Invalid choice. Please try again.")

def create_character():
    """
    Creates a new character.

    This function creates a new character using the create_character method
    of the PlayerCharacter class and assigns it to the global variable
    player_character. It then prints the character's information and waits
    for 2 seconds before returning.
    """
    player_character = character_MGMT.PlayerCharacter.create_character()
    print(f"Character created.\n{character_MGMT.PlayerCharacter.view_character(player_character)}")
    time.sleep(2)
    return player_character

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
    
    """
    Starts a new game session.

    This function initializes a new game by creating an NPC loan shark 
    and starting the game with the current player character and the 
    created NPC. If the player character has not been created yet, 
    it prints an error message and returns to the main menu.

    This function does not return anything, as it is used to start a
    new game session.
    """
    try:
        if player_character == None:
            print("Please create a character first.")
            main_menu()
        loanshark = character_MGMT.npc.create_npc("loan shark")
        print("Starting new game...")
        game_test.new_game(player_character,loanshark)
        player_character = None
    except AttributeError:
        print("Please create a character first.")
        main_menu()

main_menu()