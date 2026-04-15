import imageio.v3 as iio
from PIL import Image
import numpy as np

#insert image filenames
#         v
pic1 = 'shitphys.JPG'
pic2 = 'p1.jpg' 
pic3 = 'p2.jpg' 
pic4 = 'p3.jpg'
pic5 = 'p4.jpg'
pic6 = 'goatphys.jpg'

filenames = [pic1, pic2, pic3, pic4, pic5, pic6]
images = []

first = Image.open(filenames[0])
target_size = first.size

for filename in filenames:
  images.append(np.array(Image.open(filename).resize(target_size)))

iio.imwrite('nyan.gif', images, duration = 1000, loop = 0)