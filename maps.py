def print_drug_war_city_map():
    map_layout = [
        "-----------------------------------------------------",
        "| Harbor District  | Red Light District | Cartel Heights |",
        "| (Smuggling Hub)  | (Nightlife & Deals)| (Drug Lords)   |",
        "-----------------------------------------------------",
        "| Industrial Zone  | Underground Club   | Black Market  |",
        "| (Drug Labs)      | (Fight Pit)        | (Trade Hub)   |",
        "-----------------------------------------------------",
        "| Police Precinct  | Old Town Square    | The Slums     |",
        "| (Corrupt Cops)   | (Public Clashes)   | (Gangland)    |",
        "-----------------------------------------------------",
        "| Abandoned Bunkers| The Slums          | Hidden Routes |",
        "| (Secret Caches)  | (Drug Tunnels)     | (Escape Paths)|",
        "-----------------------------------------------------"
    ]

    for line in map_layout:
        print(line)
import random
from rich.console import Console
from rich.text import Text

def create_random_monetary_name():
    adjectives = ["Gigantic", "Tiny", "Mighty", "Small", "Extraordinary"]
    nouns = ["Roubles", "Dollars", "Pounds", "Yen", "Euro"]

    return f"{random.choice(adjectives)} {random.choice(nouns)}"



