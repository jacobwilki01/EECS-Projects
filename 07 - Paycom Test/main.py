x = 2437
y = 875

while x != y:
    if x > y:
        x -= y
    else:
        y -= x

print(f"result={x}")