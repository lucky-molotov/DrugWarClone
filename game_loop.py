import time,character_MGMT, message_events,hud,random



class newgame():
    #introduction
    def start_standard_game(character,loanshark):
        
        debt=3000
        character.money = random.randint(500,3000)
        character.day = 30
        character.inventory = None

        message_events.intro_messages(character,loanshark)
        hud.player_hud(character,character.day,character.money,debt,str(character.inventory))
        hud.actions_hud()
        hud.inventory_hud
    
    character = character_MGMT()
    loanshark = generate_loanshark()
    start_standard_game(character,loanshark)


if __name__ == "__main__":
    newgame()

