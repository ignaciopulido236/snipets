# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:02:32 2023

@author: ignac
"""

from shapely.geometry import Polygon

# Define the polygon vertices
vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

# Create a Polygon object from the vertices
polygon = Polygon(vertices)

# Check if the polygon is valid
if polygon.is_valid:
    print('Polygon is valid')
else:
    print('Polygon is invalid')
