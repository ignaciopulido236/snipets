# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:02:44 2023

@author: ignac
"""

import json
import os
import cadquery as cq

xx_min=-8408657.478
yy_min=4925157.848
xx_max=-8404727.681
yy_max=4927172.903
s= cq.Workplane('XY').polyline([(xx_min,yy_min),(xx_max,yy_min),(xx_max,yy_max),(xx_min,yy_max)])
s = s.close()
solid = s.extrude(float(10))
file_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\base\zz-base.step'
cq.exporters.export(solid, file_path, 'STEP')

print(str([(xx_min,yy_min),(xx_max,yy_min),(xx_max,yy_max),(xx_min,yy_max)]))