# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:34:08 2023

@author: ignac
"""
import os
import cadquery as cq
from concurrent.futures import ThreadPoolExecutor
from time import time
start = time()
folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\step_files_generated'
files_list = []
files_list_2 = []
import threading


# Collect filenames of all STEP files in folder_path
kk=0
for filename in sorted(os.listdir(folder_path)):
    if filename.endswith('.step'):
        if (kk%2)==0:
            files_list.append(filename)
        else:
            files_list_2.append(filename)
        kk=kk+1

def process_file(WP, files_list_given,thread):
    kk=0
  #  WP=cq.Workplane()
    
    for file in files_list_given:
        solid = cq.importers.importStep(os.path.join(folder_path, file))
        if kk!=0:
            
            print(file+thread)
            intersection=WP.intersect(solid,clean=False)
            solid_intersection=intersection.val()
            if solid_intersection.Volumen>0:
                print('intersect')
                solid=solid.cut(intersection)
                WP = WP.add(solid)
            
            else:        
                WP = WP.add(solid)
        else:
            WP = WP.add(solid)
    kk=kk+1
 #   return WP

wp = cq.Workplane()
wp_2 = cq.Workplane()
# Submit all file processing tasks to the thread pool
futures = []

threads = []
#with ThreadPoolExecutor(max_workers=4) as executor:     
try:
    t1 = threading.Thread(target=process_file, args=(wp, files_list, ' one'))
    t2 = threading.Thread(target=process_file, args=(wp_2, files_list_2, ' two'))
    
except:
    print('error')
    #wp=future.result()
    #future_2=executor.submit(process_file, wp_2, files_list)
    #wp_2=future_2.result()
# Wait for all tasks to finish and accumulate the results

t1.start()
t2.start()

t1.join()
t2.join()

wp_3=wp.add(wp_2)
# Use the final result
# ...
# Export the joined solid as a new STEP file
cq.exporters.export(wp, os.path.join(folder_path+'\outputs', 'joined_solid_with_multi_test.step'), 'STEP')
cq.exporters.export(wp_2, os.path.join(folder_path+'\outputs', 'joined_solid_with_multi_test_2.step'), 'STEP')
cq.exporters.export(wp_3, os.path.join(folder_path+'\outputs', 'joined_solid_with_multi_test_3.step'), 'STEP')
end = time()
total=(end - start)

print(total)