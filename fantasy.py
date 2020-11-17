tools = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    print('Inventory:')
    totalTools = 0
    for t, n in stuff.items():
        print(str(n)+' '+ t)
        totalTools += n

    print ("Total number of items: " + str(totalTools))

displayInventory(tools)