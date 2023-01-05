# load input
with open(r'Day 5) Supply Stacks\5_puzzle_input.txt','r') as f:
    data = f.read().split('\n')

# Part One
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
# print('+++++++++')
# print(procedure)

stacks = {}
for index,stack_number in enumerate(initial[-1]):
    boxes = []
    for row in initial[:-1]:
        if row[index] != "":
            boxes.append(row[index])
    stacks[stack_number] = boxes
# print(stacks)

for step in procedure:
    number, frm, to = step
    number = int(number)
    for repeat in range(number):
        box = stacks[frm][0]
        stacks[frm] = stacks[frm][1:]
        stacks[to] = [box] + stacks[to]
# print(stacks)

out = ""
for item in stacks.items():
    out += item[1][0]
print(out)

