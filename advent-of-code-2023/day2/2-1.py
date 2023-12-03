NUM_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


file = open("input.txt", "r")
games = file.readlines()

result = 0

for game in games:
    game_prefix, plays = game.strip().split(": ")
    game_count = game_prefix.split()[1]
    plays = plays.split("; ")
    impossible = False
    for play in plays:  # because the number of plays is small, I don't add additional continue
        for cube in play.split(", "):
            num, color = cube.split(" ")
            if int(num) > NUM_CUBES[color]:
                impossible = True
                break

    if not impossible:
        result += int(game_count)

print(f"{result=}")

file.close()
