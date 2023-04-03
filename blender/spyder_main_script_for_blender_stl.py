# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:04:34 2023

@author: ignac
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:09:45 2023

@author: ignac
"""
# =============================================================================
# from IPython import get_ipython
# get_ipython().magic('reset -f')
# =============================================================================
from osgeo import ogr

import os
os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian")

data_source= ogr.Open("shapefile.shp",0)

FEATURE_NUMBER=1


layer = data_source.GetLayer(0)
#name=data_layer.GetField("name")
number_of_layer=data_source.GetLayerCount()
# Get the first feature in the layer
feature = layer.GetFeature(FEATURE_NUMBER)
name=feature.GetField("FID")
elev=feature.GetField("ELEV")
geom = feature.GetGeometryRef()
number_of_vertex=geom.GetPointCount()
number_of_polygons=geom.GetGeometryCount()
polygons=[]
vertex_counts = []
coordinates = []
type_geom = []
# get the Multipolygon's geometries and extract the polygons
geometry = feature.GetGeometryRef()
polygons = []
if geometry.GetGeometryName() == 'MULTIPOLYGON':
    for i in range(geometry.GetGeometryCount()):
        multipolygon = geometry.GetGeometryRef(i)
        for j in range(multipolygon.GetGeometryCount()):
            polygon = multipolygon.GetGeometryRef(j)
            polygons.append(polygon)
elif geometry.GetGeometryName() == 'POLYGON':
    polygons.append(geometry)

# do something with the polygons (e.g., get their coordinates)
new_coordinates = []
new_vertices=[]
file_number=0
for polygon in polygons:
    file_name="\layer_"+str(FEATURE_NUMBER)+"poly_"+str(file_number)+".json"
    # do something with the polygon
    new_coordinates.append([polygon.GetX(),polygon.GetY()])
    file_number=file_number+1
    
    output_path=r"C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\layer_info_json_for_step"
    file = open(str(output_path+file_name) , "w")
    file.write('{\n')
    file.write('"layer_FID":'+'"' +str(int(file_number)) + '",')
    file.write('\n')
    file.write('"file_name":'+'"' + str(file_number) + '",')
    file.write('\n')
    file.write('"num_vertices":'+'"' +str(int(number_of_vertex)) + '",')
    file.write('\n')
    file.write('"coordinates":'+ str(new_coordinates).replace("(","[").replace(")","]") +',' )
    file.write('\n')
    file.write('"vertices":' + str(new_vertices).replace("(","[").replace(")","]")+',' )
    file.write('\n')
    file.write('"elev":'+'"' + str(elev))
    file.write('\n')
    
    #file.write(str(new_coordinates))

    file.write('}')
    file.close()
    

new_vertices=new_coordinates


filename_json=f"\{file_name}.json"



#ext=layer.Get
# =============================================================================
# for k in range(0,13827):
#     feature = layer.GetFeature(k)
#     
#     name=feature.GetField("FID")#
#     elev=feature.GetField("ELEV")#
# 
#     geom = feature.GetGeometryRef()
#     number_of_vertex=geom.GetPointCount()
# 
#     #Definition of offset
#     if number_of_vertex<30:
#         zoom_factor=4
#     else:
#         zoom_factor=0
#     height_offset=322+zoom_factor
#     DX=700580
#     DY=5332561
# =============================================================================
    
    
    # =============================================================================
    #         for i in range(number_of_vertex):
    #             X=geom.GetPoint(i)
    #             print(X)
    # =============================================================================
       # print("X:"+ str(x))
        #print("y:" +str(y))
        
# =============================================================================
#     #Define the tuple where we are going to save the coordinates
#     new_coordinates = []
#     new_vertices=[]
#     for i in range(number_of_vertex):
#         new_coordinates.append(geom.GetPoint(i))
#         vertex_x=new_coordinates[i][0]-DX
#         vertex_y=new_coordinates[i][1]-DY
#         vertex_z=new_coordinates[i][2]
#         new_vertices.append((vertex_x,vertex_y,vertex_z))
#      
#         
#     height=elev- height_offset
#         
#     #Layer FID  
#     layer_name=feature.GetField("ID")#
#     
#     #Define file name
#     len_of_layer_name=len(str(int(layer_name)))
#     if len_of_layer_name==5:
#         file_name="layer_"+str(int(layer_name))
#     elif len_of_layer_name==4:
#         file_name="layer_0"+str(int(layer_name))
#     elif len_of_layer_name==3:
#         file_name="layer_00"+str(int(layer_name))
#     elif len_of_layer_name==2:
#         file_name="layer_000"+str(int(layer_name))
#     elif len_of_layer_name==1:
#         file_name="layer_0000"+str(int(layer_name))
#     else:
#         raise ValueError('layer name len exception')
#     
#     filename_json=f"\{file_name}.json"
#     output_path=r"C:\Users\ignac\Upwork\Tom Hayden\layers_info_json"
#     file = open(str(output_path+filename_json) , "w")
#     file.write('{\n')
#     file.write('"layer_FID":'+'"' +str(int(layer_name)) + '",')
#     file.write('\n')
#     file.write('"file_name":'+'"' + str(file_name) + '",')
#     file.write('\n')
#     file.write('"num_vertices":'+'"' +str(int(number_of_vertex)) + '",')
#     file.write('\n')
#     file.write('"coordinates":'+ str(new_coordinates).replace("(","[").replace(")","]") +',' )
#     file.write('\n')
#     file.write('"vertices":' + str(new_vertices).replace("(","[").replace(")","]")+',' )
#     file.write('\n')
#     file.write('"elev":'+'"' + str(elev) + '",')
#     file.write('\n')
#     file.write('"height":'+'"' + str(height) +'"')
#     file.write('\n')
#     #file.write(str(new_coordinates))
#     
#     file.write('}')
#     file.close()
# 
# # =============================================================================
# # pointCount = geom.GetGeometryRef(0)
# # 
# # number_of_points=geom.GetPointCount()
# # number_of_features=layer.GetFeatureCount()
# # number_of_vertex=pointCount.GetPointCount()
# # 
# # 
# # 
# =============================================================================
# 
# 
# 
# 
# name=feature.GetField("name")#
# number_of_points=geom.GetPointCount()
# geom
# #feature.GetGeomFieldCount
# =============================================================================
#print(dir(feature))
#print(name)
# =============================================================================
# geomType = layer.GetGeomType()
# for feature in layer:
#     geom = feature.GetGeometryRef()
#     if geom is not None:
#         for i in range(geom.GetPointCount()):
#             x, y, z = geom.GetPoint(i)
#             print("Feature ID:", feature.GetFID(), "X:", x, "Y:", y, "Z:", z)
# print("end")
# =============================================================================
# Get the geometry of the feature
#geometry = feature.getY()

# =============================================================================
# for f in feature:
#     #print(dir(f))
#     #print(f.GetGeometryRef())
#     multipoint=f.GetGeometryRef()
#     print(multipoint)
#     point = multipoint.GetGeometryRef(0) # <--- Get the point at index 0
#     mx,my = point.GetX(), point.GetY()
#     print("x:"+str(mx))
#     print("y:"+str(my))
#     print("end")
# =============================================================================
# Check if the geometry is a polygon
# =============================================================================
# if geometry.GetGeometryName() == 'POLYGON':
# 
#     # Get the coordinates of the polygon vertices
#     coords = geometry.GetPoints()
# 
#     # Print the coordinates
#     print(coords)
# 
# else:
#     print('Geometry is not a polygon')
# =============================================================================


