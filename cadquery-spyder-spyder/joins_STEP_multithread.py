# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:40:21 2023

@author: ignac
"""

import os
import cadquery as cq
from concurrent.futures import ThreadPoolExecutor

# Define the folder where the STEP files are saved
folder_path = r'C:\Users\ignac\OneDrive\Escritorio\STEP_FILES'

# Create an empty Workplane to add the solids to
wp = cq.Workplane()

# Function to load a STEP file and add it to the Workplane
def load_step_file(filename):
    if filename.endswith('.step'):
        print(filename)
        # Load the STEP file as a solid and add it to the Workplane
        solid = cq.importers.importStep(os.path.join(folder_path, filename))
        return solid

# Create a thread pool and map the function to the list of files
with ThreadPoolExecutor() as executor:
    solids = list(executor.map(load_step_file, os.listdir(folder_path)))

# Add all the solids to the Workplane through a union operation
wp = wp.union(solids)

# Export the joined solid as a new STEP file
cq.exporters.export(wp, os.path.join(folder_path, 'joined_solid.step'), 'STEP')
