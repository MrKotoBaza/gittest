import random 
import os.path
height = 100
width = 100
path = r"C:\Users\Александра\Desktop\Основная папка\XXXXXXXXXXXXXXX\patterns"

def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0, 1)

grid_model = [0]*height
next_grid_model = [0]*height
for i in range(height):
    grid_model[i] = [0]*width
    next_grid_model[i] = [0]*height
    

patterns = []

def get_patterns(path):
    global patterns
    patterns = os.listdir(path)
    patterns.append("random")
    patterns.append("Choice a Pattern")

get_patterns(path)
randomize(grid_model, width, height)

def next_gen():
    global grid_model, next_grid_model

    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            count = count_neightbors(grid_model, i, j)

            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count ==3 or count == 2:
                    cell = 1

            next_grid_model[i][j] = cell

    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp

def count_neightbors(grid, r, c):
    count = 0
    if r-1 >= 0:
        count += grid[r-1][c]
    if r -1 >= 0 and c -1 >= 0:
        count += grid[r-1][c-1]
    if r - 1>=0 and c+1 < width:
        count += grid[r-1][c+1]
    if c -1 >= 0:
        count += grid[r][c-1]
    if c+1 < width:
        count += grid[r][c+1]
    if r+1 < height:
        count += grid[r+1][c]
    if r +1 < height and c-1 >= 0:
        count += grid[r+1][c-1]
    if r +1 <height and c+1 <width:
        count += grid[r+1][c+1]

    return count
    
def get_pattern(path, pattern_num):
    filename = path+f"\pattern{pattern_num}.txt"
    with open(filename, "r") as pattern_file:
        pattern = []
        for line in pattern_file:
            pattern.append(list(map(int, list(line[:-2]))))
    return pattern


def load_pattern(pattern, x_offset = 0, y_offset = 0):
    global grid_model

    for i in range(0, height):
        for j in range(0, width):
            grid_model[i][j] = 0
    
    j = y_offset
    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value

            i +=1
        j += 1

def count_files(path):
    c = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    return c

def set_new_pattern(grid):
    global path
    count = count_files(path)
    new_file = path+f"\pattern{count+1}.txt"
    print(new_file)
    with open(new_file, "a") as new_pattern:
        for i in grid:
            line = ""
            line = line.join(map(str, i)) + "\n"
            new_pattern.write(line)
        print("saved")

        


    
