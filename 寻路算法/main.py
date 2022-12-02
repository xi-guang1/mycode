

puzzle = [[1,0,0,0,1],
          [1,1,1,0,1],
          [0,0,1,0,0],
          [0,0,1,1,0],
          [0,0,1,1,1]]

class now():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

point = now()

def check(now):
    return check_up(now)

def check_up(now):
    if now.y == 0:
        return check_down(now)
    elif puzzle[now.y - 1][now.x] == 1:
        now.y -= 1
        print(now.x,now.y)
        return now
    else:
        return check_down(now)
    
def check_down(now):
    if now.y == 4:
        return check_left(now)
    elif puzzle[now.y + 1][now.x] == 1:
        now.y += 1
        print(now.x,now.y)
        return now
    else:
        return check_left(now)
    
def check_left(now):
    if now.x == 0:
        return check_right(now)
    elif puzzle[now.y][now.x - 1] == 1:
        now.x -= 1
        print(now.x,now.y)
        return now
    else:
        return check_right(now)
    
def check_right(now):
    if now.x == 4:
        return
    elif puzzle[now.y][now.x + 1] == 1:
        now.x += 1
        print(now.x,now.y)
        return now
    else:
        return False

while point.x != 4 and point.y != 4:
    puzzle[point.x][point.y] = 2
    point = check(point)

print(point.x,point.y)
# check_up(point)