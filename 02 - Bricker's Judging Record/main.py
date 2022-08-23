file = open("mytable (32).csv","r")

lines = []
for line in file:
    items = line.split(",")
    lines.append(items)

lines.pop(0)

total = 0
sat = 0
aff = 0
neg = 0
overall = 0

for line in lines:
    line[8] = line[8].strip()
    if len(line[8]) > 0:
        items = line[8].split()
        items[0] = items[0].strip('"')
        if line[7] != items[0]:
            sat += 1
        total += 1
    if line[7] == "Aff":
        aff += 1
    else:
        neg += 1
    overall += 1

print(f"Overall: {overall} | Elim Total: {total} | Sat: {sat} | Aff: {aff} | Neg: {neg}")
if aff > neg:
    print("This judge votes aff more often. They have voted aff %.2f%% of the time." % (100 * aff/overall))
    print(f"That comes out to {aff - neg} more aff votes than neg votes.")
else:
    print("This judge votes neg more often. They have voted neg %.2f%% of the time." % (100 * neg/overall))
    print(f"That comes out to {neg - aff} more neg votes than aff votes.")
print("This judge has sat %.2f%% of the elims they've judged." % (100 * sat/total))