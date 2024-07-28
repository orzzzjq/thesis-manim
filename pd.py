import numpy as np
import shapely
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

p_points_hall = np.array([
    np.array([-1, -1.5]),
    np.array([-4.5, -2.5]),
    np.array([-5, 0]),
    np.array([-4, 2]),
    np.array([-2, 1.7])
])

q_points_hall = np.array([
    np.array([4, -2.5]),
    np.array([1.5, -2.5]),
    np.array([0, 0]),
    np.array([2, 2]),
    np.array([4.5, 1])
])

p_poly = Polygon(p_points_hall)
q_poly = Polygon(q_points_hall)

p_points = p_points_hall
q_points = q_points_hall

np.random.seed(0)

counter = 0
while counter <= 40:
    x = np.random.uniform(-5, -1)
    y = np.random.uniform(-3, 2)
    if p_poly.contains(Point(x, y)):
        counter += 1
        p_points = np.vstack([p_points, [x, y]])

counter = 0
while counter <= 40:
    x = np.random.uniform(0, 5)
    y = np.random.uniform(-2.5, 2)
    if q_poly.contains(Point(x, y)):
        counter += 1
        q_points = np.vstack([q_points, [x, y]])

optimal_line_seg = [np.array([-1.3372, -0.421, 0]), np.array([0, 0, 0])]

mid_point = optimal_line_seg[0] / 2
direction = np.array([optimal_line_seg[0][1], -optimal_line_seg[0][0], 0])
optimal_svm_line = [mid_point + direction * 2, mid_point - direction * 2]
