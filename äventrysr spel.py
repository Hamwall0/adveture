import random as rand
 
class spelare():

    def __init__(self,namn, strength, hp, lvl, inventory):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        self.namn = namn

    def stats(namn):
        return print(f"Name: {namn.namn} STR: {namn.strength} + {item_bonus()} , HP: {namn.hp}, LVL: {namn.lvl}\n")
    
    def backpack(namn):
        count = 1
        for sak in namn.inventory:
            print(f"{count}.",sak.Type,"dmg:",sak.dmg)
            count +=1
        if len(namn.inventory) > 5:
            manadge_items()
        elif len(namn.inventory) > 0:
            while True:
                user_choice = input("\nvill du ta bort ett item y/n--> ")
                if user_choice in ("Yes","Y","y","yes"):
                    manadge_items()
                elif user_choice in ("No","no","N","n"):
                    break
                else:
                    print("du skrev något förbjudet")
                    continue
        else:
            print("din rygsäck är tom")

def lvl_up():
    print(f"du levlade upp: [STR {namn.strength} + 3] [LVL {namn.lvl} + 1], [HP {namn.hp} + 2]")
    namn.strength += 3
    namn.lvl += 1
    namn.hp += 2


def manadge_items():
    while True:
        x = int(input("\nvälj  positionen på itemet du vill ta bort"))
        if x <= len(namn.inventory):
            trash  = namn.inventory.pop(x-1)
            print("You removed:", trash.Type, "dmg:", trash.dmg)
            break
        else:
            print("Inmätnings fel")
            continue          
                
class item_attribut():
    def __init__(self,dmg,Type):
        self.dmg = dmg
        self.Type = Type 
        
    
def kista():
    while True:
        items = ["penna", "sudd", "sword", "Dog"]
        item_chans = rand.randint(0,len(items)-1)
        Gachaitem = items.pop(item_chans) 
        item = item_attribut(rand.randint(1,5),Gachaitem)
        print("\ndu hittade en kista")
        print("Du fick en:",item.Type,"DMG: ",item.dmg)
        lvl_up()
        namn.inventory.append(item)
        if len(namn.inventory) > 5:
            print("din rygsäck är full")
            namn.backpack()
            break
        else:
            return print(f"{item.Type}, added to inventory")

def item_bonus():
    dmg_bonus = 0
    for sak in namn.inventory:
        dmg_bonus += sak.dmg
    return(dmg_bonus)

def combat():
    full_dmg = item_bonus()
    monster_strength = rand.randint(1,3)
    monster_hp = rand.randint(5,10*namn.lvl)
    while monster_hp > 0 and namn.hp > 0:
        input("press enter to atack")
        monster_hp -= namn.strength
        namn.hp -= monster_strength
        print(f"{namn.namn} HP:{namn.hp} monster HP: {monster_hp}")
        if namn.hp <= 0:
            break
        elif monster_hp <= 0:
            lvl_up()
    
def monster():
    while True:
        choice = input("run? y/n")
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
    while namn.hp >0 and namn.lvl <= 10:
        door = input("\nvälje en av tre dörrar ('1' '2' '3'): 4 = Meny --> ")
        if door == "4":
            break
        elif door in("1","2","3"):
            chans = rand.randint(1,3)
            if chans == 1:
                print("\ndu trillade ned i en fälla")
                print(f"HP:{namn.hp} -1")
                namn.hp -= 1   
            elif chans == 2:
                kista()
            elif chans == 3:
                print("\ndu stötte på ett monster")
                monster()
        else:
            print("\ndet fins bara tre dörrar!")
            continue

namn = input("välje ett namn -> ") 
namn = spelare(namn, 5, 10, 1,[])

while namn.hp>0 and namn.lvl <= 10:
    choice = input(""" \nvad vill du göra
    1.öppna en dör      2.check status
    3.kolla ditt inventory 
    ->""")
    if choice in ("1","2","3","4"):
        if choice == "1":
            door()
        elif choice == "2":
            namn.stats()
        elif choice == "3":
            namn.backpack()
    else:
        print("du skrev in något förbjudet")
        continue
if namn.lvl == 10:
    print("du vann")
else:
    print("game over")
    #Välja en specific door, Monster HP (Combat mechanics)
