import json
import os
import cadquery as cq

folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\layer_info_json_for_step'

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        print(filename)
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
    
        # Define a rectangle with a missing corner
        points = data['vertices']
        
        # Create a Workplane object from the rectangle points
        wp = cq.Workplane('XY').polyline(points)
        
        # Close the loop to create a closed 2D shape
        wp = wp.close()
        
        # Extrude the shape along the Z axis
        solid = wp.extrude(float(data['elev']))
        
        # Export the current solid as a STEP file
        file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\step_files_generated\{}.step'.format(filename[:-5])
        cq.exporters.export(solid, file_path, 'STEP')
