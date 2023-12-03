#!/bin/bash
# Input and output directories
input_dir=$1
output_dir=$2
blender_script=$3

# Iterate over all FBX files in all subdirectories
find "$input_dir" -name "*.fbx" | while read -r fbx_file; do

  # Create output path
  intermediate_glb_file="${fbx_file%.fbx}_intermediate.glb"
  glb_file="${fbx_file%.fbx}.glb"
  glb_file="${output_dir}${glb_file#$input_dir}"

  # Create output directory
  mkdir -p "$(dirname "$glb_file")"

  # Convert FBX to GLB
  blender --background --python "$blender_script" -- "$fbx_file" "$intermediate_glb_file"

  # Run gltf-transform optimize
  gltf-transform optimize --simplify false "$intermediate_glb_file" "$glb_file" --texture-compress webp --compress meshopt

  # Remove intermediate GLB file
  rm "$intermediate_glb_file"

done
