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
    print("")
    print("         Martin's Sudoku")
    print("")
    count =0
    print("      1 2 3   4 5 6   7 8 9")
    print("   ---------------------------")
    for x in grid:
        print(count+1,end="   ")
        for y in range(len(x)):
            if(y % 3 != 0):
                print(x[y],end=" ")
            else:
                print("|",x[y],end=" ")
        print("|",end=" ")
        count+=1
        print()
        if(count % 3 == 0):
            print("   ---------------------------")
def rearrange(a):
    temp=[[],[],[],[],[],[],[],[],[]]
    count =0
    ch = 0
    for e in range(len(a)):
        for x in range(3):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count ==3):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(3,6):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count ==3):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(6,9):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count ==3):
            ch+=1
            count = 0
    return temp       
def scramble():
    global grid
    amount = 40
  
    for i in range(amount):
        y = random.randint(0,len(grid)-1)
        x = random.randint(0,len(grid)-1)
        num = random.randint(1,len(grid))
        allow = 0
        for e in range(len(grid)):
            if num not in grid[x] and num != grid[e][y]:
                allow +=1
        grid[x][y] = num
        tempo = grid     
        tempo = rearrange(tempo)
        
        for e in range(len(grid)):
            if(duplicate_checker(tempo[e])):
                allow = 0
        if allow !=len(grid):
            grid[x][y] = 0
               

                


        
grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

solved = False
scramble()
display_grid(grid)


while solved != True:
    x = int(input("enter horizontal [1,9]"))-1
    y = int(input("enter vertical [1,9] "))-1
    
    num = int(input("enter number"))
    
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
    
