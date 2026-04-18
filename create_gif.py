import imageio.v3 as iio
from PIL import Image
import numpy as np
import os

# Add your image filenames here
filenames = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg'
]

images = []
first = Image.open(filenames[0])
target_size = first.size

for filename in filenames:
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found, skipping...")
        continue
    images.append(np.array(Image.open(filename).resize(target_size)))

if images:
    iio.imwrite('output.gif', images, duration=1000, loop=0)
    print("GIF saved as output.gif")
else:
    print("No images found, GIF not created.")