def move(player, direction):
      x, y, hp = player
      xmove, ymove = direction
      x += xmove
      y += ymove
      if x < 0:
            x = 0
            hp -= 5
      if y < 0:
            y = 0
            hp -= 5
      if x > 9:
            x = 9
            hp -= 5
      if y > 9:
            y = 9
            hp -= 5      
      return x, y, hp
      
print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))