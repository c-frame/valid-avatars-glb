import bpy
import sys

# Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

fbx_in = argv[0]
glb_out = argv[1]

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Import FBX
bpy.ops.import_scene.fbx(filepath=fbx_in)

# Select all objects
bpy.ops.object.select_all(action='SELECT')

# Export GLB
bpy.ops.export_scene.gltf(filepath=glb_out)
