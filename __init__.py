# Generation ID: Hutch_1763365786400_mphx94bbp (前半)

def myai(board, color):
    """
    オセロの最適な置き手を返す関数
    入力: board(6x6または8x8), color(1=白, 2=黒)
    出力: (column, row)
    """
    size = len(board)
    opponent = 3 - color

    # コーナーとその隣の位置
    corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
    corner_neighbors = [(0, 1), (1, 0), (1, size-1), (0, size-2),
                        (size-1, 1), (size-2, 0), (size-2, size-1), (size-1, size-2)]

    # T字位置（中央付近）
    t_positions = [(1, 2), (2, 1), (size-2, 1), (size-1, 2),
                   (1, size-2), (2, size-1), (size-2, size-2), (size-1, size-2)]

    valid_moves = []

    # すべての置ける位置を探索
    for row in range(size):
        for col in range(size):
            if board[row][col] == 0:
                flips = count_flips(board, col, row, color, opponent)
                if flips > 0:
                    valid_moves.append((col, row, flips))

    if not valid_moves:
        return None

    # 1. コーナーが取れるか
    for col, row, flips in valid_moves:
        if (col, row) in corners:
            return (col, row)

    # 2. T字位置（隣の角が置かれている場合のみ）
    for col, row, flips in valid_moves:
        if (col, row) in t_positions:
            for nc, nr in corner_neighbors:
                if board[nr][nc] == color:
                    return (col, row)

    # 3. コーナーの隣を避ける（隣の角が置かれていない場合）
    filtered_moves = [m for m in valid_moves if (m[0], m[1]) not in corner_neighbors]

    if filtered_moves:
        valid_moves = filtered_moves

    # 4. 最も多く石が取れる位置
    best_move = max(valid_moves, key=lambda x: x[2])
    return (best_move[0], best_move[1])


def count_flips(board, col, row, color, opponent):
    """
    指定位置に石を置いた時、取れる石の数を計算
    """
    size = len(board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_flips = 0

    for dx, dy in directions:
        flips = 0
        x, y = col + dx, row + dy

        while 0 <= x < size and 0 <= y < size and board[y][x] == opponent:
            flips += 1
            x += dx
            y += dy

        if 0 <= x < size and 0 <= y < size and board[y][x] == color and flips > 0:
            total_flips += flips

    return total_flips

# Generation ID: Hutch_1763365786400_mphx94bbp (後半)

board3=[
[0,0,0,2,0,1],
[0,1,1,2,2,0],
[0,1,1,2,1,2],
[0,1,1,2,1,0],
[0,0,0,2,0,0],
[0,0,0,0,0,0],
]
myosero(board3,1)
