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
    def version_1_intro(player, loanshark):
        console.print("[bold magenta]Welcome to Old Town...[/bold magenta]", style="underline")
        console.print("Where fortunes are made and broken with every step.")
        console.print(f"[bold red]You've got a problem...[/bold red]")
        console.print(f"Your debt to the feared loan shark, {loanshark}, is threatening to consume you.")
        console.print(f"You have 30 days to repay the debt. The streets are watching, and so are {loanshark}'s goons.")
        console.print("Will you be able to navigate the treacherous underworld of Old Town?")
        console.print("Or will you become just another statistic in our little neighborhood?")
        console.print(f"[bold blue]You've found some cash...[/bold blue]")
        console.print(f"It's not much, but it’s enough to keep you going for now. {monetary_name}")

    def version_2_intro(player, loanshark):
        console.print("[bold magenta]In a world where fortunes are made and broken on the streets of Old Town...[/bold magenta]")
        console.print(f"You've found yourself at the center of it all.")
        console.print(f"[bold red]You owe the notorious loan shark, {loanshark}, a debt that could cost you everything.[/bold red]")
        console.print("Thirty days remain to settle this score before")
        console.print(f"the weight of your failure crushes you beneath its heel.")
        console.print("[bold green]But don’t worry...[/bold green]")
        console.print("You’ve got a small lifeline.")
        console.print(f"You won the lottery last night, and instead of blowing it all on a quick fix,")
        console.print("you wisely chose to hang onto a small sum. It might just be enough to keep you afloat.")

    def version_3_intro(player, loanshark):
        console.print("[bold magenta]The neon lights of Old Town flicker like fireflies on the night...[/bold magenta]")
        console.print(f"Your name is etched into the annals of this underworld, where fortunes are made and broken with every step.")
        console.print(f"[bold red]You're in a bind...[/bold red]")
        console.print("And you know it.")
        console.print(f"You've managed to talk your way into a high-stakes game of poker with some shady characters.")
        console.print(f"Against all odds, you came out on top, winning just enough cash to keep your head above water.")
        console.print("[bold blue]You're still standing...[/bold blue]")
        console.print("But the goons are closing in.")

    def version_4_intro(player, loanshark):
        console.print("[bold magenta]Old Town is a place where danger and opportunity dance together...[/bold magenta]")
        console.print(f"and {player[0]} knows this all too well.")
        console.print(f"[bold red]Your debt to the ruthless loan shark, {loanshark}, looms over you like a shadow.[/bold red]")
        console.print("Thirty days separate you from ruin or redemption.")
        console.print("[bold green]But fortune has smiled upon you...[/bold green]")
        console.print(f"However briefly.")
        console.print(f"You stumbled upon a street magician’s hat—abandoned and filled with coins from an unfinished performance.")
        console.print(f"You collected the scattered money, enough to give you a fragile lifeline. {monetary_name()}")

    def version_5_intro(player, loanshark):
        console.print("[bold magenta]You've been to the depths of despair...[/bold magenta]")
        console.print("The debt you owe to the infamous {loanshark} weighs heavily on your soul,")
        console.print(f"and you’ve got only 30 days to make things right.")
        console.print("[bold red]But a stroke of luck has brought you a small break.[/bold red]")
        console.print("You found a misplaced wallet wedged between the seats of an empty subway car.")
        console.print(f"[bold blue]Inside were a few crumpled bills and some loose change...[/bold blue]")
        console.print("It’s not a windfall,")
        console.print("but it’s enough to give you a fighting chance.")


    random_version = random.randint(1, 5)
    if random_version == 1:
        intro = version_1_intro(player, loanshark)
    elif random_version == 2:
        intro = version_2_intro(player, loanshark)
    elif random_version == 3:
        intro = version_3_intro(player, loanshark)
    elif random_version == 4:
        intro = version_4_intro(player, loanshark)
    elif random_version == 5:
        intro = version_5_intro(player, loanshark)
    return intro

    events = [
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
            "name": "Slush and Secrets",
            "description": (
                "Melting snow mixes with grime, creating a dirty slush that hides more than just mud. "
                "Papers, cigarette butts, and discarded secrets float in the slushy gutters, and every step is a reminder of how messy life can get."
            )
        },
        {
            "name": "Heavy Snow and Heavy Hearts",
            "description": (
                "Snow falls in thick, heavy flakes, muffling the sounds of the city. It would be beautiful if not for the cold dread that settles in the gut. "
                "In Old Town, snow is just another cover for things best kept hidden."
            )
        },
        {
            "name": "Stagnant Air",
            "description": (
                "The air is still and stagnant, as if the city itself is holding its breath. There’s no breeze, no relief, only the oppressive feeling "
                "that something is about to go very wrong. Conversations are quiet, and eyes dart to alleyways where trouble always waits."
            )
        },
        {
            "name": "Warm and Deceptive",
            "description": (
                "A rare warm spell has people shedding their coats, but the warmth feels almost wrong, like a con man’s smile. "
                "It lulls you into a false sense of security, and only the wise keep their wits sharp, knowing a storm is never far behind."
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

    # Select a random weather event
    selected_event = random.choice(events)
    print(f"Weather Event: {selected_event['name']}")
    print(f"Description: {selected_event['description']}")

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

