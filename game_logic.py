def compress_and_merge(line):
    new_line = [i for i in line if i != 0]
    changed = False
    i = 0
    while i < len(new_line) - 1:
        if new_line[i] == new_line[i + 1]:
            new_line[i] *= 2
            del new_line[i + 1]
            new_line.append(0)
            changed = True
            i += 1
        else:
            i += 1
    new_line += [0] * (len(line) - len(new_line))
    if new_line != line:
        changed = True
    return new_line, changed

def move(grid, direction):
    moved = False
    size = len(grid)

    if direction == 'up':
        for col in range(size):
            column = [grid[row][col] for row in range(size)]
            new_col, changed = compress_and_merge(column)
            if changed:
                moved = True
            for row in range(size):
                grid[row][col] = new_col[row]

    elif direction == 'down':
        for col in range(size):
            column = [grid[row][col] for row in reversed(range(size))]
            new_col, changed = compress_and_merge(column)
            if changed:
                moved = True
            for row, val in zip(reversed(range(size)), new_col):
                grid[row][col] = val

    elif direction == 'left':
        for row in range(size):
            new_row, changed = compress_and_merge(grid[row])
            if changed:
                moved = True
            grid[row] = new_row

    elif direction == 'right':
        for row in range(size):
            reversed_row = list(reversed(grid[row]))
            new_row, changed = compress_and_merge(reversed_row)
            if changed:
                moved = True
            grid[row] = list(reversed(new_row))

    return moved

def can_move(grid):
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:
                return True
            if col + 1 < size and grid[row][col] == grid[row][col + 1]:
                return True
            if row + 1 < size and grid[row][col] == grid[row + 1][col]:
                return True
    return False