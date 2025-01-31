import random

def random_rectangle():
    x1 = random.randrange(0, 11)
    y1 = random.randrange(0, 11)
    x2 = random.randrange(0, 11)
    y2 = random.randrange(0, 11)
    
    while True:
        if abs(x1 - x2) > 1 and abs(y1 - y2) > 1:
            break
        x2 = random.randrange(0, 11)
        y2 = random.randrange(0, 11)

    return x1, y1, x2, y2