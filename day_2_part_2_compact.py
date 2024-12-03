def count_safe_reports(filename):
    def is_safe(levels):
        diffs = [b - a for a, b in zip(levels, levels[1:])]

        return all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))

    def not_so_safe(levels):
        return any(is_safe(levels[:i] + levels[i + 1:]) for i in range(len(levels)))

    with open(filename) as file:
        return sum(not_so_safe(list(map(int, line.split()))) for line in file)


result = count_safe_reports("day_2_input.txt")
print(f"The number of safe reports is: {result}")
