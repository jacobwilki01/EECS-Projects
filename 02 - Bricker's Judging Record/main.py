file = open("mytable (19).csv","r")

lines = []
for line in file:
    items = line.split(",")
    lines.append(items)

lines.pop(0)


count = 0

for item in lines[0]:
    print(item)

for line in lines:
    if len(line) == 9:
        count += 1

print(count)