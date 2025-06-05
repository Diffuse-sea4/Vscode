import heapq

goal = [[1,2,3],[4,5,6],[7,8,0]]

def flatten(board):
    return tuple(num for row in board for num in row)

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def neighbors(board):
    x, y = find_zero(board)
    shifts = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []
    for dx, dy in shifts:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            result.append(new_board)
    return result

def heuristic(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                gx, gy = divmod(val - 1, 3)
                distance += abs(i - gx) + abs(j - gy)
    return distance

def solve_8_puzzle(start):
    visited = set()
    pq = [(heuristic(start), 0, start, [])]
    while pq:
        est, cost, state, path = heapq.heappop(pq)
        flat = flatten(state)
        if flat in visited:
            continue
        visited.add(flat)
        if state == goal:
            return path + [state]
        for neighbor in neighbors(state):
            heapq.heappush(pq, (cost + 1 + heuristic(neighbor), cost + 1, neighbor, path + [state]))
    return None
