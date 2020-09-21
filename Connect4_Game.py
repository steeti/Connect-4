import random
#initilizing global variables
row=6
col=7
board = []
#random function
turn=random.randint(0,1)
players=["X","O"]
playerwin="w"
numplayers=2
letrange = []
numrange=[]
playagain=99

#putting the letters into the letrange list
for x in range (row):
        letrange.append(chr(x+65))
#putting numbers into numrange list
for x in range(1,col+1):
        numrange.append(x)
                
#creating empty board
for x in range (row):
        y = []
        for s in range(col): 
                y.append(".")
        board.append(y)
#printing the board wiht variables
def printboard():
        print (' ', end='')
        for x in range (1,col+1):
                if x <= 9:
                        print ('  '+str(x)+' ', end='')
                else:
                        print('  '+str(x)+'', end='')
        print()
        for x in range(row):
                print(chr(x + 65) + "|", end=' ')
                for y in range(col):
                        print(board[x][y]+' | ', end='')
                print("\n"+" +"+"---+"*col)
        print()
#destroy disc extension
def destroydisc():
        num=0
        let=0
        x=False
        while x==False:
                loc=input("Choose location to destroy the disc, for example 1A")
                if len(loc)!=2 or loc[0] in numrange:
                        print("the input is Invalid, please print a valid input")
                        continue
                
                num=int(loc[0])
                let=loc[1]
                #print(num, let, board[int(ord(let))-65][num-1])
                
                if (let in letrange) and (num in numrange) and board[int(ord(let))-65][num-1]!=".":
                        x=True
                else:
                        print("the input is Invalid, please print a valid input")

        print(int(ord(let))-65)
        for i in range(int(ord(let))-65, 0, -1):
                print(board[i][num-1], board[i-1][num-1])
                board[i][num-1] = board[i-1][num-1]
                
        board[0][num-1]="."
        printboard()
        destroyused[turn]=True
#checking the conditions for wining the game
def wincheck(wincondition,row,col,board,playerwin):
        #horzintal checking
        for i in range(len(board)):
                chk=[]
                for j in range(len(board[0])):
                        chk=[]
                        #print(i,j)
                        #print(j+3)
                        if j+1 < col and j+2 < col and j+3 < col:
                                #print(i,j)
                                
                                #print(len(board),len(board[x]))
                                chk.append(board[i][j])
                                chk.append(board[i][j+1])
                                chk.append(board[i][j+2])
                                chk.append(board[i][j+3])
                                #print(chk)
                        cntX=0
                        cntO=0
                        
                        for k in range(4):
                                if len(chk) == 4:
                                        if chk[k]=="X":
                                                cntX+=1
                                        elif chk[k]=="O":
                                                cntO+=1
                                        if cntX==4 or cntO==4:
                                                wincondition=True
                                                if cntX==4:
                                                        playerwin="X"
                                                elif cntO==4:
                                                        playerwin="O"
                                                        
                                                return wincondition,playerwin
        #vertical checking
        for i in range(len(board)):
                chk=[]
                for j in range(len(board[0])):
                        chk=[]
                        if i+1 < row and i+2 < row and i+3 < row:
                                chk.append(board[i][j])
                                chk.append(board[i+1][j])
                                chk.append(board[i+2][j])
                                chk.append(board[i+3][j])
                        cntX=0
                        cntO=0
                        for k in range(4):
                                if len(chk) == 4:
                                        if chk[k]=="X":
                                                cntX+=1
                                        elif chk[k]=="O":
                                                cntO+=1
                                        if cntX==4 or cntO==4:
                                                wincondition=True
                                                if cntX==4:
                                                        playerwin="X"
                                                elif cntO==4:
                                                        playerwin="O"
                                                return wincondition,playerwin

        #diagnol 1 checking
        for i in range(len(board)):
                chk=[]
                for j in range(len(board[0])):
                        chk=[]
                        if j+1 < col and j+2 < col and j+3 < col and i+1 < row and i+2 < row and i+3 < row:
                                chk.append(board[i][j])
                                chk.append(board[i+1][j+1])
                                chk.append(board[i+2][j+2])
                                chk.append(board[i+3][j+3])

                        cntX=0
                        cntO=0
                        for k in range(4):
                                if len(chk) == 4:
                                        if chk[k]=="X":
                                                cntX+=1
                                        elif chk[k]=="O":
                                                cntO+=1
                                        if cntX==4 or cntO==4:
                                                wincondition=True
                                                if cntX==4:
                                                        playerwin="X"
                                                elif cntO==4:
                                                        playerwin="O"
                                                return wincondition,playerwin
        
        #diagnol 2 checking
        for i in range(len(board)):
                chk=[]
                for j in range(len(board[0])):
                        chk=[]
                        if j-1 >= 0 and j-2 >= 0 and j-3 >= 0 and i+1 < row and i+2 < row and i+3 < row:
                                chk.append(board[i][j])
                                chk.append(board[i+1][j-1])
                                chk.append(board[i+2][j-2])
                                chk.append(board[i+3][j-3])
                        cntX=0
                        cntO=0
                        for k in range(4):
                                if len(chk) == 4:
                                        if chk[k] == "X":
                                                cntX+=1
                                        elif chk[k] is "O":
                                                cntO+=1
                                        if cntX==4 or cntO==4:
                                                wincondition=True
                                                if cntX==4:
                                                        playerwin="X"
                                                elif cntO==4:
                                                        playerwin="O"
                                                return wincondition,playerwin

        return wincondition,playerwin
#main loop
#wincondition = to false because as long as the game is going it is false
wincondition=False
destroyused=[False, False]
print("players "+players[turn]+" will start the game")
while wincondition==False:
        printboard()
#impleminitg the destoy function once for every user
        if destroyused[turn]==False:
                userinput= input("Do you want to use the destroy disc feature? You can use this feature well. For yes input yes and input anything else if you dont want ot use it: ")
                if userinput=="yes":
                        destroydisc()
        #inputting the col number
        colinput=input("Player "+players[turn]+" enter column number: ")
        #checking for errors
        while not(colinput.isdigit()):
                colinput=input("Player "+players[turn]+" entered a not digit number, please try again")
        while int(colinput) > col or int(colinput)<1:
                colinput=int(input("Player "+players[turn]+" entered a number outside of the column range, please try again"))       
        colinput=int(colinput)-1
        #checks from row from the bottom to the top in the oppisete direction
        for i in range(row-1,-1,-1):
                
                if board[i][colinput]==".":
                        board[i][colinput]=players[turn]
                        break
        #checks if position is empty from the bottom
        for i in range(row-1,-1,-1):
               cnt=0
               if board[i][colinput]==".":
                        cnt=cnt+1
               if cnt==row:
                        colinput=int(input("Column is full please select another column"))
        #implementing wincheck function
        wincondition,playerwin=wincheck(wincondition,row,col,board,playerwin)
        if wincondition==True:
                printboard()
                print("Player "+playerwin+" Won the game")
                print("Do you want want to play again?")
                playagain=input("Enter \"1\" if you want to play again or anything else if you want to exit: ")
                if playagain=="1":
                        board=[]
                        for x in range (row):
                                y = []
                                for s in range(col): 
                                        y.append(".")
                                board.append(y)
                        wincondition=False
                        playagain=99
                      
        

        turn=(turn + 1)%numplayers #will give reminder of 0 or 1
        
printboard()


