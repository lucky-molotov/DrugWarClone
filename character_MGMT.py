import random
name_database = {
    "first_names": [
        "Vinnie", "Sal", "Joey", "Mickey", "Bugsy", "Frankie", "Tony", "Paulie", "Rocco", "Lucky",
        "Jimmy", "Jack", "Al", "Buddy", "Duke", "Billy", "Hank", "Bubba", "Randy", "Rocky"
    ],
    "last_names": [
        "LaRosa", "Esposito", "Morano", "Gambino", "Lucchese", "Bonanno", "Colombo", "Genovese", "Castellano", "Amuso",
        "Johnson", "Smith", "Davis", "Wilson", "Anderson", "Thomas", "Jones", "White", "Brown", "Miller"
    ],
    "nicknames": [
        "The Bull", "The Knife", "The Hammer", "The Enforcer", "The Ace", "The Kid", "The Ghost", "The Shadow", "The Snake", "The Razor",
        "The Duke", "The Outlaw", "The Cleaner", "The Kingpin", "The Tiger", "The Thug", "The Hood", "The Shark", "The Wolf"
    ]
}

class PlayerCharacter:
    def __init__(self, name, nickname, age, inventory):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.inventory = inventory
        
    def __repr__(self):
        return f"Name: {self.name}\nNickname: {self.nickname}\nAge: {self.age}"

    def create_character():
        try:
            name = random.choice(name_database["first_names"]) + " " + random.choice(name_database["last_names"])
            nickname = random.choice(name_database["nicknames"])
            age = random.randint(21, 66)
            character = [name, nickname, age]
            
            if not all(character):
                raise ValueError("Character attributes cannot be empty.")
            
            return character
        except KeyError as e:
            raise KeyError(f"Missing key in name_database: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while creating character: {e}")
    def view_character(character):
        if character is None:
            raise ValueError("Character is None")
        if not isinstance(character, list) or len(character) != 3:
            raise ValueError("Character is not a list of length 3")
        if not isinstance(character[0], str):
            raise ValueError("Name is not a string")
        if not isinstance(character[1], str):
            raise ValueError("Nickname is not a string")
        if not isinstance(character[2], int):
            raise ValueError("Age is not an integer")
        character_view = f"Name: {character[0]}\nNickname: {character[1]}\nAge: {character[2]}"
        return character_view
    
    def save_character(character):
        """
        Saves the character to the text file
        """
        if character is None:
            raise ValueError("Character is None")
        if not isinstance(character, list) or len(character) != 3:
            raise ValueError("Character is not a list of length 3")

        try:
            with open("playerCharacter.txt", "a") as file:
                file.write(f"{character[0]},{character[1]},{character[2]}\n")
        except IOError as e:
            raise IOError(f"An error occurred while saving character: {e}")
    def load_character():
        character_name = str(input("Enter character name: "))
        try:
            with open("playerCharacter.txt", "r") as file:
                for line in file:
                    if character_name in line:
                        character = line.strip().split(",")
                        character = [character[0], character[1], int(character[2])]
                        return character
        except IOError as e:
            raise IOError(f"An error occurred while loading character: {e}")
        except ValueError as e:
            raise ValueError(f"An error occurred while loading character: {e}")

    def delete_character():
        """Deletes the character from the text file"""
        character_name = input("Enter character name: ")
        if not character_name:
            raise ValueError("Character name cannot be empty")
        try:
            with open("playerCharacter.txt", "r") as file:
                lines = file.readlines()
            with open("playerCharacter.txt", "w") as file:
                for line in lines:
                    if character_name not in line:
                        file.write(line)
        except IOError as e:
            raise IOError(f"An error occurred while deleting character: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while deleting character: {e}")
            
class npc:
    def __inti__(self,name,nickname):
        self.name = name
        self.nickname = nickname    
    def __repr__(self):
        return f"Name: {self.name}\nNickname: {self.nickname}"
    def create_npc(type):
        if type == "loan shark":
            name = random.choice(name_database["first_names"]) + " " + random.choice(name_database["last_names"])
            nickname = random.choice(name_database["nicknames"])
            npc = [name,nickname]
        else:
            npc = None
        return npc    