grid = []
with open("input4.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

DIRECTIONS = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Diagonal down-right
    (1, -1),  # Diagonal down-left
    (-1, 1),  # Diagonal up-right
    (-1, -1)  # Diagonal up-left
]

def check_word(row, col, direction):
    word = "XMAS"
    for i in range(len(word)):
        new_row = row + i * direction[0]
        new_col = col + i * direction[1]
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        if grid[new_row][new_col] != word[i]:
            return False
    return True

def matrix_search():
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            for direction in DIRECTIONS:
                if check_word(row, col, direction):
                    count += 1
                    print(f"Found 'XMAS' starting at ({row}, {col}) in direction {direction}")
    return count

# Run the search and print the result
result = matrix_search()
print(f"Total occurrences of 'XMAS': {result}")