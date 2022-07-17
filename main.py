from os import environ
import time
from life import Life


def garbage_visualize(env: Life):
    print("\033[H\033[J", end="")
    for row in env.cell:
        print(''.join(map(lambda x: '  ' if x == 0 else '[]', row)))


glider = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

environment = Life(glider)

print("initial")
garbage_visualize(environment)

for i in range(100):
    environment.run_step()
    garbage_visualize(environment)
    print(i)
    time.sleep(0.1)
    # input("...")

print("Finished")
