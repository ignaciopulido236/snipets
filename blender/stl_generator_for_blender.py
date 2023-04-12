import bpy
import bmesh
import json
import os

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)


#
folder_path = r'C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\layer_info_json_for_step_blender'

os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\layer_info_json_for_step_blender")
########
for selected_file in os.listdir(folder_path):
    if selected_file.endswith('.json'):        
        
       # os.chdir(r"C:\Users\ignac\Upwork\Tom Hayden\Fourth_Map\layer_info_json_for_step")
        with open(selected_file, 'r') as f:
            # Load the JSON data into a Python dictionary
            data = json.load(f)
        #print(data)
        #
            mesh = bpy.data.meshes.new(selected_file)
            bm = bmesh.new()

            print(data['vertices'])
            new_verts = []
            for vertex in data['vertices']:            
                new_verts.append(bm.verts.new(vertex))
            bm.faces.new(new_verts)

            height=float(data['elev'])
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
            obj = bpy.data.objects.new(selected_file, mesh)

            # Add the object to the scene
            scene = bpy.context.scene
            scene.collection.objects.link(obj)


#Save to stl

filepath = "C:/Users/ignac/OneDrive/Escritorio/view_version.stl"
bpy.ops.export_mesh.stl(filepath=filepath, check_existing=False)

#Save to stl

filepath = "C:/Users/ignac/OneDrive/Escritorio/view_version_2.step"
bpy.ops.export_mesh.stl(filepath=filepath,check_existing=False)