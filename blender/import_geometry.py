import bpy
import bmesh
import json
import os
# Create a new mesh data block
mesh = bpy.data.meshes.new("Base")
os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\json_files")

with open('layer_0001.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)
  
#
bm = bmesh.new()


new_verts = []
for vertex in data['vertices']:
    new_verts.append(bm.verts.new(vertex))
bm.faces.new(new_verts)

height=data['height']
# Extrude the face
bm.faces.ensure_lookup_table()
faces = [bm.faces[0]]
extruded = bmesh.ops.extrude_face_region(bm, geom=faces)
translate_verts = [v for v in extruded['geom'] if isinstance(v, bmesh.types.BMVert)]
bmesh.ops.translate(bm, vec=(0, 0, height), verts=translate_verts)

# Finish the bmesh and write the data to the mesh data block
bm.to_mesh(mesh)
bm.free()

# Create a new object using the mesh data block
obj = bpy.data.objects.new("Triangle", mesh)

# Add the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Export the object to an STL file



########
os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\layers_info_json")
with open('layer_06795.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)
#print(data)
#
mesh = bpy.data.meshes.new(data['file_name'])
bm = bmesh.new()

print(data['vertices'])
new_verts = []
for vertex in data['vertices']:
    
    new_verts.append(bm.verts.new(vertex))
bm.faces.new(new_verts)

height=float(data['height'])
# Extrude the face
bm.faces.ensure_lookup_table()
faces = [bm.faces[0]]
extruded = bmesh.ops.extrude_face_region(bm, geom=faces)
translate_verts = [v for v in extruded['geom'] if isinstance(v, bmesh.types.BMVert)]
bmesh.ops.translate(bm, vec=(0, 0, height), verts=translate_verts)

# Finish the bmesh and write the data to the mesh data block
bm.to_mesh(mesh)
bm.free()

# Create a new object using the mesh data block
obj = bpy.data.objects.new(data['file_name'], mesh)

# Add the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)

filepath = "C:/Users/ignac/OneDrive/Escritorio/extruded.stl"
bpy.ops.export_mesh.stl(filepath=filepath, check_existing=False)