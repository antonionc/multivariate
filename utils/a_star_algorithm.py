import heapq

def a_star_algorithm(start, goal, h, neighbors):
    open_list = []
    heapq.heappush(open_list, (0 + h(start), start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h(start)}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + 1  # Assuming each edge has a cost of 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

# Example heuristic function (Manhattan distance for grid-based pathfinding)
def heuristic(node, goal=(5, 5)):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Example neighbors function for a grid-based pathfinding
def neighbors(node):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = []
    for dir in dirs:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        result.append(neighbor)
    return result

if __name__ == "__main__":
    start = (0, 0)
    goal = (5, 5)
    path = a_star_algorithm(start, goal, lambda node: heuristic(node, goal), neighbors)
    print("Path found:", path)
