import random
import pynput
from pynput import keyboard
from pynput.keyboard import Key


size = 5

board =[ [" " for i in range(size)] for j in range(size)]
vertical = [[] for i in range(size)]
horizontal = [[] for i in range(size)]
x,y=0,0

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
        if sum: horizontal[i].append(sum)
        if not horizontal[i]:
            horizontal[i]=[0]
    for i,line in enumerate(board):
        sum =0
        for _ in line:
            if _ == '-': sum+=1
            else:
                if sum: vertical[i].append(sum)
                sum =0
        if sum: vertical[i].append(sum)
        if not vertical[i]:
            vertical[i]=[0]



def printarray(array):
    for shit in array:
        for caca in shit:
            print(caca,end = " ")
        print()

def printboard():
    global board, vertical, horizontal

    formattedVertical = [' '.join(map(str, clue)) for clue in vertical]
    maxVWidth = max(len(s) for s in formattedVertical) if vertical else 0

    maxH = max(len(col) for col in horizontal) if horizontal else 0

    for level in range(maxH):
        line = ' ' * (maxVWidth + 1)
        for col in horizontal:
            startLevel = maxH - len(col)
            if level >= startLevel:
                line += f"{col[level - startLevel]} "
            else:
                line += "  "
        print(line.rstrip())

    for i, row in enumerate(board):
        vClue = formattedVertical[i].rjust(maxVWidth)
        print(f"{vClue} ", end="")
        print(' '.join(row))

createboard()
printboard()

def on_key_release(key):
    try:
        if key.char == 'd':
            print("Right key clicked")
        elif key.char == 'a':
            print("Left key clicked")
        elif key.char == 'w':
            print("Up key clicked")
        elif key.char == 's':
            print("\r", end = ' ')
    except:
        pass


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()