def multiply(n):
    y = lambda x : x*n
    return y

table = multiply(3)

for i in range(1,13):
    print(table(i))