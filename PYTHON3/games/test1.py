   def get_patterns(self):
        """
        Обновляет словарь паттернов
        """
        self.patterns_names = os.listdir(self.path)
        for name in self.patterns_names:
            filename = self.path+os.sep+name
            with open(filename, "r") as pattern_file:
                pattern = []
                for line in pattern_file:
                    pattern.append(list(map(int, list(line[:-2]))))
                self.patterns[name] = pattern

    def load_pattern_to_grid_model(self, pattern, x_offset=0, y_offset=0):
        """
        Переопределяет модель в соответствии с паттерном
        """
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

    def save_new_pattern(self):
        """
        Сохраняет паттерн существующей модели
        """
        count = len([f for f in os.listdir(self.path)
                    if os.path.isfile(os.path.join(self.path, f))])
        new_file = self.path+os.sep+f"pattern{count+1}.txt"
        with open(new_file, "a") as new_pattern:
            for i in self.grid_model:
                line = ""
                line = line.join(map(str, i)) + "\n"
                new_pattern.write(line)

            self.patterns[f"pattern{count+1}.txt"] = list(self.grid_model)
            self.patterns_names.append(f"pattern{count+1}.txt")
            self.patterns_names.sort()
            print("saved")

    def give_pattern(self, name):
        if name in self.patterns_names:
            return self.patterns[name]
        else:
            print("Weren't found")
            print(name)
            exit()
