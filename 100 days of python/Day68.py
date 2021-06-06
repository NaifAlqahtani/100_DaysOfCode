First_name = "Ahmed"
second_name = "Ali"
balance = 53.44
print("\n\nDear {0} {1}, Your current balance is ${2}".format(First_name,second_name,balance))

#Weekly Challenge:
size = 0
lst = []
size = int(input("\n\nEnter array size (1-5):\n  >"))
if 1<=size<=5:
    for i in range(0,size):
        number = input("   --> ")
        lst.append(number)
    print(lst)
else:
    print("size has to be from 1 to 5")



