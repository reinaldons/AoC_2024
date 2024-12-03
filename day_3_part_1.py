import re

def sum_valid_mul(filename):
    # Match valid 'mul(X,Y)' instructions
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    total_sum = 0

    with open(filename) as file:
        for line in file:
            for match in pattern.finditer(line):
                x, y = map(int, match.groups())
                if 1 <= x <= 999 and 1 <= y <= 999:
                    total_sum += x * y

    return total_sum


result = sum_valid_mul("day_3_input.txt")
print(f"Total sum of valid multiplications is: {result}")
