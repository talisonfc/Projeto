
import numpy as np
import cv2
import os

# gray = rgb2gray(rgb)

def isGray(image):
	return image.ndim<3

def widthHeightDividedBy(image, divisor):
	h,w = image.shape
	return (w/divisor,h/divisor)

def dist(p1, p2):
	return ( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )**0.5

def rgb2gray(rgb):
	return cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

# c - fator de reducao
def resize(img, c):
    w = int(c*len(img))
    h = int(c*len(img[0]))
    return cv2.resize(img, (h, w))

def concatH(img1, img2):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    return vis

def concatV(img1, img2):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((h1+h2, max(w1,w2)), np.uint8)
    vis[:h1, :w1] = img1
    vis[h1:h1+h2, :w2] = img2
    return vis

# add noisy
def addnoise(image, noise_typ="gauss"):
    if noise_typ == "gauss":
        row,col,ch = image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return noisy