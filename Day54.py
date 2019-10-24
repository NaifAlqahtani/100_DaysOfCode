from datetime import datetime, timedelta

x = datetime.now()


print(x.strftime("\n\nYear: %Y"))
print(x.strftime("Month: %B"))
print(x.strftime("Day: %A"))
print(x.strftime("Time: %I:%M:%S %p  --- %d/%b"))
print("__________________")#challenge bonus after this line:
y = datetime.strftime(datetime.now() - timedelta(1), 'Yesterday: %d/%B/%Y')
t = datetime.strftime(datetime.now() + timedelta(1), 'Tomorrow: %d/%B/%Y')
print(y)
print(t)

