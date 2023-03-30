# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:22:08 2023

@author: ignac
"""
file_path = r'C:\Users\ignac\OneDrive\Escritorio\STEP_FILES\cube.step'

import cadquery as cq

# Define a rectangle with a missing corner
points = [
    (-903.0315648482647, 1257.3925224943087), (-903.0315648482647, 1256.9684488167986), (-902.6666513838572, 1256.4765531625599), (-901.8185040288372, 1256.8915150966495), (-901.6791291127447, 1256.9684488167986), (-901.6791291127447, 1257.3925224943087)

]


# Create a Workplane object from the rectangle points
wp = cq.Workplane('XY').polyline(points)
wp = cq.Workplane('XY').polyline(points_2)

# Close the loop to create a closed 2D shape
wp = wp.close()

# Extrude the shape along the Z axis
solid = wp.extrude(5)

# Export the solid as a STEP file

# Export the solid as a STEP file
cq.exporters.export(solid, file_path, 'STEP')
