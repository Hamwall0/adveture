import random as rand

class item_attribut():
    def __init__(self,dmg,Type):
        self.dmg = dmg
        self.Type = Type

class spelare():

    def __init__(self,namn, strength, hp, lvl, inventory, exp, exp_lim):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        self.namn = namn
        self.exp = exp
        self.exp_lim = exp_lim

    def stats(self):
        return print(f"""Name: {Gamer_attribute.namn} 
    STR: {Gamer_attribute.strength} + {item_bonus()} 
    HP: {Gamer_attribute.hp}
    LVL: {Gamer_attribute.lvl}
    EXP: {Gamer_attribute.exp}/{40*Gamer_attribute.exp_lim}""")
    
    def backpack(self):
        count = 1
        for sak in self.inventory:
            print(f"{count}.",sak.Type,"dmg:",sak.dmg)
            count +=1
            if sak in self.inventory == 5:
                print("\n Du har blivit DPS Gud! \n + 30 HP")
                self.hp += 30
        if len(self.inventory) > 5:
            manadge_items()
        elif len(self.inventory) > 0:
            while len(self.inventory)>0:
                user_choice = input("\nvill du ta bort ett item y/n--> ")
                if user_choice in ("Yes","Y","y","yes"):
                    manadge_items()
                elif user_choice in ("No","no","N","n"):
                    break
                else:
                    print("du skrev något förbjudet")
                    continue
        else:
            print("\ndin rygsäck är tom")

    def lvl_up(self):
        Gamer_attribute.exp += 10
        if Gamer_attribute.exp == 40*Gamer_attribute.exp_lim:
            Gamer_attribute.strength += 3
            Gamer_attribute.lvl += 1
            Gamer_attribute.hp += 5
            Gamer_attribute.exp_lim += 1.5
            print(f"""du levlade upp! 
[STR: {Gamer_attribute.strength}]
[LVL: {Gamer_attribute.lvl}]
[HP: {Gamer_attribute.hp}]
EXP: {Gamer_attribute.exp}""")

class fiende():
    def __init__(self, monster_namn, monster_styrka, monster_hp):
        self.monster_namn = monster_namn
        self.monster_styrka = monster_styrka
        self.monster_hp = monster_hp

        

def manadge_items():
    while True:
        x = int(input("\nvälj  positionen på itemet du vill ta bort: "))
        if x <= len(Gamer_attribute.inventory):
            trash  = Gamer_attribute.inventory.pop(x-1)
            print("You removed:", trash.Type, "dmg:", trash.dmg)
            break
        else:
            print("Inmätnings fel")
            continue          
                
def kista():
    while True:
        items = ["penna", "sudd", "sword", "Dog"]
        item_chans = rand.randint(0,len(items)-1)
        Gachaitem = items.pop(item_chans) 
        item = item_attribut(rand.randint(1,5),Gachaitem)
        print("\ndu hittade en kista")
        print("Du fick en:",item.Type,"DMG: ",item.dmg)
        spelare.lvl_up()
        print("+ 10 EXP ")
        Gamer_attribute.inventory.append(item)
        if len(Gamer_attribute.inventory) > 5:
            print("\ndin rygsäck är full")
            Gamer_attribute.backpack()
            break
        else:
            return 
           

def item_bonus():
    dmg_bonus = 0
    for sak in Gamer_attribute.inventory:
        dmg_bonus += sak.dmg
    return(dmg_bonus)

class fiende():
    def __init__(self, styr, hp):
        self.styr = styr
        self.hp = hp
        pass

def combat():
    full_dmg = item_bonus()
    monster_strength = rand.randint(1,3)
    monster_hp = rand.randint(5,10*Gamer_attribute.lvl)
    while monster_hp > 0 and Gamer_attribute.hp > 0:
        input("press enter to attack ")
        monster_hp -= Gamer_attribute.strength + full_dmg
        Gamer_attribute.hp -= monster_strength
        print(f"{Gamer_attribute.namn} HP:{Gamer_attribute.hp} monster HP: {monster_hp}")
        if Gamer_attribute.hp <= 0:
            break
        elif monster_hp <= 0:
            Gamer_attribute.lvl_up()
            print("+ 10 EXP")
    
def monster():
    while True:
        choice = input("run? y/n: ")
        if choice in ("y","Y","Yes","YES"):
            chance = rand.randint(1,5)
            if chance in (1,2,3):
                print("du lyckades fly från monstret")
                break 
            else:
                print("du lyckades inte fly")
                combat()
                break
        elif choice in ("NO","N","n","No"):
            combat()
            break
        else:
            print("du skrev något förbjudet")
            continue
        

      
def door():
    while Gamer_attribute.hp > 0 and Gamer_attribute.lvl < 10:
        door = input("\nvälje en av tre dörrar ('1' '2' '3'): 4 = Meny --> ")
        if door == "4":
            break
        elif door in("1","2","3"):
            chans = rand.randint(1,3)
            if chans == 1:
                print("\ndu trillade ned i en fälla")
                print(f"HP:{Gamer_attribute.hp} -1")
                Gamer_attribute.hp -= 1   
            elif chans == 2:
                kista()
            elif chans == 3:
                print("\ndu stötte på ett monster")
                monster()
        else:
            print("\ndet fins bara tre dörrar!")
            continue

spelare_namn = input("välje ett namn -> ") 
Gamer_attribute = spelare(spelare_namn, 50, 50, 1,[], 0, 1)

while Gamer_attribute.hp>0 and Gamer_attribute.lvl < 10:
    choice = input(""" \nvad vill du göra
    1.öppna en dör      2.check status
    3.kolla ditt inventory 
    ->""")
    if choice in ("1","2","3","4"):
        if choice == "1":
            door()
        elif choice == "2":
            Gamer_attribute.stats()
        elif choice == "3":
            Gamer_attribute.backpack()
    else:
        print("du skrev in något förbjudet")
        continue
if Gamer_attribute.lvl == 10:
    print("DU VANN!")
else:
    print("GAME OVER")