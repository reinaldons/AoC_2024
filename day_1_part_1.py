#
# Read the file and extract numbers while calculating total distance
#
def calculate_total_distance(filename):
    left_list = []
    right_list = []

    with open(filename) as file:
        for line in file:
            # Split the line into two parts separated by 3 spaces
            left, right = map(int, line.strip().split('   '))
            left_list.append(left)
            right_list.append(right)

    # Sort both lists in place
    left_list.sort()
    right_list.sort()

    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


result = calculate_total_distance("day_1_input.txt")

print(f"The total distance is {result}")
