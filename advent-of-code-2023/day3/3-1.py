import string


# load input
engine_schematic = []

file = open("input.txt", "r")
for line in file.readlines():
    if stripped_line := line.strip():
        engine_schematic.append(list(stripped_line))
file.close()

print()
print("engine schematic")
for row in engine_schematic:
    print(row)

height = len(engine_schematic)
width = len(engine_schematic[0])

# create a matrix to store consecutive numbers
# ex [4, 6, 7, ., .] -> [AdjNum(467), AdjNum(467), AdjNum(467), None, None]


class AdjNum:
    def __init__(self, number):
        self.number = number
        self.considered = False

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

print()
print("num matrix")
for row in matrix:
    print(row)

# create flag matrix
# mark True if the point is adjacent to a synbol else False
flag_matrix = [[False for i in range(width)] for j in range(height)]

for row_i, row in enumerate(engine_schematic):
    for col_i, col in enumerate(row):
        if col not in string.digits and col != ".":
            # horizontal
            if row_i > 0:
                flag_matrix[row_i - 1][col_i] = True
            if row_i < height - 1:
                flag_matrix[row_i + 1][col_i] = True
            if col_i > 0:
                flag_matrix[row_i][col_i - 1] = True
            if col_i < width - 1:
                flag_matrix[row_i][col_i + 1] = True

            # diagonal
            if row_i > 0 and col_i > 0:
                flag_matrix[row_i - 1][col_i - 1] = True
            if row_i > 0 and col_i < width - 1:
                flag_matrix[row_i - 1][col_i + 1] = True
            if row_i < height - 1 and col_i > 0:
                flag_matrix[row_i + 1][col_i - 1] = True
            if row_i < height - 1 and col_i < width - 1:
                flag_matrix[row_i + 1][col_i + 1] = True

print()
print("flag matrix")
for row in flag_matrix:
    print(row)

result = 0
for row_i in range(height):
    for col_i in range(width):
        if not flag_matrix[row_i][col_i] or not matrix[row_i][col_i]:
            continue
        if not matrix[row_i][col_i].considered:
            result += matrix[row_i][col_i].number
            matrix[row_i][col_i].considered = True

print()
print(f"{result=}")
