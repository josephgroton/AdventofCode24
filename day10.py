trails = []
with open("input10.txt", "r") as file:
    for line in file:
        trails.append([int(char) for char in line.strip()])

        

print(trails)


