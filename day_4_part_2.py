def read_grid(filename):
    return [line.strip() for line in open(filename)]


def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def is_x_mas(cx, cy, positions):
        return all(is_valid(cx + dx, cy + dy) and grid[cx + dx][cy + dy] == char for dx, dy, char in positions)

    patterns = [
        [(-1, -1, 'M'), (-1, 1, 'S'), (0, 0, 'A'), (1, -1, 'M'), (1, 1, 'S')],  # normal
        [(-1, -1, 'S'), (-1, 1, 'M'), (0, 0, 'A'), (1, -1, 'S'), (1, 1, 'M')],  # flipped
        [(-1, -1, 'S'), (-1, 1, 'S'), (0, 0, 'A'), (1, -1, 'M'), (1, 1, 'M')],  # top S
        [(-1, -1, 'M'), (-1, 1, 'M'), (0, 0, 'A'), (1, -1, 'S'), (1, 1, 'S')]   # top M
    ]

    count = sum(
        any(is_x_mas(i, j, pattern) for pattern in patterns)
        for i in range(1, rows - 1) for j in range(1, cols - 1)
    )

    return count


result = count_x_mas(read_grid("day_4_input.txt"))

print(f"Total number of X-MAS: {result}")
