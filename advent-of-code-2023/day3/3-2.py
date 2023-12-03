# https://adventofcode.com/2023/day/3#part2
import string


# load input
engine_schematic = []

file = open("input.txt", "r")
for line in file.readlines():
    if stripped_line := line.strip():
        engine_schematic.append(list(stripped_line))
file.close()

# for row in engine_schematic:
#     print(row)

height = len(engine_schematic)
width = len(engine_schematic[0])


# create a matrix to store consecutive numbers
# ex [4, 6, 7, ., .] -> [AdjNum(467), AdjNum(467), AdjNum(467), None, None]
class AdjNum:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"AdjNum({self.number})"


matrix = [[None for i in range(width)] for j in range(height)]

for row_i, row in enumerate(engine_schematic):
    fast_i = 0
    slow_i = 0
    while fast_i < width:
        if row[fast_i] in string.digits:
            fast_i += 1
        else:
            if slow_i != fast_i:
                adj_num = AdjNum(int("".join(row[slow_i:fast_i])))
                for j in range(slow_i, fast_i):
                    matrix[row_i][j] = adj_num
            fast_i += 1
            slow_i = fast_i
    if slow_i != fast_i:
        adj_num = AdjNum(int("".join(row[slow_i:fast_i])))
        for j in range(slow_i, fast_i):
            matrix[row_i][j] = adj_num

result = 0

# check all gears
for row_i in range(height):
    for col_i in range(width):
        if engine_schematic[row_i][col_i] != "*":
            continue

        part_numbers = {}

        if row_i > 0 and matrix[row_i - 1][col_i]:
            part_numbers[id(matrix[row_i - 1][col_i])] = matrix[row_i - 1][col_i]
        if row_i < height - 1 and matrix[row_i + 1][col_i]:
            part_numbers[id(matrix[row_i + 1][col_i])] = matrix[row_i + 1][col_i]
        if col_i > 0 and matrix[row_i][col_i - 1]:
            part_numbers[id(matrix[row_i][col_i - 1])] = matrix[row_i][col_i - 1]
        if col_i < width - 1 and matrix[row_i][col_i + 1]:
            part_numbers[id(matrix[row_i][col_i + 1])] = matrix[row_i][col_i + 1]

        if row_i > 0 and col_i > 0 and matrix[row_i - 1][col_i - 1]:
            part_numbers[id(matrix[row_i - 1][col_i - 1])] = matrix[row_i - 1][col_i - 1]
        if row_i > 0 and col_i < width - 1 and matrix[row_i - 1][col_i + 1]:
            part_numbers[id(matrix[row_i - 1][col_i + 1])] = matrix[row_i - 1][col_i + 1]
        if row_i < height - 1 and col_i > 0 and matrix[row_i + 1][col_i - 1]:
            part_numbers[id(matrix[row_i + 1][col_i - 1])] = matrix[row_i + 1][col_i - 1]
        if row_i < height - 1 and col_i < width - 1 and matrix[row_i + 1][col_i + 1]:
            part_numbers[id(matrix[row_i + 1][col_i + 1])] = matrix[row_i + 1][col_i + 1]

        if len(part_numbers) != 2:
            continue
        sub_product = 1
        for adj_num in part_numbers.values():
            sub_product *= adj_num.number
        result += sub_product

# print()
# print("num matrix")
# for row in matrix:
#     print(row)

# print()
print(f"{result=}")
