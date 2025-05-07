import heapq

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search function
def astar(grid, start, goal):
    open_list = [(0, start)]
    came_from = {start: None}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0]+dx, current[1]+dy
            next = (nx, ny)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                new_cost = cost[current] + 1
                if next not in cost or new_cost < cost[next]:
                    cost[next] = new_cost
                    heapq.heappush(open_list, (new_cost + heuristic(next, goal), next))
                    came_from[next] = current
    return None

# ==== USER INPUT ====
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
grid = [[0]*cols for _ in range(rows)]

obstacles = int(input("Enter number of obstacles: "))
print("Enter obstacle positions (row col):")
for _ in range(obstacles):
    r, c = map(int, input().split())
    grid[r][c] = 1

print("Enter start position (row col):")
sx, sy = map(int, input().split())
print("Enter goal position (row col):")
gx, gy = map(int, input().split())

# ==== RUN ====
path = astar(grid, (sx, sy), (gx, gy))

# ==== OUTPUT ====
if path:
    print("\nPath found:")
    for p in path:
        print(p)
else:
    print("\nNo path found.")
