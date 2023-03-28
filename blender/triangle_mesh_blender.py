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

# Finish the bmesh and write the data to the mesh data block
bm.to_mesh(mesh)
bm.free()

# Create a new object using the mesh data block
obj = bpy.data.objects.new("Triangle", mesh)

# Add the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)
