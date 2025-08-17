grid = [
    ["#", "#", "#", "#", "#"],
    ["#", "S", "-", "T", "#"],
    ["#", "-", "T", "-", "#"],
    ["#", "-", "-", "-", "#"],
    ["#", "#", "#", "#", "#"]
]

start = None
tasks = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)  # row, column
        elif grid[i][j] == "T":
            tasks.append((i, j))

print("Start Position:", start)
print("Task Cells:", tasks)