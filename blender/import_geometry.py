import bpy
import bmesh
import json
import os

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)


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
file_id=0
file_id_len=len(str(file_id))
if file_id_len==1:
    selected_file='layer_0000' +str(file_id)+'.json'
elif file_id_len==2:
    selected_file='layer_000' +str(file_id)+'.json'
elif file_id_len==3:
    selected_file='layer_00' +str(file_id)+'.json'
elif file_id_len==4:
    selected_file='layer_0' +str(file_id)+'.json'
elif file_id_len==5:
    selected_file='layer_' +str(file_id)+'.json'
    
    
os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\layers_info_json")
with open(selected_file, 'r') as f:
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


#Save to stl

filepath = "C:/Users/ignac/OneDrive/Escritorio/extruded.stl"
bpy.ops.export_mesh.stl(filepath=filepath, check_existing=False)