file = open("input.txt", "r")
games = file.readlines()

result = 0

for game in games:
    game_prefix, plays = game.strip().split(": ")
    game_count = game_prefix.split()[1]
    plays = plays.split("; ")

    max_blue, max_green, max_red = 0, 0, 0
    max_count = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }
    for play in plays:
        for cube in play.split(", "):
            num, color = cube.split(" ")
            max_count[color] = max(max_count[color], int(num))

    result += max_count["blue"] * max_count["green"] * max_count["red"]

print(f"{result=}")

file.close()
