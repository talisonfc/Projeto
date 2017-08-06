import cv2
import rects
import utils

class Face(object):

	def __init__(self):
		self.faceRect = None
		self.leftEyeRect = None
		self.rightEyeRect = None
		self.noseRect = None
		self.mouthRect = None
		self.leftIrisRect = None


class FaceTracker(object):

	def __init__(self, scaleFactor = 1.2, minNeighbors = 2, flags = cv2.CASCADE_SCALE_IMAGE):
		self.scaleFactor = scaleFactor
		self.minNeighbors = minNeighbors
		self.flags = flags

		self._faces = []
		self._faceClassifier = cv2.CascadeClassifier('C:\haarcascades\haarcascade_frontalface_alt.xml')
		self._eyeClassifier = cv2.CascadeClassifier('C:\haarcascades\haarcascade_eye_tree_eyeglasses.xml')
		self._noseClassifier = cv2.CascadeClassifier('C:\haarcascades\haarcascade_mcs_nose.xml')
		self._mouthClassifier = cv2.CascadeClassifier('C:\haarcascades\haarcascade_mcs_mouth.xml')

	@property
	def faces(self):
		return self._faces

	def update(self, image):
		self._faces  = []

		if utils.isGray(image):
			image = cv2.equalizeHist(image)
		else:
			image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			cv2.equalizeHist(image, image)

		minSize = utils.widthHeightDividedBy(image, 8)
		minSize = (int(minSize[0]),int(minSize[1]))

		faceRects = self._faceClassifier.detectMultiScale(image, self.scaleFactor, self.minNeighbors, self.flags, minSize)

		if faceRects is not None:
			for faceRect in faceRects:
				face = Face()
				face.faceRect = faceRect
				x, y, w, h = faceRect

				#buscar o olho e atualizar o lado esquerdo da face
				searchRect = (x+w/7, y, w*2/7, h/2)
				face.leftEyeRect = self._detectOneObject(self._eyeClassifier, image, searchRect, 64)

				#buscar o olho e atualizar o lado direito da face
				searchRect = (x+w*4/7, y, w*2/7, h/2)
				face.rightEyeRect = self._detectOneObject(self._eyeClassifier, image, searchRect, 64)	

				#buscar nariz
				searchRect = (x+w/4, y+h/4, w/2, h/2)
				face.noseRect = self._detectOneObject(self._noseClassifier, image, searchRect, 32)

				#buscar boca
				searchRect = (x+w/6, y+h*2/3, w*2/3, h/3)
				face.mouthRect = self._detectOneObject(self._mouthClassifier, image, searchRect, 16)

				self._faces.append(face)

	def _detectOneObject(self, classifer, image, rect, imageSizeToMinSizeRatio):
		x, y, w, h = rect;
		x = int(x)
		y = int(y)
		h = int(h)
		w = int(w)

		minSize = utils.widthHeightDividedBy(image, imageSizeToMinSizeRatio)
		minSize = (int(minSize[0]),int(minSize[1]))
		subImage = image[y:y+h, x:x+w]
		subRects = classifer.detectMultiScale(subImage, self.scaleFactor, self.minNeighbors, self.flags, minSize)

		if len(subRects)==0:
			return None

		subX, subY, subW, subH = subRects[0]
		return (x+subX, y+subY, subW, subH)

	def drawDebugRects(self, image):
		if utils.isGray(image):
			faceColor = 255
			leftEyeColor = 255
			rightEyeColor = 255
			noseColor = 255
			mouthColor = 255	
		else:
			faceColor = (255,255,255)
			leftEyeColor = (0,0,255)
			rightEyeColor = (0,255,255)
			noseColor = (0,255,0)
			mouthColor = (255,0,0)
			white = (255,255,255)

		for face in self.faces:
			rects.outlineRect(image, face.faceRect, faceColor)
			rects.outlineRect(image, face.leftEyeRect, leftEyeColor)
			rects.outlineRect(image, face.rightEyeRect, rightEyeColor)
			rects.outlineRect(image, face.noseRect, noseColor)
			rects.outlineRect(image, face.mouthRect, mouthColor)

			k = 5
			leftEye = None
			rightEye = None
			mouth = None
			nose = None

			if face.leftEyeRect is not None:
				leftEye = (face.leftEyeRect[0]+int(face.leftEyeRect[2]/2) , face.leftEyeRect[1]+int(face.leftEyeRect[3]/2))
				rect = (leftEye[0]-k, leftEye[1]-k, 2*k, 2*k)
				rects.outlineRect(image, rect, white)
				
			if face.rightEyeRect is not None:
				rightEye = (face.rightEyeRect[0] + int(face.rightEyeRect[2]/2), face.rightEyeRect[1] + int(face.rightEyeRect[3]/2))
				rect = (rightEye[0]-k, rightEye[1]-k, 2*k, 2*k)
				rects.outlineRect(image, rect, white)

			if face.mouthRect is not None:
				mouth = (face.mouthRect[0]+int(face.mouthRect[2]/2), face.mouthRect[1]+int(face.mouthRect[3]/2))
				rect = (mouth[0]-k, mouth[1]-k, 2*k, 2*k)
				rects.outlineRect(image, rect, white)

			if face.noseRect is not None:
				nose = (face.noseRect[0]+int(face.noseRect[2]/2), face.noseRect[1]+int(face.noseRect[3]/2))
				rect = (nose[0]-k, nose[1]-k, 2*k, 2*k)
				rects.outlineRect(image, rect, white)

			if leftEye and rightEye and nose and mouth is not None:
				cv2.line(image, leftEye, rightEye,white, 1)
				cv2.line(image, leftEye, mouth,white, 1)
				cv2.line(image, mouth, rightEye,white, 1)
				cv2.line(image, nose, rightEye,white, 1)
				cv2.line(image, nose, leftEye,white, 1)
				cv2.line(image, nose, mouth,white, 1)

				# Descritores
				distEyes = utils.dist(leftEye, rightEye)
				distLeftEyeToNose = utils.dist(leftEye, nose)
				distRightEyeToNose = utils.dist(rightEye, nose)
				distLeftEyeToMouth = utils.dist(leftEye, mouth)
				distRightEyeToMouth = utils.dist(rightEye, mouth)
				distNoseToMouth = utils.dist(nose, mouth)
				
				#print(distEyes, distLeftEyeToNose, distRightEyeToNose, distLeftEyeToMouth, distRightEyeToMouth, distNoseToMouth)
				print(distEyes/distLeftEyeToNose, distEyes/distRightEyeToNose, distEyes/distLeftEyeToMouth, distEyes/distRightEyeToMouth, \
					distLeftEyeToNose/distLeftEyeToMouth, distRightEyeToNose/distRightEyeToMouth)

			# Gerando caracterizadores faciais
			#print(">> Face: ",face.faceRect)
			#print(">> Left eye: ",face.leftEyeRect)
			#print(">> Right eye: ",face.rightEyeRect)
			#print(">> Nose: ", face.noseRect)
			#print(">> Mouth: ",face.mouthRect)