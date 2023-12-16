import fitz  # PyMuPDF
import io
import os
import json
from PIL import Image

# order in the pdf
images_xref_order = [
# page 1
1083,
1084,
1095,
1101,
1102,
1103,
1104,
1105,
1106,
1107,
1085,
1086,
1087,
1088,
1089,
1090,
1091,
1092,
1093,
1094,
1096,
1097,
1098,
1099,
1100,
# page 2
3,
4,
16,
22,
23,
24,
25,
26,
27,
28,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
17,
18,
19,
20,
21,
# page 3
32,
33,
44,
50,
51,
52,
53,
54,
55,
56,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
45,
46,
47,
48,
49,
# page 4
59,
60,
71,
77,
78,
79,
80,
81,
82,
83,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
72,
73,
74,
75,
76,
# page 5
86,
87,
98,
104,
105,
106,
107,
108,
109,
110,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
99,
100,
101,
102,
103,
# page 6
113,
114,
124,
130,
131,
132,
133,
134,
135,
136,
115,
116,
117,
118,
119,
120,
121,
122,
123,
205,
125,
126,
127,
128,
129,
# page 7
139,
140,
151,
157,
158,
159,
160,
161,
162,
163,
141,
142,
143,
144,
145,
146,
147,
148,
149,
150,
152,
153,
154,
155,
156,
# page 8
167,
169,
180,
186,
187,
188,
189,
190,
191,
192,
170,
171,
172,
173,
174,
175,
176,
177,
178,
179,
181,
182,
183,
184,
185,
# page 9
200,
201,
202,
203,
204,
196,
197,
198,
199,
205,
]

# the sort of texts doesn't work on page 9
xref2text = {
200: "X_NHPI_F_3_Casual",
201: "X_NHPI_F_3_Busi",
202: "X_NHPI_F_3_Medi",
203: "X_NHPI_F_3_Milit",
204: "X_NHPI_F_3_Util",
196: "X_NHPI_M_1_Casual",
197: "X_NHPI_M_1_Busi",
198: "X_NHPI_M_1_Medi",
199: "X_NHPI_M_1_Milit",
205: "X_NHPI_M_1_Util",
}

def pdf_image_extract(pdf_path, images_dir):
    doc = fitz.open(pdf_path)
    data = []

    for i in range(len(doc)):
        page = doc[i]

        # Get a list of all images on the page
        images = page.get_images(full=True)
        images = sorted(images, key=lambda x: images_xref_order.index(x[0]))

        # Get a list of all text blocks on the page
        blocks = page.get_text("blocks")
        # Filter out blocks that don't contain any text
        blocks = [b for b in blocks if not b[4].startswith("<image")]
        # Sort blocks by vertical position, then horizontal position
        blocks = sorted(blocks, key=lambda b: (b[1], b[0]))

        # Now match each image with the closest text block below it
        for img in images:
            xref = img[0]
            # base = img[1]
            img_data = doc.extract_image(xref)
            img_data_bytes = img_data["image"]

            # Save the image data to a PIL image
#            image = Image.open(io.BytesIO(img_data_bytes))

            # Get the closest text block below this image
            if i == 8:
                base = xref2text.get(xref)
            else:
                closest_block = blocks.pop(0)
                base = closest_block[4].strip().replace('x_', 'X_')
                if base == 'MENA_1_Casual':
                    base = 'MENA_M_1_Casual'
                if base.startswith('X_AIAN_F_2'):
                    base = base.replace('X_AIAN_F_2', 'X_AIAN_F_1')
                if base.startswith('Mena_M_2'):
                    base = base.replace('Mena_M_2', 'Hispanic_F_2')
                if base.startswith('Mena_M_3'):
                    base = base.replace('Mena_M_3', 'Hispanic_F_3')

            # Save the image data to a JPEG file
#            filename = base + img_data["ext"]
            filename = base + ".jpg"
            os.makedirs(images_dir, exist_ok=True)
            image_path = os.path.join(images_dir, filename)
#            image.save(image_path, "JPEG")
            with open(image_path, 'wb') as f:
                f.write(img_data_bytes)

            ethnicity, gender, num, outfit = base.rsplit("_", 3)
            if ethnicity.startswith('X_'):
                model_path = os.path.join('avatars', 'X_Non-validated', base + ".glb")
            else:
                model_path = os.path.join('avatars', ethnicity, base + ".glb")

            if not os.path.exists(model_path):
                print(model_path, "doesn't exist")
                continue

            # Save the image path and model path to the data list
            data.append({
                'text': base,
                'image': image_path,
                'model': model_path,
                'ethnicity': ethnicity,
                'gender': gender,
                'num': num,
                'outfit': outfit
            })

    # Export to JSON
    with open('avatars.json', 'w') as f:
        json.dump(data, f, indent=2)

# Make sure to replace with your actual paths
pdf_image_extract('../Validated-Avatar-Library-for-Inclusion-and-Diversity---VALID/All Models.pdf', 'images')

# avatars/X_Non-validated/X_AIAN_F_2_Casual.glb doesn't exist
# avatars/X_Non-validated/X_AIAN_F_2_Busi.glb doesn't exist
# avatars/X_Non-validated/X_AIAN_F_2_Medi.glb doesn't exist
# avatars/X_Non-validated/X_AIAN_F_2_Milit.glb doesn't exist
# avatars/X_Non-validated/X_AIAN_F_2_Util.glb doesn't exist
