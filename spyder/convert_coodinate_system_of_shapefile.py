from osgeo import ogr, osr


# set the input shapefile
from IPython import get_ipython
get_ipython().magic('reset -f')

import os
os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_attemp\basemap_countour_sample2\basemap_countour_sample2")

input_ds= ogr.Open("basemap.shp",0)
# set the output shapefile
output_shapefile = r"C:\Users\ignac\Upwork\Tom Hayden\Second_Map\shapefiles\third_map_in_cartesian\shapefile.shp"

# open the input shapefile

# get the input layer
input_layer = input_ds.GetLayer()

# get the input spatial reference
input_srs = input_layer.GetSpatialRef()

# create the output spatial reference
output_srs = osr.SpatialReference()
output_srs.SetUTM(18, 1)
output_srs.SetWellKnownGeogCS("NAD83")

# create the transformation from input to output spatial reference
transform = osr.CoordinateTransformation(input_srs, output_srs)

# create the output shapefile
driver = ogr.GetDriverByName("ESRI Shapefile")
output_ds = driver.CreateDataSource(output_shapefile)

# create the output layer
output_layer = output_ds.CreateLayer("output", output_srs, ogr.wkbPolygon)

# loop through the input features and transform them to the output spatial reference
for feature in input_layer:
    # transform the geometry
    geometry = feature.GetGeometryRef()
    geometry.Transform(transform)
    
    # create the output feature
    output_feature = ogr.Feature(output_layer.GetLayerDefn())
    output_feature.SetGeometry(geometry)
    
    # add the output feature to the output layer
    output_layer.CreateFeature(output_feature)

# close the input and output shapefiles
input_ds = None
output_ds = None
