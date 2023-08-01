import random
class player:
    def __init__(self, nama, bertahan, hp=100, energi=100):
        self.nama = nama
        self.hp = hp
        self.energi = energi
        self.bertahan = bertahan
    def serang(self, target, damage=10):
        #target = monster
        target.hp -= damage
        self.energi -= damage/2
        print(f"player serang monster {damage}")
        if target.diserang():
            if self.bertahan == True:
                self.hp -= target.damage/2
            else:
                self.hp -= target.damage
        
class monster:
    def __init__(self, nama, hp=500, damage=0):
        self.nama = nama
        self.hp = hp
        self.hp_init = self.hp
        self.damage =  random.choice(range(10, 51, 10))
        print(f"monster menyerang {self.damage}")
    def diserang(self):
        
        return self.hp < self.hp_init
        
    
#player = player(nama="bejo", bertahan= False)
monster1 = monster(nama ="kaijuu")
monster2 = monster(nama= "godzilaa")
#player.serang(target=monster1 )
print(player.__dict__)
print(monster1.__dict__)
print(monster2.__dict__)

p1 = input("berikan nama pada player anda:")
print(p1)
player1 = player(nama=p1)
print(f"selamat datang {p1}")

while True:
    action = input("pilih aksi anda \nA. Serang monster\nB. Bertahan").lower
    if action == "a":
        player1.serang(target=monster1)
        monster1.showinfo()