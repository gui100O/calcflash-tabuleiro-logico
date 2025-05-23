# game_logic.py

def slide_row_left(row):
    new_row = [i for i in row if i != 0]
    new_row += [0] * (len(row) - len(new_row))
    return new_row

def combine_tiles(grid, direction):
    moved = False
    combined = False
    score = 0

    def transpose(g):
        return [list(row) for row in zip(*g)]

    def reverse(g):
        return [row[::-1] for row in g]

    temp_grid = [row[:] for row in grid]

    if direction in ['up', 'down']:
        temp_grid = transpose(temp_grid)
    if direction in ['right', 'down']:
        temp_grid = reverse(temp_grid)

    new_grid = []
    for row in temp_grid:
        row = slide_row_left(row)
        for i in range(len(row)-1):
            if row[i] != 0 and row[i] == row[i+1]:
                row[i] *= 2
                score += row[i]
                row[i+1] = 0
                combined = True
        row = slide_row_left(row)
        new_grid.append(row)

    if direction in ['right', 'down']:
        new_grid = reverse(new_grid)
    if direction in ['up', 'down']:
        new_grid = transpose(new_grid)

    if new_grid != grid:
        moved = True
        for r in range(4):
            for c in range(4):
                grid[r][c] = new_grid[r][c]

    return combined, moved, score

def can_combine(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                return True
            if r < 3 and grid[r][c] == grid[r+1][c]:
                return True
            if c < 3 and grid[r][c] == grid[r][c+1]:
                return True
    return False
