import random as rand
import time

class Fiende():
    def __init__(self, monster_namn, monster_styrka):
        self.namn = monster_namn
        self.styrka = monster_styrka
        self.hp = rand.randint(20,30)
            
class Cockroach_type(Fiende):
    def __init__(self, monster_namn, monster_styrka):
        super().__init__(monster_namn, monster_styrka)
        self.hp = rand.randint(21,40)

    
class Sheep_type(Fiende):
    def __init__(self, monster_namn, monster_styrka):
        super().__init__(monster_namn, monster_styrka)
        self.hp = rand.randint(10,19)


class item_attribut():
    def __init__(self,dmg,Type):
        self.dmg = dmg
        self.Type = Type

class Spelare():

    def __init__(self,namn, strength, hp, lvl, inventory, exp, exp_lim):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        self.namn = namn
        self.exp = exp
        self.exp_lim = exp_lim

    def stats(self): # en funktion som skriver ut spelarens nuvarande stats
        return print(f"""Name: {spelare.namn} 
    STR: {spelare.strength} + {item_bonus()} 
    HP: {spelare.hp}
    LVL: {spelare.lvl}
    EXP: {spelare.exp}/{40*spelare.exp_lim}""")
    
    def backpack(self): # en funtkion som skriver ut spelarens föremål
        count = 1
        for sak in self.inventory:
            print(f"{count}.",sak.Type,"dmg:",sak.dmg,)
            time.sleep(.25)
            count +=1
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
        spelare.exp += 20
        if spelare.exp == 40*spelare.exp_lim:
            spelare.exp -= 40*spelare.exp_lim
            spelare.strength += 3
            spelare.lvl += 1
            spelare.hp += 5
            spelare.exp_lim += 0.5
            print(f"""du levlade upp! 
[STR: {spelare.strength}]
[LVL: {spelare.lvl}]
[HP: {spelare.hp}]
EXP: {spelare.exp}""")
      

def manadge_items():# en funktion som hanterar spelaren föremål 
    while True:
        val = input("\nvälj  positionen på itemet du vill ta bort: ")
        if val.isdigit() and int(val) <= len(spelare.inventory):
            skräp = spelare.inventory.pop(int(val)-1)
            print("You removed:", skräp.Type, "dmg:", skräp.dmg)
            break
        else:
            print("Inmätnings fel")
            continue          
                
def kista():
    while True:
        items = ["penna", "sudd", "sword", "Dog"] # Är items som hittas i kista
        item_chans = rand.randint(0,len(items)-1) # Definerar ett slumpmässigt item som "item_chans"
        item = item_attribut(5,items.pop(item_chans)) # Ger ett slumpmässigt föremål en slumpmässig styrka 
        print("\ndu hittade en kista")
        print("Du fick en:",item.Type,"DMG: ",item.dmg)
        spelare.lvl_up()
        print("+ 10 EXP ")
        spelare.inventory.append(item)
        if len(spelare.inventory) > 5:
            print("\ndin rygsäck är full")
            spelare.backpack()
            break
        else:
            if item_bonus() == 25:
                print("\n Du har blivit DPS Gud! \n + 30 HP")
                spelare.hp += 30
            return 
           

def item_bonus():
    dmg_bonus = 0
    for sak in spelare.inventory:
        dmg_bonus += sak.dmg
    return(dmg_bonus)

def combat():
    full_dmg = item_bonus()
    list_of_fiende = [fiende, sheep, roaches]
    fiende_chans = rand.randint(0,len(list_of_fiende)-1)
    random_fiende = list_of_fiende.pop(fiende_chans)
    monster_hp = rand.randint(5,10*spelare.lvl)
    print(f"\n The battle begins! {spelare.namn} vs {random_fiende.namn}")
    while spelare.hp > 0 or random_fiende.hp:
        monster_hp == random_fiende.hp
        input("press enter to attack ")
        fiende.styrka = rand.randint(6,9)
        sheep.styrka = rand.randint(3,5)
        roaches.styrka = rand.randint(0,2)
        random_fiende.hp -= spelare.strength + full_dmg
        spelare.hp -= random_fiende.styrka
        print(f"\n {random_fiende.namn} dealt: {random_fiende.styrka}       {spelare.namn} dealt: {spelare.strength} ")
    
        print(f"""{random_fiende.namn}'s HP = {random_fiende.hp}       {spelare.namn}'s HP = {spelare.hp} """)
        if spelare.hp <= 0:
            print("\nYou lost the battle!")
            break
        elif random_fiende.hp <= 0:
            print("\nThe monster was defeated!")
            spelare.lvl_up()
            print("you gained 10 EXP")
            break
#Ger chosen att alltingen fly eller attakera monstret.
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
    while spelare.hp > 0 and spelare.lvl < 10:
        door = input("\nvälje en av tre dörrar ('1' '2' '3'): 4 = Meny --> ")
        if door == "4":
            break
        elif door in("1","2","3"):
            chans = rand.randint(1,3)
            if chans == 1:
                print("\ndu trillade ned i en fälla")
                print(f"HP:{spelare.hp} -1")
                spelare.hp -= 1   
            elif chans == 2:
                kista()
            elif chans == 3:
                print("\ndu stötte på ett monster")
                monster()
        else:
            print("\ndet fins bara tre dörrar!")
            continue

roaches = Cockroach_type("Roach", rand.randint(0,9))
sheep = Sheep_type("Sheep", rand.randint(5,12))
fiende = Fiende("Bertil", rand.randint(6,9))

spelare_namn = input("välje ett namn -> ") 
spelare = Spelare(spelare_namn, 50, 50, 1,[], 0, 1)

while spelare.hp>0 and spelare.lvl < 10:
    choice = input(""" \nvad vill du göra
1.öppna en dör      2.check status

3.kolla ditt inventory 
    ->""")
    if choice in ("1","2","3","4"):
        if choice == "1":
            door()
        elif choice == "2":
            spelare.stats()
        elif choice == "3":
            spelare.backpack()
    else:
        print("du skrev in något förbjudet")
        continue
if spelare.lvl == 10:
    print("DU VANN!")
else:
    print("GAME OVER")