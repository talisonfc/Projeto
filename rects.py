import cv2

def outlineRect(image, rect, color):
	if rect is None:
		return
	x, y, w, h = rect
	cv2.rectangle(image, (x,y), (x+w,y+h),color)

def copyRect(src, dst, srcRect, dstRect, interpolation = cv2.INTER_LINEAR):
	#Copia parte da fonte para a parte destino
	x0, y0, w0, h0 = srcRect
	x1, y1, w1, h1 = dstRect

	#Resize o retangulo src no retangulo dst
	#Coloca o conteudo do src no dst
	dst[y1:y1+h1, x1:x1+w1] = cv2.resize(src[y0:y0+h0 , x0:x0+w0], (w1,h1), interpolation = interpolation)

def swapRects(src, dst, rects, interpolation = cv2.INTER_LINEAR):
	# Copiar a fonte com dois ou mais subretangulo

	if dst is not src:
		dst[:] = src

	numRects = len(rects)
	print(numRects)

	if numRects<2:
		return

	# Copia o conteudo do ultimo retangulo para dentro da memoria temporaria
	x, y, w, h = rects[numRects - 1]
	temp = src[y:y+h, x:x+w].copy()

	# Copia o conteudo de cada retangulo para dentro do proximo
	i = numRects - 2
	while i >= 0:
		copyRect(src, dst, rects[i], rects[i+1], interpolation)
		i -= 1

	# Copia o conteudo de temp dentro do primeiro retangulo
	copyRect(temp, dst, (0,0,w,h), rects[0], interpolation)