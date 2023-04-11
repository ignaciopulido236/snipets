# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:45:51 2023

@author: ignac
"""
import json
import os
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Define the polygons
poly1 = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])
poly2 = Polygon([(5, 0), (5, 15), (15, 15), (15, 5)])
poly3 = Polygon([(12, 3), (12, 8), (17, 8), (17, 3)])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the polygons
ax.fill(*poly1.exterior.xy, alpha=0.5, label='Polygon 1')
ax.fill(*poly2.exterior.xy, alpha=0.5, label='Polygon 2')
ax.fill(*poly3.exterior.xy, alpha=0.5, label='Polygon 3')

# Set the axis limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

# Add a legend and show the plot
ax.legend()
plt.show()


from shapely.geometry import Polygon

# Define two polygons


# Check if the polygons intersect
if poly1.intersects(poly2):
    # Find the intersection between the polygons
    intersection_poly = poly3.intersection(poly2)

    # Print the area of the intersection
    print("Area of the intersection:", intersection_poly.area)
else:
    print("Polygons do not intersect")
