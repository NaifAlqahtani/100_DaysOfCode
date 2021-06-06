import datetime

date = datetime.datetime.now()

day = date.strftime('%A')
dayt = date.day
month = date.month
year = date.year
print(f"\n\n{day}\n{dayt}/{month}/{year}")