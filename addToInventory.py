def addToInventory(inventory, addedItems):
    # your code goes here

    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    #return(inventory)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)