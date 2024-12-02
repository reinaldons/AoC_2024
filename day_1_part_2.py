from collections import Counter


#
# Read the file and extract numbers while calculating total similarity score
#
def calculate_total_similarity_score(filename):
    left_list = []
    right_counter = Counter()

    with open(filename) as file:
        for line in file:
            # Split the line into two parts separated by exactly 3 spaces
            left_str, right_str = line.strip().split('   ')
            left_list.append(int(left_str))
            right_counter[int(right_str)] += 1

    similarity_count = 0
    for num in left_list:
        # sum of left number multiplied by number of occurrences in the right list
        similarity_count += num * right_counter[num]

    return similarity_count


result = calculate_total_similarity_score("day_1_input.txt")

print(f"The total similarity count is: {result}")



