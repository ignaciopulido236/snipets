
"""
Created on Tue Apr  4 12:02:32 2023

@author: ignac
"""
import json
import os
#import cadquery as cq
#import matplotlib.pyplot as plt
from shapely.geometry import Polygon
folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\layer_info_json_for_step'
polygons=[]
elevations=[]
offset=[]
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        #print(filename)
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
            polygons.append(data['coordinates'])
            elevations.append(data['elev'])
            offset.append(data['offset'])
            
for i in range(len(polygons)):
    print('polygon number: '+str(i))
    polygon_a=Polygon(polygons[i])
    polygon_a_area=polygon_a.area
    for j in range(len(polygons)):
        if i!=j:       
            
            
            polygon_b=Polygon(polygons[j])    
            intersection_poly=polygon_a.intersection(polygon_b)
            intersection_area=intersection_poly.area
            if intersection_area!=0:
                area_ratio=polygon_a_area/intersection_area
                if area_ratio==1:
                    if elevations[i]>elevations[j] and offset[i]<elevations[j]:
                        offset[i]=elevations[j]
        if float(offset[i])-float(elevations[i])==0:
            raise
    

