
# Reading input from file
with open(r'Day 2) Rock Paper Scissors\2_puzzle_input.txt',"r") as f:
    data = f.read().split('\n')

# Part One

# Dictinoary for opponent's moves
opponent = {
    "A":"r",
    "B":"p",
    "C":"s",
}

# Dictinoary for my moves
me = {
    "X":"r",
    "Y":"p",
    "Z":"s",
}

win_condition = {
    "r":"p",
    "p":"s",
    "s":"r",
}

# Dictionary with Points for shape
point = {
    "X":1,
    "Y":2,
    "Z":3,
}

score = 0
for i in data:
    oppo_move, my_move = i.split(' ')
    score = score + point[my_move]
    if (opponent[oppo_move] == me[my_move]):
        # Draw
        score += 3
    elif (win_condition[opponent[oppo_move]] ==
          me[my_move]):
        # Won
        score += 6
    else:
        # Lost
        score += 0

print("Part One:", score)

# Part Two
# Defining dictionaries again to avoid confusion

# Dictinoary for opponent's moves
opponent = {
    "A":"r",
    "B":"p",
    "C":"s",
}
# my move to loose
me_loose = {
    "p":"r",
    "s":"p",
    "r":"s",
}

# my move to draw is redundant as
# I will have the same move as opponent's

# my move to win
me_win = {
    "r":"p",
    "p":"s",
    "s":"r",
}

# Dictionary with Points for move
point = {
    "r":1,
    "p":2,
    "s":3,
}

score = 0
for i in data:
    oppo_move, required = i.split(' ')
    if (required == "X"):
        # need to loose
        score += 0 # for loosing
        score += point[me_loose[opponent[oppo_move]]]
    elif (required == "Y"):
        # need to draw
        score += 3 # for drawing
        score += point[opponent[oppo_move]]
    else:
        # need to win
        score += 6
        score += point[me_win[opponent[oppo_move]]]

print("Part Two:", score)