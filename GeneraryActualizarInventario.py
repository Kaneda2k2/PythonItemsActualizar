import collections
#dragon loot

#Formulara para pasar de lista a dictionario
#dodo=dict(collections.Counter(inv)+collections.Counter(dragonLoot))
#print(dodo)



#lista de los objetos que suelta el jefe final nivel estatico #
Diablo=["moneda oro","daga","moneda oro","moneda oro","ruby","daga","antorcha"]
#inventario jugador
inv = {"flecha":12,"moneda oro":42,"cuerda":1,"antorcha":6,"daga":1}


#pasamos la lista a diccionario , importar collections
Diablo=dict(collections.Counter(inv)+collections.Counter(Diablo))



def add_to_inventory(inventory, items):
    inv.update(Diablo)




def display_inventory(inventory):
     item_total = sum(inventory.values())
     for k,v in inventory.items():
       print(k,v)
     print("Total number of items: " + str(item_total))

display_inventory(inv)
add_to_inventory(inv, Diablo)
display_inventory(inv)
