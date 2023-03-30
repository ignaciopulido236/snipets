import cadquery as cq

# Crear el primer sólido (un cubo de 10 mm de lado)
solid1 = cq.Workplane().box(10, 10, 10)

# Crear el segundo sólido (un cilindro de radio 5 mm y altura 20 mm)
solid2 = cq.Workplane().circle(5).extrude(20)

# Crear el tercer sólido (un prisma triangular de base 10x10 mm y altura 15 mm)
points = [(0, 0), (10, 0), (5, 10)]
solid3 = cq.Workplane().polyline(points).close().extrude(15)

# Combinar los tres sólidos
combined_solid = solid1.union(solid2).union(solid3)

# Guardar el resultado en un archivo STEP
cq.exporters.export(combined_solid, 'C:/Users/ignac/OneDrive/Escritorio/STEP_FILES/three_solids.step')
