import sys

sys.stdin = open("input_file.txt")
sys.stdout = open("output_file.txt", "w")
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
num_inputs = int(input())  # read a line with a single integer
print(num_inputs)

for test_case in range(1, num_inputs + 1):
    digits = [s for s in input().split(" ")]
    digits = list(map(list, digits))
    depth_string = ""
    for j in range(len(digits[0]) - 1):
        if not depth_string:
            depth_string + ("(" * int(digits[0][j])) + str(digits[0][j])
        else:
            close_parens = int(digits[0][j-1]) - int(digits[0][j])
            depth_string + (")" * close_parens) + digits[0][j]
            if (j == len(digits[0]) - 1):
                depth_string + (")" * int(digits[0][j]))

    print("Case #{}: {}".format(test_case, depth_string))