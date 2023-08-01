import random
def bgk (player_input, status_player, status_enemy):
    tools = ("batu", "gunting", "kertas")
    status_player = False
    status_enemy = False
    mix = random.randint(0, len(tools)-1)
    bot = tools[mix]
    if player_input not in tools:
        print("maaf tapi hanya terdapat 3 alat, gunakan alat yang tersedia")
    else: 
        if player_input == bot :
            print(f"player {player_input} dan enemy {bot}\nseri")
        elif player_input == "batu" and bot == "gunting":
            print(f"player {player_input} dan enemy {bot}\nplayer win")
            status_player = True
        elif player_input == "gunting" and bot == "kertas":
            print(f"player {player_input} dan enemy {bot}\nplayer win")
            status_player = True
        elif player_input == "kertas" and bot == "batu":
            print(f"player {player_input} dan enemy {bot}\nplayer win")
            status_player = True
        else:
            print(f"player {player_input} dan enemy {bot}\nplayer lose")
            status_enemy = True
    return status_player, status_enemy


class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        win = 
    def attack(self, target, damage = 10):
        crit = (True, False)
        chance = random.choice(crit)
        if chance == True:
            rate = [2, 2.5]
            chose = random.choice(rate)
            damage = damage*chose
            target.health -= damage
            print("serangan kritikal")
        else:
            print("serangan normal")
            target.health -= damage
        print(f"{self.name} attacking {damage} damage to {target.name}")
        
        
        '''if target.is_attacked(player_name=self.name):
            self.health -= target.damage'''
    def show_info(self):
        print(f"{self.name} health: {self.health}") 
    def wincon(self, win, target):
        if target.health <= 0 :
            win = True
            print("selamat anda menang")

class Monster:
    def __init__(self, health=100):
        self.name = "Enemy"
        self.health = health #dinamis
        self.damage = 10
    def attack(self, target, damage = 10):
        crit = (True, False)
        chance = random.choice(crit)
        if chance == True:
            rate = [2, 2.5]
            chose = random.choice(rate)
            damage = damage*chose
            target.health -= damage
            print("serangan kritikal")
        else:
            print("serangan normal")
            target.health -= damage
        print(f"{self.name} attacking {damage} damage to {target.name}")
        
    
    '''def is_attacked(self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}")
        return self.health < self.health_init'''
    def show_info(self):
        win= False
        if self.health <= 0 :
            win = True
            print("selamat anda menang")
        print(f"{self.name} health: {self.health}")
    def wincon(self, win, target):
        if target.health <= 0 :
            win = True
            print("sayang sekali anda kalah")
dragon = Monster(health=100)

nama = input("masukan nama player anda")
player = Player(name=nama)
player.show_info()
status_player = False
while True:
    print("selamat datang di program ini")
    player_input = input("ketik batu, gunting atau kertas\n").lower()
    status_player, status_enemy = bgk(player_input, status_player, status_enemy=False)
    
    if status_player:
        player.attack(target=dragon)
        dragon.show_info()
        
    elif status_enemy:
        dragon.attack(target=player)
        player.show_info()