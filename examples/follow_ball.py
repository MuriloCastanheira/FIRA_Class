import sys
sys.path.insert(0,"src")
from Communication import Communication
from go_to import go_to

while True:
    ball = Communication().ball()
    go = go_to(0, True, ball.x, ball.y, 0)
    go.go_to()
