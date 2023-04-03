# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:02:44 2023

@author: ignac
"""

import json
import os
import cadquery as cq
s= cq.Workplane('XY').polyline([(489167,4483416),(489417,4469188),(500191,4469199),(500225,4483430)])
s = s.close()
solid = s.extrude(float(10))
file_path = r'C:\Users\ignac\Downloads\JDonwloader\base.step'
cq.exporters.export(solid, file_path, 'STEP')