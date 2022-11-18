import random as rand
 
class spelare():

    def __init__(self,strength, hp, lvl, inventory):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        
    def inventory(self,inventory):
            self.inventory = inventory.append(item)
    
def __str__():
    print(f"Name: {name} STR: {namn.strength} , HP: {namn.hp}, LVL: {namn.lvl}")

def kista():
        while True:
            item_chans = rand.randint(0,len(items)-1)
            item = items.pop(item_chans)
            print("du hittade en kista")
            print(item)
            print(items)
            return(items)
            
def door():
    while True:
        door = input("välje en av tre dörrar ('1' '2' '3'): ")
        chans = rand.randint(1,3)
        if door in("1","2","3"):
            if chans == 1:
                print("du trillade ned i en fälla")
            elif chans == 2:
                items = ["penna", "sudd", "sword"]
                items = items
                kista()  
            else:
                print("du stötte på ett monster")
        else:
            print("det fins bara tre dörrar!")
            continue
namn = input("välje ett namn -> ") 
namn = spelare(5, 10, 1,[])
while True:
    choice = input(""" vad vill du göra
    1.öppna en dör      2.check status

    3.kolla ditt inventory 
    ->""")
    if choice in ("1","2","3","4"):
        if choice == "1":
            door()
        elif choice == "2":
            stats()
    else:
        print("du skrev in något förbjudet")
        continue
     