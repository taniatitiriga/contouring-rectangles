import random

def random_rectangle():
    x1 = random.randrange(0, 100) / 10
    y1 = random.randrange(0, 100) / 10
    x2 = random.randrange(0, 100) / 10
    y2 = random.randrange(0, 100) / 10
    
    while True:
        if abs(x1 - x2) > 1 and abs(y1 - y2) > 1:
            break
        x2 = random.randrange(0, 100) / 10
        y2 = random.randrange(0, 100) / 10

    return x1, y1, x2, y2