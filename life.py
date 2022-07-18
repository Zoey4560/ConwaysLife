import copy

Cell = list[list[int]]

class Life:
    cell: Cell

    def __init__(self, starting_cell: Cell):    # IMPROVEMENT: just trusting input? verify? use bool instead of int?
        self.cell = starting_cell
        

    def run_step(self):
        try:
            self.__pad_cell()
            self.cell = self.__generate_next_cell()
            self.__crop_cell()
        except IndexError:
            return # she's dead, jim
    
    def __generate_next_cell(self):
        new_cell = copy.deepcopy(self.cell)
        # Check neighbors and change state of new_cell
        for iy, row in enumerate(self.cell):
            for ix, val in enumerate(row):
                live_neighbors = self.__count_neighbors(ix, iy)
                if self.cell[iy][ix] == 0:
                    if live_neighbors == 3:
                        new_cell[iy][ix] = 1 # birth
                else:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_cell[iy][ix] = 0 # underpopulation & overpopulation
        return new_cell

    def __pad_cell(self):
        for row in self.cell:
            row.insert(0, 0)                        # left
            row.append(0)                           # right
        self.cell.insert(0, [0] * len(self.cell[0]))# top
        self.cell.append([0] * len(self.cell[0]))   # bottom

    def __crop_cell(self):
        # top
        while not any(self.cell[0]):
            del self.cell[0]
        # bottom
        while not any(self.cell[-1]):
            del self.cell[-1]
        # left
        while not any(row[0] for row in self.cell):
            for row in self.cell:
                del row[0]
        # right
        while not any(row[-1] for row in self.cell):
            for row in self.cell:
                del row[-1]

    def __count_neighbors(self, x, y):
        # scope cell down to only neighbor blocks; sum them all up.
        x_start = max(0, x - 1)
        x_end = min(len(self.cell[0]), x + 2) # +2 because arr[start:end] stops _before_ end
        y_start = max(0, y -1)
        y_end = min(len(self.cell), y + 2)
        
        count = 0 - self.cell[y][x]
        for row in self.cell[y_start:y_end]:
            count += sum(row[x_start:x_end])

        return count