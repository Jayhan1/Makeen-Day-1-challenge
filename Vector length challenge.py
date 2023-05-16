IndexPoints = [[-10, 20, -10, -18], [-10, 20, 0, 3], [0, 3, 8, 17], [8, 17, 10, -16], [10, -16, -10, -18]]

ymax = float('-inf')  # initialize ymax to negative infinity

for IndexPoints in IndexPoints:

    ymax = max(ymax, IndexPoints[1], IndexPoints[3])

print("The max y is:", ymax)
..........................................
Indexpoints = [[-10, 20, -10, -18], [-10, 20, 0, 3], [0, 3, 8, 17], [8, 17, 10, -16], [10, -16, -10, -18]]

ymin = float('inf') 

for Indexpoint in Indexpoints:

    ymin = min(ymin, Indexpoint[1], Indexpoint[3])

print("The min y is:", ymin)

..........................................
Indexpoints = [[-10, 20, -10, -18], [-10, 20, 0, 3], [0, 3, 8, 17], [8, 17, 10, -16], [10, -16, -10, -18]]

lengths = []

for Indexpoint in Indexpoints:
    x1, y1, x2, y2 = Indexpoint
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    lengths.append(length)
print("The lengths of the vectors are:", lengths) 

or....................
import math

Indexpoints = [[-10, 20, -10, -18], [-10, 20, 0, 3], [0, 3, 8, 17], [8, 17, 10, -16], [10, -16, -10, -18]]

lengths = []

for Indexpoint in Indexpoints:
    x1, y1, x2, y2 = Indexpoint
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    lengths.append(float(format(length, '.2f')))

print("The lengths of the vectors are:", lengths)

