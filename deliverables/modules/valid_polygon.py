# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:02:32 2023

@author: ignac
"""
import json
import os
#import cadquery as cq
#import matplotlib.pyplot as plt
from shapely.geometry import Polygon
folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\layer_info_json_for_step'

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        #print(filename)
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
    
        # Define a rectangle with a missing corner
        points = data['vertices']
        if len(points)>0:
            x=[]
            y=[]
            for coordinates in points:
                x.append(coordinates[0])
                y.append(coordinates[1])
            
            # Create a Workplane object from the rectangle points
    
            # Define the vertices of the polygon
            vertices = points
            polygon = Polygon(vertices)

            # Check if the polygon is valid
            if polygon.is_valid:
                pass
            else:
                print('Polygon is invalid')




