import random
import os

class GridModel():
    """
    Хранит информацию обо всей модели, в чаcности паттерны модели
    Также сохраняет паттерны и загружает их в модель 
    """
    patterns= []

    def __init__(self, width, height, path):
        self.grid_model = [[0]*width for i in range(height)]
        self.next_grid_model = self.grid_model

        self.width = width
        self.height = height
        self.path = path
        self.is_running = False

        self.get_patterns_names()
        self.randomize()

    def randomize(self):
        """
        Рандомно заполняет модель
        """
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.grid_model[i][j] = random.randint(0, 1)

    def update_grid(self):
        """
        Обновляет сетку в соответсвии с наличием соседей
        Если соседей <2, клетка умирает, если >3, клетка тоже умирает
        Также 3 клетки генерируют новую клетку
        """
        for i in range(0, self.height):
            for j in range(0, self.width):
                cell = 0
                count = self.count_neightbors(i, j)

                if self.grid_model[i][j] == 0:
                    if count == 3:
                        cell = 1
                elif self.grid_model[i][j] == 1:
                    if count ==3 or count == 2:
                        cell = 1

                self.next_grid_model[i][j] = cell
        self.grid_model, self.next_grid_model = self.next_grid_model, self.grid_model

    def count_neightbors(self, r, c):
        """
        Считает соседей клетки
        Вспомогательный метод
        """
        count = 0
        if r-1 >= 0:
            count += self.grid_model[r-1][c]
        if r -1 >= 0 and c -1 >= 0:
            count += self.grid_model[r-1][c-1]
        if r - 1>=0 and c+1 < self.width:
            count += self.grid_model[r-1][c+1]
        if c -1 >= 0:
            count += self.grid_model[r][c-1]
        if c+1 < self.width:
            count += self.grid_model[r][c+1]
        if r+1 < self.height:
            count += self.grid_model[r+1][c]
        if r +1 < self.height and c-1 >= 0:
            count += self.grid_model[r+1][c-1]
        if r +1 < self.height and c+1 <self.width:
            count += self.grid_model[r+1][c+1]

        return count

    def get_patterns_names(self):
        self.patterns = os.listdir(self.path)

    def save_new_pattern(self):
        num = len(self.patterns) + 1
        new_name = self.path + os.sep + "ptrn" + str(num) + ".txt"
        with open(new_name, "a") as pattern:
            pattern.write(str(self.width) + "/" + str(self.height) + "\n")
            for i in self.grid_model:
                pattern.write(''.join(list(map(str, i))) + "-")
            print("file writed")

        self.get_patterns_names()
        print("saved")

    def load_pattern_to_grid_model(self, name, x_offset=0, y_offset=0):

        pattern = self.give_pattern(name)
        
        if pattern == None:
            raise TypeError

        for i in range(0, self.height):
            for j in range(0, self.width):
                self.grid_model[i][j] = 0

        j = y_offset
        for row in pattern:
            i = x_offset
            for value in row:
                self.grid_model[i][j] = value

                i += 1
            j += 1

    def give_pattern(self, name):
        if name in self.patterns:
            with open(self.path + os.sep + name, "r") as new_pattern:
                line = new_pattern.readline().split("/")
                self.grid_model = [[0]*int(line[0]) for i in range(int(line[1]))]
                self.width = int(line[0])
                self.height = int(line[1])
                self.next_grid_model = list(self.grid_model)
                ptrn = new_pattern.read().split("-")
                ptrn[-1] = ptrn[-1][:-3]
                temp = []
                for x in ptrn:
                    temp.append(list(map(int, list(x))))


                return temp
        else:
            raise RuntimeError("werem't found this name")





