import bpy
import sys

# Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

fbx_in = argv[0]
glb_out = argv[1]

# Clear existing mesh objects (this is to remove the default Cube)
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()
# An alternative to the above 3 lines is
# bpy.ops.wm.read_factory_settings(use_empty=True)
# that will also remove Camera and Light but those are not exported in GLB
# by default anyway.

# Import FBX
bpy.ops.import_scene.fbx(filepath=fbx_in)

# Select all objects (not needed, GLB export all objects by default)
# bpy.ops.object.select_all(action='SELECT')

# Export GLB
bpy.ops.export_scene.gltf(filepath=glb_out, export_format='GLB')
