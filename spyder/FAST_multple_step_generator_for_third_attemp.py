# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:53:25 2023

@author: ignac
"""

import json
import os
import cadquery as cq
from concurrent.futures import ThreadPoolExecutor

folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\layer_info_json_for_step'

def process_file(filename):
    with open(os.path.join(folder_path, filename), 'r') as f:
        data = json.load(f)
    print(filename)
    
    

    # Define a rectangle with a missing corner
    points = data['vertices']
    
    
    
# =============================================================================
#     vertices = points
# 
#     # Create a new figure
#     fig, ax = plt.subplots()
# 
#     # Create a polygon patch from the vertices and add it to the plot
#     polygon = plt.Polygon(vertices, facecolor='blue', edgecolor='black')
#     ax.add_patch(polygon)
# 
#     # Set the limits of the plot
#    
# 
#     # Show the plot
#     plt.show()
# =============================================================================

    # Create a Workplane object from the rectangle points
    wp = cq.Workplane('XY').polyline(points)

    # Close the loop to create a closed 2D shape
    wp = wp.close()

    # Extrude the shape along the Z axis
    solid = wp.extrude(float(data['elev']))

    # Export the current solid as a STEP file
    file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\step_files_generated\{}.step'.format(filename[:-5])
    cq.exporters.export(solid, file_path, 'STEP')

# Get list of JSON files in the directory sorted by modification time
files = sorted([f for f in os.listdir(folder_path) if f.endswith('.json')], key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

# Use 4 worker threads to process the files in parallel
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(process_file, files)
