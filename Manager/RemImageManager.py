from PIL import Image
import os
from Generators.AsciiGenerator import *

class RemImageManager():

	def __init__(self, rem):
		self.rem = rem

	def showPicture(self):
		new_width = 100
		path = f'./Images/{self.rem.current_image}'
		try:
		    image = PIL.Image.open(path)
		except:
		    print(path, " is not a valid picture.")
		    return
		new_image_data = pixels_to_ascii(grayify(resize_image(image)))
		pixel_count = len(new_image_data)  
		ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
		print(ascii_image)
