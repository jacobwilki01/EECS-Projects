import time

alphabet = "abcdefghijklmnopqrstuvwxyz"
term = input("")
output = ""
index = 0

while output != term:
    for char in alphabet:
        if index < len(term):
            if term[index] == " ":
                output += " "
                index += 1
            elif char == term[index]:
                output += char
                index += 1
                print(output)
            else:
                print(output + char)
        else:
            break
        time.sleep(.001)