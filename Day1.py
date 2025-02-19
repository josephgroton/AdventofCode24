from collections import Counter
# Creating two empty lists for later
left_list = []
right_list = []
# Opening the file in read mode, looping through the lines and splitting them into the two lists I made in the beginning
with open("input1.txt", "r") as file:
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
#sorting lists
left_list.sort()
right_list.sort()

total_difference = 0
for num in range(len(left_list)):
    total_difference += abs(left_list[num] - right_list[num])
# print(total_difference)

# Part 2: Finding "similarity score" aka how many times a number is repeated multipled by the amount of times it is present
left_counts = Counter(left_list)
right_counts = Counter(right_list)

similarity_score = 0
for num in left_list:
    left_count_in_right = right_counts.get(num, 0)
    similarity_score += num * left_count_in_right 

print(similarity_score)