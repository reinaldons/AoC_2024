def is_safe_report(levels):
    increasing = decreasing = True

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]

        if not (1 <= abs(diff) <= 3):
            return False

        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
        else:
            return False  # Adjacent levels are equal

    return increasing or decreasing


def count_safe_reports(filename):
    safe_count = 0

    with open(filename) as file:
        for line in file:
            levels = list(map(int, line.split()))

            if is_safe_report(levels):
                safe_count += 1

    return safe_count


result = count_safe_reports("day_2_input.txt")

print(f"The number of safe reports is: {result}")
