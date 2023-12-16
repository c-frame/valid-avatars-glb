Download all fbx avatars:
```sh
cd ~
git clone git@github.com:xrtlab/Validated-Avatar-Library-for-Inclusion-and-Diversity---VALID.git
cd Validated-Avatar-Library-for-Inclusion-and-Diversity---VALID
git checkout b3f8a0dd9e6102d63df181f56cf1a616aaeb9b12
# This is to read the previous pdf version
```

In this repo:

```sh
cd scripts
mkdir -p ../avatars
export PATH=~/blender-3.6.0-linux-x64/:$PATH
./convert_all_avatars.sh ~/Validated-Avatar-Library-for-Inclusion-and-Diversity---VALID ../avatars ./blender_fbx_to_glb.py
cd ..
mv avatars/Avatars/* avatars/
rmdir avatars/Avatars
```

This takes 25 min.

Extract all images:

```sh
python3 -mvenv images_extraction
cd images_extraction
. bin/activate
pip install PyMuPDF Pillow
python scripts/extract_images_xref.py
# set images xref order in second script manually
python scripts/extract_images_text.py
```

