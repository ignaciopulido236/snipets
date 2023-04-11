# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:03:54 2023

@author: ignac
"""

import json
import os
import cadquery as cq

folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\layer_info_json_for_step_with_offset'
ignored=[]
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        print(filename)
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
    
        # Define a rectangle with a missing corner
        points = data['vertices']
        offset=data['offset']
        elev=data['elev']
        new_heigh=float(elev)-float(offset)
        if new_heigh==0:    
            ignored.append(filename)
        else:
            # Create a Workplane object from the rectangle points
            wp = cq.Workplane('XY').polyline(points)
            
            # Close the loop to create a closed 2D shape
            wp = wp.close()
            
            # Extrude the shape along the Z axis
         
            if float(offset)>0 and new_heigh>0:
                print(offset)
                solid = wp.extrude(float(new_heigh)).translate((0,0,float(offset)))
            else:
                solid = wp.extrude(float(elev))
          
            
            # Export the current solid as a STEP file
            if new_heigh!=0:
                file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\step_files_generated_with_offset\{}.step'.format(filename[:-5])
                cq.exporters.export(solid, file_path, 'STEP')
            else:
                file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\step_files_generated_with_offset\ZZZ_{}.step'.format(filename[:-5])
                cq.exporters.export(solid, file_path, 'STEP')
