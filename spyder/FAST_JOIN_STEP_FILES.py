# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 02:18:42 2023

@author: ignac
"""

import os
import cadquery as cq
from concurrent.futures import ThreadPoolExecutor

# Define the folder where the STEP files are saved
folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\step_files_generated'

# Create a list of the files in the directory with their file sizes
files = []
for filename in os.listdir(folder_path):
    if filename.endswith('.step'):
        file_path = os.path.join(folder_path, filename)
        file_size = os.path.getsize(file_path)
        files.append((file_path, file_size))

# Sort the list by file size
files.sort(key=lambda x: x[1])

# Create an empty Workplane to add the solids to
wp = cq.Workplane()

# Loop through each file in the sorted list
with ThreadPoolExecutor() as executor:
    for file_path, file_size in files:
        print(os.path.basename(file_path))
        # Load the STEP file as a solid and add it to the Workplane
        solid = cq.importers.importStep(file_path)
        wp = wp.add(solid)

# Export the joined solid as a new STEP file
cq.exporters.export(wp, os.path.join(folder_path+'\outputs', 'joined_solid.step'), 'STEP')
