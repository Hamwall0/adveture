import random as rand
 
class spelare():

    def __init__(self,namn, strength, hp, lvl, inventory):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        self.namn = namn

    def stats(namn):
        return print(f"Name: {namn.namn} STR: {namn.strength} , HP: {namn.hp}, LVL: {namn.lvl}\n{namn.inventory}")
    
    def backpack(namn):
        count = 1
        for i in namn.inventory:
            print(f"{count}.",i.Type,"dmg:",i.damadge)
            count +=1
        while True:
            user_choice = input("vill du ta bort ett item y/n--> ")
            if user_choice in ("Yes","Y","y","yes"):
                while True:
                    x = input("välj  positionen på itemet du vill ta bort") 
                    if x <= 5:
                        namn.inventory.pop(x)
                        break
                    else:
                        print("Inmätnings fel")
                        continue
            elif user_choice in ("No","no","N","n"):
                break
            else:
                print("du skrev något förbjudet")
                continue
            
        
        #invent = ["Slot_1","Slot_2","Slot_3","Slot_4","Slot_5"]
        #return print(invent)
        
class item_attribut():
    def __init__(self,dmg,Type):
        self.damadge = dmg
        self.Type = Type 
        
    
def kista():
    while True:
        items = ["penna", "sudd", "sword", "Dog"]
        item_chans = rand.randint(0,len(items)-1)
        Gachaitem = items.pop(item_chans) 
        item = item_attribut(rand.randint(1,5),Gachaitem)
        print("du hittade en kista")
        print("Du fick en:",item.Type)
        namn.inventory.append(item)
        if len(namn.inventory) > 5:
            print("din rygsäck är full")
            
        else:
            return print(f"{item.Type}, added to inventory")

def monster():
    monster_strength = rand.randint(1,10)
    if namn.strength > monster_strength:
        print("du besegrade monstret ")
    elif namn.strength < monster_strength:
        namn.hp += -monster_strength
        print(f"monstret var starkare än dig och du tog skada, M_STR: {monster_strength}")
        print("Current HP:",namn.hp)
    else:
        print(f"{namn.namn} och monstret va gämn starka ")
    

    pass
                
def door():
    while True:
        door = input("välje en av tre dörrar ('1' '2' '3'): 4 = Meny -->  ")
        if door == "4":
            break
        else:
            chans = rand.randint(1,3)
            if chans == 1:
                print("du trillade ned i en fälla")
            elif chans == 2:
                kista()
            elif chans == 3:
                print("du stötte på ett monster")
                monster()
            else:
                print("det fins bara tre dörrar!")
                continue

namn = input("välje ett namn -> ") 
namn = spelare(namn, 5, 10, 1,[])

while True:
    choice = input(""" vad vill du göra
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
