import pygame

class Sudoku():
    def __init__(self):
        self.rows = 9
        self.cols = 9
        self.sudoku_board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.selected = None
        
    def generate_sudoku(self):
        with open("grids.txt", 'r') as file:
            for i, line in enumerate(file):
                numbers = [int(num) for num in line.strip().split()]                
                self.sudoku_board[i] = numbers
                
    def print_sudoku(self):
        for row in range(0, 9):
            for col in range(0, 9):
                print(str(self.sudoku_board[row][col]) + " ", end = "")            
            print("\n")
            
    def is_safe(self, value, row, col) -> bool:
        for index in range(0, 9):
            if self.sudoku_board[index][col] == value:
                return False
            
            if self.sudoku_board[row][index] == value:
                return False
            
            if self.sudoku_board[3 * (row // 3) + index // 3][3 * (col // 3) + index % 3] == value:
                return False
        
        return True
    
    def solve_sudoku(self) -> bool:
        for row in range(0, 9):
            for col in range(0, 9):
                if self.sudoku_board[row][col] == 0:
                    for value in range(1, 10):
                        if self.is_safe(value, row, col):
                            self.sudoku_board[row][col] = value
                            drawboard()
                            pygame.display.update()
                            pygame.time.delay(15)
                            answer = self.solve_sudoku()
                            if answer:
                                return True
                            else:
                                self.sudoku_board[row][col] = 0
                                drawboard()
                                pygame.display.update()
                                pygame.time.delay(15)
                    return False
                
        return True
    
sudoku = Sudoku()
sudoku.generate_sudoku()
sudoku.print_sudoku()
    
def drawboard():
    for i in range (9):
            for j in range (9):
                if sudoku.sudoku_board[i][j]!= 0:
                    pygame.draw.rect(screen, (255, 255, 255), (i * diff, j * diff, diff + 1, diff + 1))
                    text_a = font.render(str(sudoku.sudoku_board[i][j]), 1, (0, 0, 0))
                    screen.blit(text_a, (i * diff + 15, j * diff + 1))
                elif sudoku.selected == (i, j):
                    pygame.draw.rect(screen, (200, 200, 255), (i * diff, j * diff, diff + 1, diff + 1))

    for val in range(10):
        if val % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, val * diff), (500, val * diff), thick)
        pygame.draw.line(screen, (0, 0, 0), (val * diff, 0), (val * diff, 500), thick)

def insert_number(num):
    if sudoku.selected:
        row, col = sudoku.selected
        sudoku.sudoku_board[row][col] = num

# Setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 40)
diff = 500 // 9
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos
            row = y // diff
            col = x // diff
            sudoku.selected = (col, row)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sudoku.solve_sudoku()
                drawboard()
            elif event.key == pygame.K_1:
                insert_number(1)
            elif event.key == pygame.K_2:
                insert_number(2)
            elif event.key == pygame.K_3:
                insert_number(3)
            elif event.key == pygame.K_4:
                insert_number(4)
            elif event.key == pygame.K_5:
                insert_number(5)
            elif event.key == pygame.K_6:
                insert_number(6)
            elif event.key == pygame.K_7:
                insert_number(7)
            elif event.key == pygame.K_8:
                insert_number(8)
            elif event.key == pygame.K_9:
                insert_number(9)

    screen.fill((255, 255, 255))
    drawboard()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
