# Read the input file containing reports
levels = []
with open("input2.txt", "r") as file:
    for line in file:
        levels.append(list(map(int, line.strip().split())))

safe_count = 0
unsafe_count = 0

def is_safe(level):
    """Check if a report is safe."""
    # Check if the levels are sorted (either increasing or decreasing)
    if level == sorted(level) or level == sorted(level, reverse=True):
        # Check if all adjacent levels differ by at least 1 and at most 3
        for i in range(1, len(level)):
            if abs(level[i] - level[i-1]) < 1 or abs(level[i] - level[i-1]) > 3:
                return False
        return True
    return False

# First Pass: Check each report
unsafe_reports = []
for level in levels:
    if is_safe(level):
        safe_count += 1
    else:
        unsafe_reports.append(level)

# Second Pass: Try removing one level from unsafe reports and check again
for level in unsafe_reports:
    for i in range(len(level)):
        # Create a new level by removing the i-th element
        new_level = level[:i] + level[i+1:]
        if is_safe(new_level):
            safe_count += 1
            break  # No need to check further, as it is now safe after removal
    else:
        unsafe_count += 1  # If no removal makes it safe, count as unsafe

# Output the results
print(safe_count)
print(unsafe_count)
