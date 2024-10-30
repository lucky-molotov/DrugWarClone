import random
gangster_database = {
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
    MIN_HEALTH = 0

    def __init__(self, first_name: str,last_name: str,nickname: str, health: int, weapon: str, currency: int, inventory: list, location: str):
        if health <= 0:
            raise ValueError("Health must be a positive number")

        self.name = first_name
        self.lastname = last_name
        self.nickname = nickname
        self.health = health
        self.max_health = health
        self.min_health = self.MIN_HEALTH
        self.weapon = weapon
        self.currency = currency
        self.inventory = inventory
        self.location = location
    def __str__(self):
        """Returns a string representation of the player's name."""
        return self.name

    def __repr__(self):
        """Returns a string representation of the player's state."""
        return f"Player(name={self.name},lastname={self.lastname}, nickname={self.nickname} , health={self.health}, weapon={self.weapon}, currency={self.currency}, inventory={len(self.inventory)} items({self.inventory}), location={self.location})"

    def is_alive(self):
        """Returns True if the player is alive, False otherwise."""
        return self.health > 0

    def is_dead(self):
        """Returns True if the player is dead, False otherwise."""
        return self.health <= 0

    def take_damage(self, damage: int):
        """
        Reduces the player's health by the given amount of damage.

        Args:
            damage (int): The amount of damage to apply.

        Returns:
            int: The player's updated health.
        """
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self.health -= damage
        self.health = max(self.min_health, min(self.health, self.max_health))
        return self.health
    

def create_gangster():
    first_name = random.choice(gangster_database["first_names"])
    last_name = random.choice(gangster_database["last_names"])
    nickname = random.choice(gangster_database["nicknames"])
    return first_name, last_name, nickname
