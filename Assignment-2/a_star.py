import math

DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def moveGen(pos, n, grid):
    x, y = pos
    for dx, dy in DIRECTIONS:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            yield (nx, ny)

def reconstruct_path(parent, start, goal):
    if goal not in parent and goal != start:
        return []
    path = []
    cur = goal
    while cur in parent:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()
    return path

def a_star_search(grid):
    n = len(grid)
    start, goal = (0,0), (n-1,n-1)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    open_list = [start]
    parent = {}
    g_cost = {start: 0}

    while open_list:
        current = min(open_list, key=lambda x: g_cost[x] + heuristic(x, goal))
        open_list.remove(current)

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return len(path), path

        for neighbor in moveGen(current, n, grid):
            new_cost = g_cost[current] + 1
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return -1, []


if __name__ == "__main__":
    print("Example 1:")
    grid1 = [[0,1],[1,0]]
    print("A* Search  →", a_star_search(grid1))

    print("\nExample 2:")
    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    print("A* Search  →", a_star_search(grid2))

    print("\nExample 3:")
    grid3 = [[1,0,0],[1,1,0],[1,1,0]]
    print("A* Search  →", a_star_search(grid3))
