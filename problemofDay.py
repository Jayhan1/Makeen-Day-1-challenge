# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:45:45 2023

@author: Jihan Alnofli
"""

import matplotlib.pyplot as plt

# House coordinates
houses = [
    [(0, 0), (0, 15), (5, 15), (5, 0)],
    [(5, 0), (5, 10), (7, 10), (7, 0)],
    [(7, 0), (7, 12), (8, 12), (8, 0)],
    [(9, 0), (9, 10), (10, 10), (10, 0)],
    [(10, 0), (10, 5), (11, 5), (11, 0)]
]

# Draw houses
for house in houses:
    x_coords = [coord[0] for coord in house]
    y_coords = [coord[1] for coord in house]
    plt.plot(x_coords, y_coords, 'k-')  # 'k-' for black lines

# Connect top points with lines
for house in houses:
    x_top = [house[1][0], house[2][0]]
    y_top = [house[1][1], house[2][1]]
    plt.plot(x_top, y_top, 'r-')  # 'r-' for red lines

# Set plot limits
plt.xlim(-1, 12)
plt.ylim(-1, 16)

# Display the plot
plt.show()
