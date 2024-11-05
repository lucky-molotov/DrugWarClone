import random
from rich.console import Console
monetary_name = "Crows"
console = Console()
def intro_messages(player, loanshark):


    """
    Prints a random intro message to the console.

    The intro message includes the player's name, the name of the loan shark,
    and a description of the situation. The message is chosen randomly from
    a list of predefined messages.

    Parameters:
    player (str): The player's name.
    loanshark (str): The name of the loan shark.

    Returns:
    None
    """
    def version_1a_intro(player, loanshark):
        """A gritty, high-stakes introduction."""
        console.print(f"[bold red]Old Town's got a new problem...[/bold red]", style="underline")
        console.print(f"You're it. Your debt to {loanshark.name} {loanshark.nickname} is about to catch up with you.")
        console.print(f"Thirty days. That's all you've got to turn things around. After that, the loan shark'll be knocking on your door...")
        console.print(f"The streets are watching, and so are his goons. It's time to make a move or face the consequences.")
        console.print(f"[bold green]You've got a glimmer of hope...[/bold green]")
        console.print(f"You've managed to scrounge up {monetary_name}. It's not much, but it's enough to keep you going for now...")
        console.print(f"Will you be able to navigate the underworld of Old Town and stay one step ahead of your debtors?")


    def version_1b_intro(player, loanshark):
        """A more mysterious introduction."""
        console.print(f"[bold purple]The shadows are closing in...[/bold purple]", style="underline")
        console.print(f"You've been chosen. By the very fabric of Old Town's underworld.")
        console.print(f"Your debt to {loanshark.name} {loanshark.nickname} is a ticking time bomb...")
        console.print(f"Thirty days. That's all you've got to defuse it before things get out of hand.")
        console.print(f"[bold yellow]You've stumbled upon something...[/bold yellow]")
        console.print(f"A cryptic message, hinting at a way to escape your debt. But can you trust it?")
        console.print(f"The streets are full of secrets, and so are his goons. You'll need all your wits about you to survive...")

    def version_1c_intro(player, loanshark):
        """A more fast-paced introduction."""
        console.print(f"[bold orange]Time's running out...[/bold orange]", style="underline")
        console.print(f"You've got a debt to {loanshark.name} {loanshark.nickname}, and it's about to catch up with you.")
        console.print(f"Thirty days. That's all you've got to make some noise, raise some cash...")
        console.print(f"[bold green]You're in this now...[/bold green]")
        console.print(f"You've managed to scrounge up {monetary_name}. It's a start, but it won't be enough on its own.")
        console.print(f"You'll need to move fast, and make some moves. The streets are alive with possibilities...")


    def version_1d_intro(player, loanshark):
        """A more emotional introduction."""
        console.print(f"[bold pink]Your heart is racing...[/bold pink]", style="underline")
        console.print(f"You've been through the wringer, {player.name}. Your debt to {loanshark.name} {loanshark.nickname} is a constant reminder...")
        console.print(f"Thirty days. That's all you've got to turn things around.")
        console.print(f"[bold blue]You've found a glimmer of hope...[/bold blue]")
        console.print(f"You've managed to scrounge up {monetary_name}. It's not much, but it's enough to keep you going for now...")
        console.print(f"Will you be able to find your way out of this darkness, or will the shadows consume you?")


    def version_1e_intro(player, loanshark):
        """A more philosophical introduction."""
        console.print(f"[bold black]The universe is a cruel joke...[/bold black]", style="underline")
        console.print(f"You've been dealt a hand, {player.name}. Your debt to {loanshark.name} {loanshark.nickname} is just the beginning.")
        console.print(f"Thirty days. That's all you've got to find your way in this twisted game...")
        console.print(f"[bold white]You're on the cusp of something...[/bold white]")
        console.print(f"You've managed to scrounge up {monetary_name}. It's a start, but what does it truly mean?")
        console.print(f"The streets are full of meaning, or at least that's what you tell yourself. But can you truly find your place in this chaotic world?")


    random_version = random.randint(1, 5)
    if random_version == 1:
        intro = version_1a_intro(player, loanshark)
    elif random_version == 2:
        intro = version_1b_intro(player, loanshark)
    elif random_version == 3:
        intro = version_1c_intro(player, loanshark)
    elif random_version == 4:
        intro = version_1d_intro(player, loanshark)
    elif random_version == 5:
        intro = version_1e_intro(player, loanshark)
    return intro
def random_weather_event():


    """
    Randomly selects a weather event from a predefined list and prints it to the console.

    Each weather event is represented by a dictionary with two keys: 'name' and 'description'.
    The 'name' key contains the name of the weather event, and the 'description' key contains
    a descriptive string that sets the mood and atmosphere for the event.

    The function will print the name of the selected event and its description to the console.
    If no weather events are available, the function will print an error message.

    This function is used to generate random weather events for the game.
    """
    weather_events = [
        {
            "name": "Gray and Oppressive",
            "description": (
                "Thick, gray clouds loom low over the city, pressing down with a weight that matches the mood of Old Town. "
                "The air feels heavy with unspoken secrets, and the faint scent of gasoline lingers. People keep their heads down, "
                "eyes wary for signs of trouble."
            )
        },
        {
            "name": "Misty Alleyways",
            "description": (
                "A dense, cold mist hangs in the narrow alleyways, shrouding figures that move like ghosts in the fog. "
                "Streetlights struggle to pierce the gloom, and shadows seem to whisper as they pass. Perfect cover for a deal gone wrong."
            )
        },
        {
            "name": "Cold and Unforgiving",
            "description": (
                "A biting wind cuts through even the thickest of coats, reminding everyone that Old Town is no place for the faint-hearted. "
                "The cold freezes more than just bones—it chills the ambitions of anyone foolish enough to dream too big."
            )
        },
        {
            "name": "Light Snow with Footprints",
            "description": (
                "Snow falls lightly, covering the city in a thin blanket of white, but footprints don't stay hidden for long. "
                "Every step leaves a trail that someone might be following, and in a place like this, anonymity melts as quickly as the snow."
            )
        },
        {
            "name": "Stifling Heat and Suspicion",
            "description": (
                "Unseasonable heat makes the air thick, almost suffocating, as if the whole town is sweating out a guilty conscience. "
                "Cigarette smoke hangs in the air, and tempers are as hot as the pavement. Deals go bad quickly in this kind of weather."
            )
        },
        {
            "name": "Thunderclouds and Tension",
            "description": (
                "Dark thunderclouds gather over Old Town, mirroring the tension in the streets. The threat of a downpour looms, "
                "and every conversation is cut short by the ominous rumble of distant thunder. Even the bravest enforcers seek cover."
            )
        },
        {
            "name": "Fogged-In Harbor",
            "description": (
                "The harbor is blanketed in a thick, impenetrable fog, hiding cargo ships and shady deals alike. "
                "Smugglers move with ease in this weather, but for others, every echo carries a hint of danger."
            )
        },
        {
            "name": "Rain-Slick Streets",
            "description": (
                "Heavy rain pounds against the city, washing away the grime but not the sins of Old Town. "
                "Neon signs reflect in rain-slick streets, and alleyways become treacherous rivers. Only the desperate or the determined are out tonight."
            )
        },
        {
            "name": "Gloomy and Silent",
            "description": (
                "The whole city feels hushed, with an unnatural silence hanging in the air. People speak in whispers, as if afraid the walls might be listening. "
                "Even the usual sounds of industry are muffled, creating an eerie, uneasy calm."
            )
        },
        {
            "name": "Brisk and Restless",
            "description": (
                "A brisk wind blows through the city, carrying news and rumors faster than a Soviet courier. "
                "The cold makes people quick and jittery, glancing over their shoulders, always expecting the unexpected."
            )
        },
        {
            "name": "Slushy Streets",
            "description": (
                "The rain-soaked streets are slick with slush, making every step a potential hazard. The city's residents scramble to stay ahead of the mess."
            )
        },
        {
            "name": "Starless Night",
            "description": (
                "The sky is pitch-black, not a star to be seen, and the usual city lights seem dimmer than usual. "
                "It’s the kind of night when people disappear, swallowed by darkness, and even the bravest avoid the unlit alleys."
            )
        }
    ]

    if not weather_events:
        print("No weather events available.")
        return


    try:
        selected_event = random.choice(weather_events)
        console.print(f"[bold]Weather Event:[/bold] {selected_event['name']}")
        console.print("---------------------------------------------------------------")
        console.print(f"[italic]{selected_event['description']}[/italic]")
        console.print("---------------------------------------------------------------")
    except (IndexError, KeyError) as e:
        console.print(f"An error occurred: {e}")

if __name__ == "__main__":
    intro_messages("player", "loanshark")
    random_weather_event()

