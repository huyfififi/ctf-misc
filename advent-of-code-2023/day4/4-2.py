# https://adventofcode.com/2023/day/4#part2

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

# check the matches and calculate the number of cards
num_same_cards = [1] * len(cards)

for i in range(len(cards)):
    winning_numbers, numbers_in_hand = cards[i][0], cards[i][1]
    num_matches = len(winning_numbers & numbers_in_hand)
    for j in range(num_matches):
        if i + j + 1 >= len(num_same_cards):
            continue
        num_same_cards[i + j + 1] += num_same_cards[i]

# print(num_same_cards)
result = sum(num_same_cards)

print(f"{result=}")
