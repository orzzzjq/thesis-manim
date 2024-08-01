import numpy as np
from manim import *

radius = 2

objects = [
    Circle(radius=0.5, color=YELLOW, fill_opacity=0.3).shift([2.5, 0, 0]),
    Circle(radius=0.25, color=YELLOW, fill_opacity=0.3).shift([np.cos(PI * 2 / 3) * 2.25, np.sin(PI * 2/ 3) * 2.25, 0]),
    Circle(radius=0.4, color=YELLOW, fill_opacity=0.3).shift([np.cos(-PI / 2) * 2.4, np.sin(-PI / 2) * 2.4, 0])
]

np.random.seed(1)

counter = 0
while counter < 5:
    x = np.random.uniform(-2, 2)
    y = np.random.uniform(-2, 2)
    if x ** 2 + y ** 2 <= 4:
        counter += 1
        objects.append(Circle(radius=np.random.uniform(0.3, 0.7), color=YELLOW, fill_opacity=0.3).shift([x, y, 0]))

soft_direction = objects[1].get_center() - objects[2].get_center()
soft_distance = np.sqrt(sum(soft_direction ** 2))
soft_radius = (soft_distance - 0.65) / 2
soft_center = (objects[2].get_center() + soft_direction * (0.4 / soft_distance) + objects[2].get_center() + soft_direction * (soft_distance - 0.25) / soft_distance) / 2
soft_margin_radius = np.sqrt(sum((soft_center - np.array([2.5, 0, 0])) ** 2)) - 0.5

# print(direction, soft_distance, radius, center)

