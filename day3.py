import re
pattern = r"mul\(\d+,\d+\)"

matches = []
with open("input3.txt", "r") as file: 
    for line in file:
        matches.extend(re.findall(pattern, line))

results = []

for match in matches:
    numbers = re.findall(r"\d+", match)
    results.append(int(numbers[0]) * int(numbers[1]))

total_sum = sum(results)
print(total_sum)