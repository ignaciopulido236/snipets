# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 10:55:53 2023

@author: ignac
"""

import json
import os
#import cadquery as cq
import matplotlib.pyplot as plt

folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\layer_info_json_for_step'
fig, ax = plt.subplots()
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        print(filename)
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
    
        # Define a rectangle with a missing corner
        points = data['vertices']
        if len(points)>5000:
            x=[]
            y=[]
            for coordinates in points:
                x.append(coordinates[0])
                y.append(coordinates[1])
            
            # Create a Workplane object from the rectangle points
    
            # Define the vertices of the polygon
            vertices = points
            
            # Create a new figure
            # Create a Matplotlib figure and axis
            fig, ax = plt.subplots()
            
            # Plot the polygon
            ax.plot(x, y, color='blue')
            plt.rcParams['figure.dpi']=500
            # Show the plot
            #plt.show()
            second_name=filename[:-5]
            
            file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\plots_over_100\{}.png'.format(second_name)
            plt.savefig(file_path)



