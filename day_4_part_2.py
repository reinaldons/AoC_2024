def read_grid(filename):
      with open(filename) as file:
          return [line.strip() for line in file]


def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def is_x_mas(center_x, center_y):
        # go verbose, no smart moves
        normal_positions = [
            (center_x - 1, center_y - 1, 'M'),  # top-left
            (center_x - 1, center_y + 1, 'S'),  # top-right
            (center_x, center_y, 'A'),          # center
            (center_x + 1, center_y - 1, 'M'),  # bottom-left
            (center_x + 1, center_y + 1, 'S')   # bottom-right
        ]
        flipped_positions = [
            (center_x - 1, center_y - 1, 'S'),  # top-left
            (center_x - 1, center_y + 1, 'M'),  # top-right
            (center_x, center_y, 'A'),          # center
            (center_x + 1, center_y - 1, 'S'),  # bottom-left
            (center_x + 1, center_y + 1, 'M')   # bottom-right
        ]
        top_s_positions = [
            (center_x - 1, center_y - 1, 'S'),  # top-left
            (center_x - 1, center_y + 1, 'S'),  # top-right
            (center_x, center_y, 'A'),          # center
            (center_x + 1, center_y - 1, 'M'),  # bottom-left
            (center_x + 1, center_y + 1, 'M')   # bottom-right
        ]
        top_m_positions = [
            (center_x - 1, center_y - 1, 'M'),  # top-left
            (center_x - 1, center_y + 1, 'M'),  # top-right
            (center_x, center_y, 'A'),          # center
            (center_x + 1, center_y - 1, 'S'),  # bottom-left
            (center_x + 1, center_y + 1, 'S')   # bottom-right
        ]

        return (
            all(is_valid(x, y) and grid[x][y] == char for x, y, char in normal_positions) or
            all(is_valid(x, y) and grid[x][y] == char for x, y, char in flipped_positions) or
            all(is_valid(x, y) and grid[x][y] == char for x, y, char in top_s_positions) or
            all(is_valid(x, y) and grid[x][y] == char for x, y, char in top_m_positions)
        )

    count = 0
    # rows/cols - 1 to avoid grid edges
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if is_x_mas(i, j):
                count += 1

    return count


result = count_x_mas(read_grid("day_4_input.txt"))

print(f"Total number of X-MAS: {result}")
