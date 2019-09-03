thislist = ['Dog','Cat','Bird','Horse','Cat','Donkey','Dog']

thislist.append('Cat')
thislist.pop(2)
catNumber = thislist.count('Cat')
newCopy = thislist.copy()

print(newCopy,'\nThere are {} cats in this list'.format(catNumber))