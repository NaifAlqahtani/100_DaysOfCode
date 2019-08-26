x = int(3)
y = int("3") #using quotes wont change the output

z = str(314159)
length = len(z) #finding a length of an integer using the function len() will not work until you convert it to a string

print(x,y,"\n",z,"it's length is",length,"digits")