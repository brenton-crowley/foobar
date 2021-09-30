from pprint import pprint

# Input: solution.solution(0, 1)
# Output: 3

# Input: solution.solution(19, 36)
# Output: 1

RELATIVE_MOVES = ((1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)) # tuple of tuples of possible knight moves from current.
board = []

def solution(src, dest):
    """
    src:    int between 0-63 starting position
    dest:   int between 0-63 target position
    """
    global board
    board = [[-1 for y in range(8)] for x in range(8)]
    queue = [] # a list of coordinates to check
    startCoords = get_coord(src)
    targetCoords = get_coord(dest)

    queue.append(startCoords)

    # We use relative moves to get the next set of coords to add to the queue

    set_start(startCoords)

    return find_moves(queue, targetCoords)

def get_coord(num):
    x = num // 8    # results in the row index
    y = num % 8     # results in the column index
    return (x, y)

def is_unvisited(coord):
    value = get_coord_value(coord)
    return False if value > -1 else True

def get_moves_for(coord):
    """
    coord: a tuple (x, y) where x, y is a value between 0-7
    """
    moves = []
    for dx, dy in RELATIVE_MOVES:
        x = coord[0] + dx
        y = coord[1] + dy

        if is_valid_move(x) and is_valid_move(y) and is_unvisited((x, y)):
            moves.append((x, y))

    return moves

# could move is_unvisited to here as this constitutes a valid move
def is_valid_move(num):
    """
    num: an int
    """
    return False if num < 0 or num > 7 else True

def set_start(coord):
    set_coord_value(coord, 0)

def set_coord_value(coord, value):
    x = coord[0]
    y = coord[1]
    board[x][y] = value

def get_coord_value(coord):
    x = coord[0]
    y = coord[1]
    return board[x][y]


def find_moves(queue, targetCoords):
    """
    1. get the first element from the queue and set to currentCoord
    - get the moves for that element
    - loop through moves and set a move value
        # increment whatever its num value is + 1. So for the first coord, which is 0
    - check that coord is unvisited
    - check if targetCoord is the coord being checked. If so, get that value as it's the one we need.
    """
    while len(queue) > 0:

    # put the code below into a repeating function and you just about have your solution
        currentCoord = queue.pop(0)
        moves = get_moves_for(currentCoord)
        for coord in moves:
            if is_unvisited(coord):
                current_value = get_coord_value(currentCoord)
                set_coord_value(coord, current_value+1)

            if coord == targetCoords:
                print(f"Target Reached. Min moves: {get_coord_value(coord)}")
                pprint(board)
                return get_coord_value(coord)

        queue += moves
    # repeat until the queue is empty or we reach the target coord
