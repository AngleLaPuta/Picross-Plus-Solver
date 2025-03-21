import random

size = 5

board =[ ["" for i in range(size)] for j in range(size)]
vertical = [[] for i in range(size)]
horizontal = [[] for i in range(size)]

def createboard():
    global board,vertical,horizontal,size
    for i in range(size):
        for j in range(size):
            if random.randint(0,2)==1:
                board[i][j] = '-'
    for i in range(size):
        sum = 0
        for j in range(size):
            poop = board[j][i]
            if poop == '-':
                sum += 1
            else:
                if sum: horizontal[i].append(sum)
                sum = 0
    for i,line in enumerate(board):
        sum =0
        for _ in line:
            if _ == '-': sum+=1
            else:
                if sum: vertical[i].append(sum)
                sum =0



def printarray(array):
    for shit in array:
        for caca in shit:
            print(caca,end = " ")
        print()

def printboard():
    global board,vertical,horizontal
    print(horizontal)
    for i,shit in enumerate(board):
        print(vertical[i],end = " ")
        for caca in shit:
            print(caca,end = " ")
        print()

createboard()
printboard()