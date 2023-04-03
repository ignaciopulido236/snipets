# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:02:44 2023

@author: ignac
"""

import json
import os
import cadquery as cq
s= cq.Workplane('XY').polyline([(1150,1300),(-1150,1300),(1150,-1300),(-1150,-1300)])
s = s.close()
s = s.close()