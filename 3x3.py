# 3x3 sudoku
import random

def duplicate_checker(a):
        b = set(a)
        result = len(a) != len(b)
        #print(result)
        if(result == True):
            return True
            
def checkrow_horz(a):
    for x in a:
        if(duplicate_checker(x) == True):
            return True
            
            
def checkrow_vert(a):
    for y in range(len(a)):
        temp = []
        for x in a:
            temp.append(x[y])
        if(duplicate_checker(temp) == True):
            return True
        
def display_grid(grid):
    print("")
    count =1
    print("   1  2  3")
    for x in grid:
        
        print(count,x,end=" ")
        count+=1
        print()
        
def scramble(grid):
    for x in range(6):
        y = random.randint(0,2)
        x = random.randint(0,2)
        grid[x][y] = 0


        
grid = [[1, 2, 3],[3, 1, 2] ,[2, 3, 1]]

solved = False
scramble(grid)
display_grid(grid)


while solved != True:
    y = int(input("enter vertical [1,3] "))-1
    x = int(input("enter horizontal [1,3]"))-1
    num = int(input("enter number]"))
    
    if grid[y][x] == 0:
        grid[y][x] = num
    else:
        if input("overwrite? [y/n]") == "y":
            grid[y][x] = num
        
    display_grid(grid)
    full = True
    for x in grid:
        for y in x:
            if(y == 0):
                full = False
    if(full ==True):
        if(checkrow_horz(grid)==True or checkrow_vert(grid) == True):
            print("try again")
        else:
            print("solved")
            solved =True
    
