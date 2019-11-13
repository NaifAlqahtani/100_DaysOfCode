import random

cell = [' ',' ',' ',
        ' ',' ',' ',
        ' ',' ',' ']

user = ['X','O']
turn = random.choice(user)

def flipTurn():
    global turn
    if turn == user[0]:
        turn = user[1]
    else:
        turn = user[0]

def clear():
    print(chr(27) + "[2J")
    print("\n\n")

def drawBoard():    
    print(f" {cell[0]} | {cell[1]} | {cell[2]} ")
    print("---|---|---")
    print(f" {cell[3]} | {cell[4]} | {cell[5]} ")
    print("---|---|---")
    print(f" {cell[6]} | {cell[7]} | {cell[8]}\n\n\n")

def checkwinner():
    diagonalCells1 = [cell[0],cell[4],cell[8]]
    diagonalCells2 = [cell[2],cell[4],cell[6]]
    verticleCells1 = [cell[0],cell[3],cell[6]]
    verticleCells2 = [cell[1],cell[4],cell[7]]
    verticleCells3 = [cell[2],cell[5],cell[8]]
    horizontalCells1 = [cell[0],cell[1],cell[2]]
    horizontalCells2 = [cell[3],cell[4],cell[5]]
    horizontalCells3 = [cell[6],cell[7],cell[8]]
    if cell.count(' ') == 0:
        return False
    elif diagonalCells1[0] != ' ' and len(set(diagonalCells1)) == 1 or diagonalCells2[0] != ' ' and len(set(diagonalCells2)) == 1:
        return False
    elif verticleCells1[0] != ' ' and len(set(verticleCells1)) == 1 or verticleCells2[0] != ' ' and len(set(verticleCells2)) == 1:
        return False
    elif verticleCells3[0] != ' ' and len(set(verticleCells3)) == 1 or horizontalCells1[0] != ' ' and len(set(horizontalCells1)) == 1:
        return False
    elif horizontalCells2[0] != ' ' and len(set(horizontalCells2)) == 1 or horizontalCells3[0] != ' ' and len(set(horizontalCells3)) == 1:
        return False
    else:
        return True

clear()
# gamemode = int(input("""Game Starting.... 
#   1. VS HUMAN
#   2. VS CPU\n\n  Please select an option\n   > """))  #Coming Soon. Stay tuned!
drawBoard()
choice = int(input("Choose cell from 1-9:\n    > ")) 

while checkwinner():
    if 1<=choice<=9 and cell[choice-1] == ' ':
        clear()
        cell[choice-1] = turn 
        flipTurn()
        checkwinner()
        if checkwinner() == False:
            break
        drawBoard()
    else:
        clear()
        drawBoard()
        print("ERROR: Please enter a valid cell number") 
    choice = int(input("Choose cell from 1-9:\n    > "))

clear()
drawBoard()
flipTurn()
if turn == user[0] and cell.count(' ') > 0:
    print("(X) Crosses WON!")
elif turn == user[1] and cell.count(' ') > 0:
    print("(O) Naughts WON!")
else:
    print("It's a BORING draw...")
        

    
        



