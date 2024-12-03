import re


def sum_valid_enabled_mul(filename):
    # Regular expressions for the instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

    max_product = 0
    enabled = True  # Instructions are enabled/disabled

    with open(filename) as file:
        content = file.read()

    # Tokenize the instructions and process sequentially
    instructions = re.split(r"(?=do\(\)|don't\(\))", content)

    for instruction in instructions:
        if instruction.startswith("do()"):
            enabled = True
        elif instruction.startswith("don't()"):
            enabled = False

        if enabled:
            for match in mul_pattern.finditer(instruction):
                x, y = map(int, match.groups())
                max_product += x * y

    return max_product

result = sum_valid_enabled_mul("day_3_input.txt")
print(f"Total sum of valid enabled multiplications is: {result}")



