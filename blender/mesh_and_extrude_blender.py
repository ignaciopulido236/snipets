import bpy
import bmesh

# Create a new mesh data block
mesh = bpy.data.meshes.new("Triangle")

# Create a new empty bmesh and add a triangular face
bm = bmesh.new()
v1 = bm.verts.new((0.0, 0.0, 0.0))
v2 = bm.verts.new((2, 0.0, 0.0))
v3 = bm.verts.new((0.0, 3, 0.0))
bm.faces.new((v1, v2, v3))

# Extrude the face
bm.faces.ensure_lookup_table()
faces = [bm.faces[0]]
extruded = bmesh.ops.extrude_face_region(bm, geom=faces)
translate_verts = [v for v in extruded['geom'] if isinstance(v, bmesh.types.BMVert)]
bmesh.ops.translate(bm, vec=(0, 0, 6), verts=translate_verts)

# Finish the bmesh and write the data to the mesh data block
bm.to_mesh(mesh)
bm.free()

# Create a new object using the mesh data block
obj = bpy.data.objects.new("Triangle", mesh)

# Add the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Export the object to an STL file
filepath = "C:/Users/ignac/OneDrive/Escritorio/extruded.stl"
bpy.ops.export_mesh.stl(filepath=filepath, check_existing=False)


#this script creates a triangle in blender and export everything to stl