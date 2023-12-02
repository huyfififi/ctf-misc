# https://adventofcode.com/2023/day/1
import string


with open("input.txt", "r") as f:
    calibration_values = []
    for line in f:
        first_digit = None
        last_digit = None
        for c in line:
            if c not in string.digits:
                continue
            first_digit = first_digit or c
            last_digit = c
        calibration_values.append(int(first_digit + last_digit))
    print(f"result: {sum(calibration_values)}")
