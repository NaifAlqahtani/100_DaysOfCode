
def func():
    x = 300
    def returnfunc():
        print(x)
    returnfunc()

func()
#print(x) allowing this will raise an error since x is a local variable to func() only and not globally