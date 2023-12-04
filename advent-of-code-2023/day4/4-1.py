# https://adventofcode.com/2023/day/4

f = open("input.txt", "r")
cards = f.readlines()
f.close()

# no need to use two loops, but split it up for readability
for i in range(len(cards)):
    _, numbers = cards[i].strip().split(":")
    winning_numbers, numbers_in_hand = numbers.split("|")
    winning_numbers = set(int(x) for x in winning_numbers.split())
    numbers_in_hand = set(int(x) for x in numbers_in_hand.split())
    cards[i] = (winning_numbers, numbers_in_hand)
# print(cards)

# check the number of winning numbers and sum up the numbers
result = 0
for winning_numbers, numbers_in_hand in cards:
    num_matches = len(winning_numbers & numbers_in_hand)
    if num_matches == 0:
        continue
    result += 2 ** (num_matches - 1)

print(f"{result=}")
