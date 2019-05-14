import cv2
import numpy

# classe para gerenciar o acesso a camera
# iniciar camera
# capturar imagem
# mostrar imagem
# salvar imagem

class Camera:

	def __init__(self,name):
		self.vc = cv2.VideoCapture(0)
		self.window = name
		cv2.namedWindow(name)

	def capture(self):
		val, frame = self.vc.read()
		return numpy.fliplr(frame)

	def show(self,frame):
		cv2.imshow(self.window,frame)

	def screenshot(nome,frame):
		cv2.imwrite(nome,frame)

	def screencast(self,nome, fps, duration, codec = cv2.VideoWriter_fourcc('I','4','2','0')):
		size = (int(self.vc.get(3)), int(self.vc.get(4)))
		self.videoWrite = cv2.VideoWriter(nome, codec, fps, size)
		self.numFrameRemaining = fps*duration

	def record(self, frame):
		if self.numFrameRemaining > 0:
			self.videoWrite.write(frame)
			self.numFrameRemaining -= 1

