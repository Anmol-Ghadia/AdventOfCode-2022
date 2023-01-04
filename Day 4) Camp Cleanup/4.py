# load input
with open(r'Day 4) Camp Cleanup\4_puzzle_input.txt','r') as f:
    data = f.read().split('\n')

# Part One
total_1 = 0
for pair in data:
    sections = pair.replace("-",",").split(",")
    new_sections = []
    for sec in sections:
        new_sections.append(int(sec))
    if ((new_sections[0] <= new_sections[2] and 
         new_sections[1] >= new_sections[3]) or
        (new_sections[0]>= new_sections[2] and 
         new_sections[1]<= new_sections[3])):
        total_1 += 1

print("Part One:", total_1)

# Part Two
total_2 = 0
for pair in data:
    sections = pair.replace("-",",").split(",")
    new_sections = []
    for sec in sections:
        new_sections.append(int(sec))
    if ((new_sections[0] < new_sections[2] and
         new_sections[1] < new_sections[2]) or
         (new_sections[0] > new_sections[3] and
         new_sections[1] > new_sections[3])):
        continue
    total_2 += 1

print("Part Two:", total_2)