with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

calories = 0
elves = []

for line in lines:
    if line:
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0
print(max(elves))

elves.sort()
print(sum(elves[-3:]))
