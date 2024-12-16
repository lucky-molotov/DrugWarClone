import character_MGMT,time,sys,game_loop
def main_menu():
    """
    Displays the main menu of the game, allowing the user to interact with the game or exit.

    The main menu is an infinite loop that displays a list of options to the user, with each option
    corresponding to a function that can be called to perform the desired action. The options are:

    *   C. Create Character: Creates a new character
    *   V. View Character: Views the current character
    *   S. Save Character: Saves the current character
    *   L. Load Character: Loads a saved character
    *   D. Delete Character: Deletes a saved character
    *   N. New Game: Starts a new game
    *   X. Exit: Exits the game

    If the user enters an invalid option, the menu displays an error message and loops back to the
    beginning.

    This function does not return anything, as it is an infinite loop that only breaks when the user
    chooses to exit the game.
    """
    global player_character
    actions = {
        'c': create_character,
        'v': view_character,
        's': save_character,
        'l': load_character,
        'd': delete_character,
        'n': new_game,
        'x': quit
    }

    while True:
       
        print("\nC. Create Character")
        print("V. View Character")
        print("S. Save Character")
        print("L. Load Character")
        print("D. Delete Character")
        print("N. New Game")
        print("X. Exit")

        choice = input("Enter your choice: ").lower()

        action = actions.get(choice)
        if action:
            try:
                action()
            except AttributeError as e:
                print(f"Error: {e}")
                time.sleep(1)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            
def create_character():
    """
    Creates a new character.

    This function creates a new character using the create_character method
    of the PlayerCharacter class and assigns it to the global variable
    player_character. It then prints the character's information and waits
    for 2 seconds before returning.

    This function does not return anything, as it is used to modify the
    global variable player_character.
    """
    global player_character
    player_character = character_MGMT.PlayerCharacter.create_character()
    print(f"Character created.\n{character_MGMT.PlayerCharacter.view_character(player_character)}")
    time.sleep(2)

def view_character():
    """
    Views the current character.

    This function attempts to print the current character's information.
    If the character has not been created yet, it prints an error message
    and goes back to the main menu.

    This function does not return anything, as it is used to display the
    character's information.
    """
    try:
        print(character_MGMT.PlayerCharacter.view_character(player_character))
    except AttributeError:
        print("Please create a character first.")
        main_menu()
    time.sleep(2)

def save_character():
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
    global player_character
    try:
        player_character = character_MGMT.PlayerCharacter.load_character()
        print("Character loaded.")
        print(character_MGMT.PlayerCharacter.view_character(player_character))
    except AttributeError:
        print("Please create a character first.")
        main_menu()
    time.sleep(2)

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

def new_game():
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
        loanshark = character_MGMT.npc.create_npc("loan shark")
        game_loop.new_game(player_character,loanshark)
    except AttributeError:
        print("Please create a character first.")
        main_menu()
    time.sleep(2)