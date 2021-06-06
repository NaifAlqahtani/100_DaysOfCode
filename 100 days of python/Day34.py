def function(aList):
    for i in range(1,len(aList)):
        print(i*5)
def tri_recursion(x):
    if x > 0:
        answer = x+tri_recursion(x-1)
        print(answer)
    else:
        answer = 0
    return answer

tri_recursion(6)
print("_______________")
lst = [1,2,3,4,5]

function(lst)