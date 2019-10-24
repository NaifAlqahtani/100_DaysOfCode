try:
    print(x)
except NameError:
    print("Name Error")
except:
    print("Not name Error but an error nonetheless")
################################
try:
    print("Hi")
except:
    print("Some Error")
else:
    print("No errors. All good")
################################
try:
    print("Hi")
except:
    print("Some Error")
finally:
    print("Try:Excpet finished")