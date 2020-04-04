# python3 solution.py < input_file.txt > output_file.txt
import sys

# sys.stdin = open("input_file.txt")
# sys.stdout = open("output_file.txt", "w")
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
num_inputs = int(input())  # read a line with a single integer

for test_case in range(1, num_inputs + 1):
    square_inputs = int(input())
    construct_matrix = []
    # construct our matrix from the input
    for j in range(square_inputs):
        construct_matrix.append([int(s) for s in input().split(" ")])
    # process repeats in row
    row_repeat = 0
    col_repeat = 0
    trace_sum = 0
    for row in construct_matrix:
        if len(set(row)) != len(row):
            row_repeat += 1 
    for col in zip(*construct_matrix):
        if len(set(col)) != len(col):
            col_repeat += 1
    for num in range(square_inputs):
        trace_sum += construct_matrix[num][num]

    print("Case #{}: {} {} {}".format(test_case, trace_sum, row_repeat, col_repeat))
