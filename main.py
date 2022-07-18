from os import environ
from random import randint
import time
from life import Life


def garbage_visualize(env: Life):
    print("\033[H\033[J", end="")
    for row in env.cell:
        print(''.join(map(lambda x: '  ' if x == 0 else ' o', row)))


glider = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

expand = [
    [1, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1]
]

diagonal = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

ded = [[1]]


randomish = [
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1]
]

r_pentomino = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 1, 0]
]

diehard = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1]
]

growth = [[1]*8 + [0] + [1]*5 + [0]*3 + [1]*3 + [0]*6 + [1]*7 + [0] + [1]*5]

switch_engine = [
    [0]*11 + [1, 0, 1, 0, 0],
    [1, 1] + [0]*8 + [1] + [0]*5,
    [1, 1] + [0]*9 + [1, 0, 0, 1, 0],
    [0]*13 + [1]*3
]


random = [[randint(0,1) for _ in range(10)] for _ in range(10)]



environment = Life(random)

print("initial")
garbage_visualize(environment)

for i in range(1000):
    start_time = time.time()
    environment.run_step()
    run_time = time.time()
    garbage_visualize(environment)
    print(i, run_time - start_time, time.time() - run_time)
    time.sleep(0.1)
    # input("...")

print("Finished")
