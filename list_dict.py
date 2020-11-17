def addToInventory(inventory, addedItem):    
    
    for i in addedItem:
        inventory.setdefault(i, 0)
        inventory[i] += 1
        
    return inventory
    

def displayInventory(stuff):

    print('Inventory:')
    totalTools = 0

    for t, n in stuff.items():
        print(str(n)+' '+ t)
        totalTools += n

    print ("Total number of items: " + str(totalTools))

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)