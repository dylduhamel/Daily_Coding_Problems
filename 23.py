# Important Matrix 
# Use a BFS on the matrix, this is important because it uses a queue
# This code should run in O(M * N) time and space, since in the worst case we need to examine the entire board to find our target coordinate.


from collections import deque

# Givn a row and column, returns whether that tile is walkable
def walkable(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    # Board filled with t/f
    return not board[row][col]

# Given a row and col, returns list of valid neighbors
def get_walkable_neighbors(board, row, col):
    return [(r, c) for r, c in [
        (row, col -1),
        (row, col + 1), 
        (row - 1, col),
        (row + 1, col)]
        if walkable(board, r, c)
    ]

# Find shortest path with BFS
def shortest_path(board, start, end):
    seen = set()
    queue = deque([(start, 0)])
    while queue:
        coords, count = queue.popleft()
        if coords == end:
            return count
        seen.add(coords)
        neighbors = get_walkable_neighbors(board, coords[0], coords[1])
        queue.extend((neighbor, count + 1) for neighbor in neighbors if neighbor not in seen)

board = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]

print(shortest_path(board, (3, 0), (0, 0)))