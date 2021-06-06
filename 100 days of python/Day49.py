x = 420

def function():
    global x
    x = 69 #this will change the previous value of x since we used global to call x

function()
print(x)