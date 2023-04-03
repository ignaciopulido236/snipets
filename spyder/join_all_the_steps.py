import os
import cadquery as cq
from concurrent.futures import ThreadPoolExecutor

# Define the folder where the STEP files are saved
folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\step_files_generated'

# Create an empty Workplane to add the solids to
wp = cq.Workplane()

# Loop through each file in the folder
with ThreadPoolExecutor() as executor:
    for filename in os.listdir(folder_path):
        if filename.endswith('.step'):
            print(filename)
            # Load the STEP file as a solid and add it to the Workplane
            solid = cq.importers.importStep(os.path.join(folder_path, filename))
            wp = wp.add(solid)

# Export the joined solid as a new STEP file
cq.exporters.export(wp, os.path.join(folder_path+'\outputs', 'joined_solid.step'), 'STEP')