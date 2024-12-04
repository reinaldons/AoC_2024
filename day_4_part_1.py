def read_grid(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1)  # Up-Left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y):
        count = 0

        for dx, dy in directions:
            nx, ny = x, y
            has_match = True
            for k in range(len(target)):
                if not is_valid(nx, ny) or grid[nx][ny] != target[k]:
                    has_match = False
                    break

                nx += dx
                ny += dy

            if has_match:
                count += 1

        return count

    total_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "X":
                total_count += search(i, j)

    return total_count


result = count_xmas(read_grid("day_4_input.txt"))

print(f"Total number of XMAS: {result}")
