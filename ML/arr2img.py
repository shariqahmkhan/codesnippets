import numpy as np
from PIL import Image

image = Image.open("lena.png")
np_array = np.array(image)

pil_image=Image.fromarray(np_array)
pil_image.show()
