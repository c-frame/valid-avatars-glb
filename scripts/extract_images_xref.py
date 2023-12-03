import fitz  # PyMuPDF
import io
import os
import json
from PIL import Image

def pdf_image_extract(pdf_path, images_dir):
    doc = fitz.open(pdf_path)
    data = []

    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base = img[1]
            print(xref,base)
            img_data = doc.extract_image(xref)
            img_data_bytes = img_data["image"]
            base = str(xref)

            # Save the image data to a PIL image
            image = Image.open(io.BytesIO(img_data_bytes))

            # Save the image data to a JPEG file
            filename = base + ".jpg"  # Remove the file extension and add .jpg
            folder_path = os.path.join(images_dir, str(i+1))
            image_path = os.path.join(folder_path, filename)
            os.makedirs(folder_path, exist_ok=True)
            image.save(image_path, "JPEG")

            # Save the image path and filename to the data list
            data.append({
                'image': image_path,
                'model': base + ".glb",
            })

    # Export to JSON
    with open('output.json', 'w') as f:
        json.dump(data, f)

# Make sure to replace with your actual paths
pdf_image_extract('../Validated-Avatar-Library-for-Inclusion-and-Diversity---VALID/All Models.pdf', 'images_xref')
