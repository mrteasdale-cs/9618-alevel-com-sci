from typing import List, Tuple, Set, Dict

def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Get valid neighboring positions."""
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in directions:
        new_x, new_y = position[0] + dx, position[1] + dy

        # Check if position is within grid bounds and walkable
        if (0 <= new_x < len(grid) and
                0 <= new_y < len(grid[0]) and
                grid[new_x][new_y] == 0):
            neighbors.append((new_x, new_y))

    return neighbors


def get_lowest_f_score_node(open_set: Set[Tuple[int, int]], f_score: Dict[Tuple[int, int], float]) -> Tuple[int, int]:
    """Find the node with the lowest f_score in the open set."""
    return min(open_set, key=lambda x: f_score.get(x, float('inf')))


def a_star(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Implementation of A* pathfinding algorithm without using heapq.
    Returns the path from start to goal if found, otherwise returns empty list.
    """
    # Initialize the open and closed sets
    open_set = {start}
    closed_set = set()

    # Keep track of path and costs
    came_from = {}
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal)}

    while open_set:
        # Get node with lowest f_score
        current = get_lowest_f_score_node(open_set, f_score)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_set.remove(current)
        closed_set.add(current)

        # Check all neighbors
        for neighbor in get_neighbors(current, grid):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, goal)
                open_set.add(neighbor)

    return []  # No path found


def print_grid(grid: List[List[int]]) -> None:
    """Print the initial grid."""
    symbols = {0: ".", 1: "█", 2: "●"}
    for row in grid:
        print(" ".join(symbols[cell] for cell in row))


def print_path(grid: List[List[int]], path: List[Tuple[int, int]]) -> None:
    """Visualise path on the grid."""
    # Create a copy of the grid
    result_grid = [row[:] for row in grid]

    # Mark the path
    for pos in path:
        result_grid[pos[0]][pos[1]] = 2

    # Print the grid with path
    symbols = {0: ".", 1: "█", 2: "●"}
    for row in result_grid:
        print(" ".join(symbols[cell] for cell in row))


def main():
    # Example grid (0: walkable, 1: obstacle)
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    print("Initial Grid:")
    print_grid(grid)
    print("\nFinding path from", start, "to", goal, "...")

    path = a_star(grid, start, goal)

    if path:
        print("\nPath found!")
        print("Path:", path)
        print("\nVisualised path:")
        print_path(grid, path)
    else:
        print("\nNo path found!")


if __name__ == "__main__":
    main()