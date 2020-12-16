def addToInventory(inventory, addedItems):
    # your code goes here
    for dragonthings in addedItems:
        inventory.setdefault(dragonthings, 0)
        inventory[dragonthings] += 1
    return(inventory)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        item_total= item_total+v
        print (str(v)+' '+k)
    print("Total number of items: " + str(item_total))



inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)