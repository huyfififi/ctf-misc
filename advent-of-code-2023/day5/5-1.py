# https://adventofcode.com/2023/day/5

# for each map, convert prev to curr (e.g., seed -> soil)
prev = {}
curr = {}  # {number: is_mapped}

f = open("input.txt", "r")
for line in f:
    # print(line.strip())
    if not line.strip():
        pass

    elif line.startswith("seeds:"):
        curr = {int(x): False for x in line.strip().split()[1:]}

    elif line.strip().endswith("map:"):
        for number in prev.keys():
            if not prev[number]:  # any source numbers that aren't mapped correspond to the same destination
                curr[number] = False
        prev = curr
        curr = {}

    else:
        dst, src, _range = [int(x) for x in line.strip().split()]
        # this approach can take much time when the range is large
        # it can be finished in a finite time tho
        # for i in range(_range):
        #     if src + i in prev:
        #         prev[src + i] = True
        #         curr[dst + i] = False

        # looking at the input data, iterating sources is much faster
        for number in prev.keys():
            if src <= number < src + _range:
                prev[number] = True
                curr[number - src + dst] = False

f.close()

# for the last map
for number in prev.keys():
    if not prev[number]:
        curr[number] = False

result = min(curr.keys())
print(f"{result=}")
