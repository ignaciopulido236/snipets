# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:32:47 2023

@author: ignac
"""
import json
import os

os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\layers_info_json")


file_id=10654
file_id_len=len(str(file_id))
if file_id_len==1:
    selected_file='layer_0000' +str(file_id)+'.json'
elif file_id_len==2:
    selected_file='layer_000' +str(file_id)+'.json'
elif file_id_len==3:
    selected_file='layer_00' +str(file_id)+'.json'
elif file_id_len==4:
    selected_file='layer_0' +str(file_id)+'.json'
elif file_id_len==5:
    selected_file='layer_' +str(file_id)+'.json'



os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\layer_info_json_for_step")
with open(selected_file, 'r') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)
    

file_path = r'C:\Users\ignac\OneDrive\Escritorio\STEP_FILES\layer_10654.step'

import cadquery as cq

# Define a rectangle with a missing corner
points = data['vertices']


# Create a Workplane object from the rectangle points
wp = cq.Workplane('XY').polyline(points)


# Close the loop to create a closed 2D shape
wp = wp.close()

# Extrude the shape along the Z axis
solid = wp.extrude(5)

# Export the solid as a STEP file

# Export the solid as a STEP file
cq.exporters.export(solid, file_path, 'STEP')
