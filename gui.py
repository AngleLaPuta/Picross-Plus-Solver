import pygame
import sys
import random

pygame.init()
GRID_SIZE = 10
BOX_SIZE = 800/(GRID_SIZE+2)
NUM_PADDING =  100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FILLED_COLOR = (0, 255, 0)
BAD_COLOR = (255, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Picross GUI")
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

vertical = [[] for i in range(GRID_SIZE)]
horizontal = [[] for i in range(GRID_SIZE)]

def createboard():
    global board,vertical,horizontal,GRID_SIZE,grid
    vertical = [[] for i in range(GRID_SIZE)]
    horizontal = [[] for i in range(GRID_SIZE)]
    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.randint(0,10)<6:
                board[i][j] = '*'
    for i in range(GRID_SIZE):
        sum = 0
        for j in range(GRID_SIZE):
            poop = board[j][i]
            if poop == '*':
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
            if _ == '*': sum+=1
            else:
                if sum: vertical[i].append(sum)
                sum =0
        if sum: vertical[i].append(sum)
        if not vertical[i]:
            vertical[i]=[0]


def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * BOX_SIZE + NUM_PADDING, row * BOX_SIZE + NUM_PADDING, BOX_SIZE, BOX_SIZE)
            if grid[row][col] == '*':
                if board[row][col] == '*':pygame.draw.rect(screen, FILLED_COLOR, rect)
                else:
                    pygame.draw.rect(screen, BAD_COLOR, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)


    font = pygame.font.SysFont(None, 24)

    for row in range(GRID_SIZE):
        x_offset = NUM_PADDING//4-(len(vertical[row])-1)*NUM_PADDING//len(vertical[row])
        for i,number in enumerate(vertical[row]):
            number_surface = font.render(str(number), True, BLACK)
            screen.blit(number_surface,
                        (x_offset + NUM_PADDING // 2,row * BOX_SIZE + NUM_PADDING + BOX_SIZE // 2 - number_surface.get_height() // 2))
            x_offset += NUM_PADDING//len(vertical[row])

    for col in range(GRID_SIZE):
        y_offset = NUM_PADDING // 4 - (len(horizontal[col]) - 1) * NUM_PADDING // len(horizontal[col])
        for i, number in enumerate(horizontal[col]):
            number_surface = font.render(str(number), True, BLACK)
            screen.blit(number_surface,
                        (col * BOX_SIZE + NUM_PADDING + BOX_SIZE // 2 - number_surface.get_width() // 2, y_offset+ NUM_PADDING // 2))
            y_offset += NUM_PADDING // len(horizontal[col])


def handle_click(pos):
    col = int((pos[0] - NUM_PADDING) // BOX_SIZE)
    row = int((pos[1] - NUM_PADDING) // BOX_SIZE)
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
        grid[row][col] = '*' if grid[row][col] == ' ' else ' '
    for i in range(GRID_SIZE):
        print(grid[i], board[i])
    print()

createboard()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                handle_click(event.pos)
    screen.fill(WHITE)
    draw_grid()
    if grid == board: createboard()
    pygame.display.flip()

pygame.quit()
sys.exit()
