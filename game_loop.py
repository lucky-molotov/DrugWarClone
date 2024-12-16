import time,character_MGMT, message_events,hud,random



class newgame():
    #function to create a new character
    def create_character():
        player_character = character_MGMT.PlayerCharacter.create_character()
        time.sleep(2)
        
        return player_character
    
     #function to create a new landlord   
    def generate_landlord():
        loanshark = character_MGMT.npc.create_npc("loan shark")
        return loanshark
    #introduction
    def start_standard_game(character,loanshark):
        debt=3000
        character.money = random.randint(500,3000)
        character.day = 30
        character.inventory = None

        message_events.intro_messages(character,loanshark)
        hud.player_hud(character,character.day,character.money,debt,str(character.inventory))
        hud.actions_hud()
        hud.inventory_hud()
    
    character = create_character()
    loanshark = generate_landlord()
    start_standard_game(character,loanshark)

newgame()
