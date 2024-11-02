import random
from rich.console import Console
from rich.text import Text

def print_drug_war_city_map():
    """Prints the layout of the drug war city map."""
    console = Console()

    # Define the map layout with improved formatting
    map_layout = [
        (Text("Harbor District", style="blue bold"), Text("(Smuggling Hub)", style="cyan")),
        (Text("Red Light District", style="magenta bold"), Text("(Nightlife & Deals)", style="cyan")),
        (Text("Cartel Heights", style="green bold"), Text("(Drug Lords)", style="cyan")),
        (Text("Industrial Zone", style="yellow bold"), Text("(Drug Labs)", style="cyan")),
        (Text("Underground Club", style="red bold"), Text("(Fight Pit)", style="cyan")),
        (Text("Black Market", style="purple bold"), Text("(Trade Hub)", style="cyan")),
        (Text("Police Precinct", style="grey"), Text("(Corrupt Cops)", style="cyan")),
        (Text("Old Town Square", style="orange bold"), Text("(Public Clashes)", style="cyan")),
        (Text("The Slums", style="brown"), Text("(Gangland)", style="cyan")),
        (Text("Abandoned Bunkers", style="grey"), Text("(Secret Caches)", style="cyan")),
        (Text("Hidden Routes", style="green bold"), Text("(Escape Paths)", style="cyan")),
    ]

    console.print("City Map:", style="bold underline")
    console.print("-----------------------------------------------------")

    # Print each district with corresponding description
    for district, description in map_layout:
        # Format strings separately to align properly
        district_str = f"{district}"
        description_str = f"{description}"
        
        console.print(f"{district_str:<20} | {description_str}")

    console.print("-----------------------------------------------------")

# Example usage
if __name__ == "__main__":
    print_drug_war_city_map()
