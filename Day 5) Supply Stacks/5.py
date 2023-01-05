# load input
with open(r'Day 5) Supply stacks\5_puzzle_input.txt','r') as f:
    data = f.read().split('\n')

initial = []
procedure = []
split = False
for row in data:
    if row == "":
        split = True
        continue
    if split:
        procedure.append(row
                        .replace("move ","")
                        .replace(" from ",".")
                        .replace(" to ",".")
                        .split("."))
        continue
    else:
        new_row = []
        for index,ele in enumerate(row):
            if index%4 in [0,2,3]:
                continue
            else:
                if ele == " ":
                    new_row.append("")
                else:
                    new_row.append(ele)
        initial.append(new_row)
# print(initial)
# print(procedure)

stacks = {}
for index,stack_number in enumerate(initial[-1]):
    boxes = []
    for row in initial[:-1]:
        if row[index] != "":
            boxes.append(row[index])
    stacks[stack_number] = boxes
# print(stacks)

# Part One
stacks_1 = stacks.copy()

for step in procedure:
    number, frm, to = step
    number = int(number)
    for repeat in range(number):
        box = stacks_1[frm][0]
        stacks_1[frm] = stacks_1[frm][1:]
        stacks_1[to] = [box] + stacks_1[to]
# print(stacks_1)

out_1 = ""
for item in stacks_1.items():
    out_1 += item[1][0]
print("Part One:", out_1)

# Part Two
stacks_2 = stacks.copy()

for step in procedure:
    number, frm, to = step
    number = int(number)
    boxes = stacks_2[frm][0:number]
    stacks_2[frm] = stacks_2[frm][number:]
    stacks_2[to] = boxes + stacks_2[to]
    # print(stacks_2)

out_2 = ""
for item in stacks_2.items():
    out_2 += item[1][0]
print("Part Two:", out_2)