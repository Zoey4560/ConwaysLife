import copy

def get_generation(og_cells, generations):
    cells = copy.deepcopy(og_cells) #prevent modification of input cells
    
    for _ in range(generations):
        # Pad for expansion
        pad_cells(cells)
        
        # Create working copy
        new_cells = copy.deepcopy(cells)
        
        # Check neighbors and change state of new_cells
        for iy, row in enumerate(cells):
            for ix, val in enumerate(row):
                live_neighbors = count_neighbors(cells, ix, iy)
                if cells[iy][ix] == 0:
                    if live_neighbors == 3:
                        new_cells[iy][ix] = 1 # birth
                else:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_cells[iy][ix] = 0 # underpopulation & overpopulation
                        
        # Crop to living cells and set to cells for next generation
        still_cropping = True
        while still_cropping:
            still_cropping = crop_cells(new_cells)
        cells = new_cells

    return cells



def pad_cells(cells):
    #note: mutates
    for row in cells:
        row.insert(0, 0)                # left
        row.append(0)                   # right
    cells.insert(0, [0] * len(cells[0]))# top
    cells.append([0] * len(cells[0]))   # bottom
    
def crop_cells(cells):
    #note: mutates; returns if it cropped
    cropped = False
    # top
    if sum(cells[0]) == 0:
        del cells[0]
        cropped = True
    # bottom
    if sum(cells[-1]) == 0:
        del cells[-1]
        cropped = True
    # left
    if sum(row[0] for row in cells) == 0:
        for row in cells:
            del row[0]
        cropped = True
    # right
    if sum(row[-1] for row in cells) == 0:
        for row in cells:
            del row[-1]
        cropped = True
    return cropped
    
def count_neighbors(cells, ix, iy):
    # cut cells down to only neighbor blocks; sum them all up.
    x_start = max(0, ix - 1)
    x_end = min(len(cells[0]), ix + 2) # +2 because arr[start:end] stops _before_ end
    y_start = max(0, iy -1)
    y_end = min(len(cells), iy + 2)
    
    count = 0 - cells[iy][ix]
    for row in cells[y_start:y_end]:
        count += sum(row[x_start:x_end])

    return count

    
""" 
test.describe('count_life')
test.it('counts empty')
empty = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
test.expect(0 == count_neighbors(empty, 1, 1))
test.expect(0 == count_neighbors(empty, 0, 0))
test.expect(0 == count_neighbors(empty, 2, 2))

test.it('counts full')
full = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
test.expect(8 == count_neighbors(full, 1, 1))
test.expect(3 == count_neighbors(full, 0, 0))
test.expect(5 == count_neighbors(full, 1, 0))
test.expect(3 == count_neighbors(full, 2, 2))

test.it('counts big')
big_empty = [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]
test.expect(0 == count_neighbors(big_empty, 2, 2))
big_full = [[0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]
test.expect(8 == count_neighbors(big_full, 2, 2))
"""
