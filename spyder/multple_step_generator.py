import json
import os
import cadquery as cq

os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\Second_Map\layer_info_json_for_step")
solids = []
#for i in range(5):
#s = cq.Workplane("XY").box(1, 1, 1)
# s= cq.Workplane('XY').polyline([(1150,1300),(-1150,1300),(1150,-1300),(-1150,-1300)])
# s = s.close()
# s=s.extrude(10)
# =============================================================================
# 
#     s = cq.Workplane("XY").box(11000, 14100, 5)
#     solids.append(s)
#     solids.append(s)
#     combined = solids[0]
#     file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\layer_info_json_for_step'.format(k)
#     cq.exporters.export(s, file_path, 'STEP')
# =============================================================================
 
#wp_2 = cq.Workplane()
for k in range(0,1679):
    file_id=k
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
    
    print(selected_file)
    os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\Second_Map\layer_info_json_for_step")

    try:
        with open(selected_file, 'r') as f:
            # Load the JSON data into a Python dictionary
            data = json.load(f)
    except FileNotFoundError:
        print("The specified file does not exist.")
        
    # Define a rectangle with a missing corner
    points = data['vertices']
    
    # Create a Workplane object from the rectangle points
    wp = cq.Workplane('XY').polyline(points)
    
    # Close the loop to create a closed 2D shape
    wp = wp.close()
    
    # Extrude the shape along the Z axis
    solid = wp.extrude(float(data['height']))
    
    # Add the solid to the main Workplane object
    #wp_2 = wp.union(solid)
    #combined = combined.union(solid)
    
    # Export the current solid as a STEP file
    file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\step_files_generated\layer_{:05d}.step'.format(k)
    cq.exporters.export(solid, file_path, 'STEP')
    
# Export the final combined solid as a STEP file
#file_path = r'C:\Users\ignac\OneDrive\Escritorio\STEP_FILES\layers_combined2.step'
#cq.exporters.export(combined, file_path, 'STEP')
