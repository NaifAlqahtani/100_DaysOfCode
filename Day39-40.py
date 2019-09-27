def power(base,exp):
    if(exp==1):
        return(base)
    if(exp==0):
        return(1)
    if(exp>1):
        return(base*power(base,exp-1))

fivePowerThree = power(5,3)
print(fivePowerThree)
#---------------------------------------------
myList = [-4, -6, -5, -1, 2, 3, 7, 9, 88]

def positive(lst):
    newList = list(filter(lambda n: (n >= 0), lst))
    return newList

print(positive(myList))