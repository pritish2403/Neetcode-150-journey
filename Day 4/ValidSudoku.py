board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

valid = True

for r in range(9):
    for c in range(9):
        val = board[r][c]
        if val == ".":
            continue
        
        box_idx = (r // 3) * 3 + (c // 3)

        if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
            valid = False
            break

        rows[r].add(val)
        cols[c].add(val)
        boxes[box_idx].add(val)

    if not valid:
        break

print(valid)
