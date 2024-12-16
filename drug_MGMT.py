import random

class Drugs:
    drug_database = [
        {
            'name': 'Velox',
            'description': 'A fast-acting stimulant that enhances focus and energy',
            'base_value_range': (75, 120),
        },
        {
            'name': 'Serenity-X',
            'description': 'A calming blend that promotes relaxation and stress relief',
            'base_value_range': (90, 140),
        },
        {
            'name': 'EchoWave',
            'description': 'A mild psychedelic that amplifies sound and visuals',
            'base_value_range': (120, 180),
        },
        {
            'name': 'PureZen',
            'description': 'A clean, herbal remedy for inducing a tranquil, meditative state',
            'base_value_range': (40, 70),
        },
        {
            'name': 'SomaLift',
            'description': 'A mood booster that provides a balanced, euphoric feeling',
            'base_value_range': (150, 220),
        }
    ]

    @staticmethod
    def print_all():
        # Print the drug database
        for drug in Drugs.drug_database:
            print(f"Name: {drug['name']}")
            print(f"Description: {drug['description']}")
            print(f"Base Value Range: {drug['base_value_range']}")
            print("=" * 100)
def print_drug_price_test():
    # Accessing a random drug and generating its price
    x = random.randint(0, 4)  # Randomly choose an index between 0 and 4
    newdrug = Drugs.drug_database[x]  # Select the drug based on the random index

    # Generating a random price within the base value range
    newdrug_price = random.randint(newdrug['base_value_range'][0], newdrug['base_value_range'][1])

    # Printing the result
    print(f"{newdrug['name']} price: ${newdrug_price}")

    # Optionally, print all drugs
    # Drugs.print_all()  # Uncomment this line if you want to print all drug details