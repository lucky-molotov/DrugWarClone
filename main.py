import characters

def main():
    player_character = characters.PlayerCharacter(
        first_name=characters.create_gangster()[0],
        last_name=characters.create_gangster()[1],
        nickname=characters.create_gangster()[2],
        health=100,
        weapon="none",
        currency=100,
        inventory=["empty"],
        location="OldTown",
    )

    print(player_character.__repr__())

main()