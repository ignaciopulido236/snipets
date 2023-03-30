# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 08:01:18 2023

@author: ignac
"""
import os
import cadquery as cq

# Define the folder where the STEP files are saved
folder_path = r'C:\Users\ignac\OneDrive\Escritorio\STEP_FILES'

# Create an empty Workplane to add the solids to
wp = cq.Workplane()

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.step'):
        print(filename)
        # Load the STEP file as a solid and add it to the Workplane
        solid = cq.importers.importStep(os.path.join(folder_path, filename))
        wp = wp.union(solid)

# Export the joined solid as a new STEP file
cq.exporters.export(wp, os.path.join(folder_path, 'joined_solid.step'), 'STEP')
