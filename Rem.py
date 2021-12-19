from Manager.RemImageManager import RemImageManager
from Manager.MessagingManager import MessagingManager

class Rem():

	current_image = "rem_idle.png"

	def __init__(self):
		self.im_manager = RemImageManager(self)
		self.im_manager.showPicture()
		self.mes_manager = MessagingManager(self)

	def main_loop(self):
		while True:
			self.mes_manager.run()
			self.im_manager.showPicture()

	def image_update(self, image):
		self.current_image = image