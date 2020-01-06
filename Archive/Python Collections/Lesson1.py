def move(player, direction):
        x, y, hp = player
        xmove, ymove = direction
        x += xmove
        y += ymove
        if 1 > x:
                x = 0
                hp -= 5
        if 1 > y:
                y = 0
                hp -= 5
        return x, y, hp
print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))