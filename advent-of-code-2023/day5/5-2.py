# https://adventofcode.com/2023/day/5#part2
# BRUTE_FORCE :angry:
# If I have a strong machine, this script will return the answer
# Please teach me how to solve this problem with a better way
import time
import math


maps = []
_map = []
seeds = []

f = open("input.txt", "r")
start = time.time()
for line in f:
    if not line.strip():
        pass

    elif line.startswith("seeds:"):
        _seeds = [int(x) for x in line.strip().split()[1:]]
        for i in range(0, len(_seeds), 2):
            seeds.append((_seeds[i], _seeds[i + 1]))

    elif line.strip().endswith("map:"):
        if _map:
            maps.append(_map)
            _map = []

    else:
        dst, src, _range = [int(x) for x in line.strip().split()]
        _map.append((dst, src, _range))

maps.append(_map)

_min = math.inf

for i, seed in enumerate(seeds):
    print(f"seed {i + 1} / {len(seeds)}", flush=True)
    for j in range(seed[1]):
        if j % 10000000 == 0:
            print(f"{j} / {seed[1]} {time.time() - start}", flush=True)
        num = seed[0] + j
        for _map in maps:
            for ops in _map:
                dst, src, _range = ops
                if src <= num <= src + _range:
                    num = dst + (num - src)
                    break
        _min = min(num, _min)

print(f"{time.time() - start}")
print(_min)
