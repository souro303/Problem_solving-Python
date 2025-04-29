def find_square_coordinates(x1, y1, x2, y2):
    if x1 == x2:  # Vertical line
        side = abs(y2 - y1)
        return f"{x1 + side} {y1} {x2 + side} {y2}"
    elif y1 == y2:  # Horizontal line
        side = abs(x2 - x1)
        return f"{x1} {y1 + side} {x2} {y2 + side}"
    elif abs(x1 - x2) == abs(y1 - y2):  # Diagonal
        return f"{x1} {y2} {x2} {y1}"
    else:
        return "-1"

x1, y1, x2, y2 = map(int, input().split())
print(find_square_coordinates(x1, y1, x2, y2))
