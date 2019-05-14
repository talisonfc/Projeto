from camera import Camera
import cv2
from trasckers import FaceTracker
import rects
import numpy

cam = Camera('Camera')
cam.screencast('video.avi',10,10)
faceTracker = FaceTracker()

while cv2.waitKey(1) != 27:
	frame = cam.capture()
	frameMirrod = numpy.fliplr(frame)

	faceTracker.update(frame)
	faceTracker.drawDebugRects(frame)

	#cam.record(frame)
	cam.show(frameMirrod)