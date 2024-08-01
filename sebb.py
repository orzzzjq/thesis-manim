import numpy as np
from manim import *

radius = 2

objects = [
    Dot([2, 0, 0], color=YELLOW),
    Dot([np.cos(PI * 2 / 3) * 2, np.sin(PI * 2/ 3) * 2, 0], color=YELLOW),
    Dot([np.cos(-PI / 2) * 2, np.sin(-PI / 2) * 2, 0], color=YELLOW)
]

np.random.seed(1)

counter = 0
while counter < 15:
    x = np.random.uniform(-2, 2)
    y = np.random.uniform(-2, 2)
    if x ** 2 + y ** 2 <= 4:
        counter += 1
        objects.append(Dot([x, y, 0], color=YELLOW))
