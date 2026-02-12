def find_king(board):
    rows = len(board)
    cols = len(board[0])
    for y in range(rows):
        for x in range(cols):
            if board[y][x] == 'K':
                return (x, y)
    return None

# def find_rook(board):
#     rows = len(board)
#     cols = len(board[0])
#     for y in range(rows):
#         for x in range(cols):
#             if board[y][x] == 'R':
#                 return (x, y)
#     return None
# def find_pawn(board):
#     rows = len(board)
#     cols = len(board[0])
#     for y in range(rows):
#         for x in range(cols):
#             if board[y][x] == 'P':
#                 return (x, y)
#     return None

# def find_queen(board):
#     rows = len(board)
#     cols = len(board[0])
#     for y in range(rows):
#         for x in range(cols):
#             if board[y][x] == 'Q':
#                 return (x, y)
#     return None

# def find_bishop(board):
#     rows = len(board)
#     cols = len(board[0])
#     for y in range(rows):
#         for x in range(cols):
#                 if board[y][x] == 'B':
#                     return (x, y)
#         return None

def attack_by_rook(board, king_pos, rook_pos):
    kx, ky = king_pos
    rx, ry = rook_pos
    
    if kx != rx and ky != ry:
        return False

    step_x = 0 if kx == rx else (1 if kx > rx else -1)
    step_y = 0 if ky == ry else (1 if ky > ry else -1)
    
    curr_x, curr_y = rx + step_x, ry + step_y
    
    while (curr_x, curr_y) != (kx, ky):
        if board[curr_y][curr_x] != '.':
            return False
        curr_x += step_x
        curr_y += step_y
        
    return True

def attack_by_bishop(board, king_pos, bishop_pos):
    kx, ky = king_pos
    bx, by = bishop_pos

    if abs(kx - bx) != abs(ky - by):
        return False

    step_x = 1 if kx > bx else -1
    step_y = 1 if ky > by else -1
    
    curr_x, curr_y = bx + step_x, by + step_y
    
    while (curr_x, curr_y) != (kx, ky):
        if board[curr_y][curr_x] != '.':
            return False
        curr_x += step_x
        curr_y += step_y

    return True

def attack_by_queen(board, king_pos, queen_pos):
    return attack_by_rook(board, king_pos, queen_pos) or attack_by_bishop(board, king_pos, queen_pos)

def attack_by_pawn(king_pos, pawn_pos):
    kx, ky = king_pos
    px, py = pawn_pos
    if ky == py - 1 and abs(kx - px) == 1:
        return True
    return False

def checkmate(boards):
    board = [line.strip() for line in boards.strip().split('\n')]
        
    if not board:
        print("Fail")
        return

    rows = len(board)
    cols = len(board[0])
        
    for i in board:
       if len(i) != cols:
            print("Fail")
            return

    king_pos = find_king(board)
    # rook_pos = find_rook(board)
    # pawn_pos = find_pawn(board)
    # queen_pos = find_queen(board)
    # bishop_pos = find_bishop(board)
    if not king_pos:
        print("Fail")
        return

    for y in range(rows):
        for x in range(cols):
            piece = board[y][x]
            enemy_pos = (x, y)
            is_check = False

            if piece == 'R':
                is_check = attack_by_rook(board, king_pos, enemy_pos)
            elif piece == 'B':
                is_check = attack_by_bishop(board, king_pos, enemy_pos)
            elif piece == 'Q':
                is_check = attack_by_queen(board, king_pos, enemy_pos)
            elif piece == 'P':
                is_check = attack_by_pawn(king_pos, enemy_pos)
                
            if is_check:
                print("Success")
                return

    print("Fail")
