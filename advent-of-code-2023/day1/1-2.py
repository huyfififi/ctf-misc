# https://adventofcode.com/2023/day/1#part2
import string


with open("input.txt", "r") as f:
    calibration_values = []
    for line in f:
        characters = list(line.strip())
        first_digit = None
        last_digit = None
        for i, c in enumerate(characters):
            # still considering more concise ways to do this
            if c in string.digits:
                first_digit = first_digit or c
                last_digit = c
            elif "".join(characters[i : i + 3]) == "one":
                first_digit = first_digit or "1"
                last_digit = "1"
            elif "".join(characters[i : i + 3]) == "two":
                first_digit = first_digit or "2"
                last_digit = "2"
            elif "".join(characters[i : i + 5]) == "three":
                first_digit = first_digit or "3"
                last_digit = "3"
            elif "".join(characters[i : i + 4]) == "four":
                first_digit = first_digit or "4"
                last_digit = "4"
            elif "".join(characters[i : i + 4]) == "five":
                first_digit = first_digit or "5"
                last_digit = "5"
            elif "".join(characters[i : i + 3]) == "six":
                first_digit = first_digit or "6"
                last_digit = "6"
            elif "".join(characters[i : i + 5]) == "seven":
                first_digit = first_digit or "7"
                last_digit = "7"
            elif "".join(characters[i : i + 5]) == "eight":
                first_digit = first_digit or "8"
                last_digit = "8"
            elif "".join(characters[i : i + 4]) == "nine":
                first_digit = first_digit or "9"
                last_digit = "9"
        calibration_values.append(int(first_digit + last_digit))
    print(f"result: {sum(calibration_values)}")
