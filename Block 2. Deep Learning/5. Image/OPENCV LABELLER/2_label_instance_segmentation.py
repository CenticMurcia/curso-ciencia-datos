'''
====================================================================
Interactive Instance Segmentation using GrabCut algorithm.

USAGE:

	python 2_label_instance_segmentation.py <img_filename>

	Two windows will show up, one for input and one for output.
	At first, in input window, draw a rectangle around the object using the
	right mouse button. Then press 'n' to segment the object (once or a few times)

	For any finer touch-ups, you can press any of the keys below and draw lines on
	the areas you want. Then again press 'n' to update the output.

	Key '0' - To select areas of sure background
	Key '1' - To select areas of sure foreground
	Key '2' - To select areas of probable background
	Key '3' - To select areas of probable foreground
	Key 'n' - To update the segmentation
	Key 'r' - To reset the setup
	Key 's' - To save the results

SOURCE

	https://github.com/opencv/opencv/blob/master/samples/python/grabcut.py
	https://github.com/makelove/OpenCV-Python-Tutorial/blob/master/%E5%AE%98%E6%96%B9samples/grabcut.py

====================================================================
'''


import numpy as np
import cv2   as cv
import sys


SCREEN_WINDOW_POS = {"top": 500, "left": 500}
ESCAPE_KEY = 27

BLUE       = [255,  0,  0] # rectangle color
GREEN      = [  0,255,  0]
RED        = [  0,  0,255]
BLACK      = [  0,  0,  0]
DARK_GREY  = [ 50, 50, 50]
LIGHT_GREY = [200,200,200]
WHITE      = [255,255,255]

BACKGROUND  = {'color': BLACK,      'val': cv.GC_BGD }   # an obvious background pixel. VALUE: 0
PROBABLY_BG = {'color': DARK_GREY,  'val': cv.GC_PR_BGD} # a possible background pixel. VALUE: 2
PROBABLY_FG = {'color': LIGHT_GREY, 'val': cv.GC_PR_FGD} # a possible foreground pixel. VALUE: 3
FOREGROUND  = {'color': WHITE,      'val': cv.GC_FGD}    # an obvious foreground pixel. VALUE: 1



class InstanceSegmentator():

	def __init__(self, img_path):

		self.img  = cv.imread(cv.samples.findFile(img_path))
		self.img2 = self.img.copy()                                # a copy of original image
		self.grabcut_mask = np.zeros(self.img.shape[:2], dtype = np.uint8) # mask initialized to PR_BG
		self.binary_mask  = np.zeros(self.img.shape[:2], dtype = np.uint8) # mask initialized to PR_BG
		self.output = np.zeros(self.img.shape, np.uint8)           # output image to be shown
		
		self.rect = (0,0,1,1)
		self.drawing = False         # flag for drawing curves
		self.rectangle = False       # flag for drawing rect
		self.rect_over = False       # flag to check if rect drawn
		self.rect_or_mask = 100      # flag for selecting rect or mask mode
		self.value = FOREGROUND      # drawing initialized to FG
		self.thickness = 3           # brush thickness

		# input and output windows
		cv.namedWindow('input')
		cv.namedWindow('output')
		cv.moveWindow('input',  x=SCREEN_WINDOW_POS["top"],                   y=SCREEN_WINDOW_POS["left"])
		cv.moveWindow('output', x=SCREEN_WINDOW_POS["top"]+self.img.shape[1], y=SCREEN_WINDOW_POS["left"])
		cv.setMouseCallback('input', self.onmouse)

		print(" Instructions: \n")
		print(" Draw a rectangle around the object using right mouse button \n")


	def segment_with_grabCut(self):
		# GC_INIT_WITH_RECT marks all pixels outside the given rect as "background"
		# and all pixels inside the rect as "probably foreground"

		bgdmodel = np.zeros((1, 65), np.float64)
		fgdmodel = np.zeros((1, 65), np.float64)

		if (self.rect_or_mask == 0):         # grabcut with rect
			cv.grabCut(self.img2, self.grabcut_mask, self.rect, bgdmodel, fgdmodel, 1, cv.GC_INIT_WITH_RECT) # self.grabcut_mask, bgdmodel, fgdmodel ARE UPDATED HERE
			self.rect_or_mask = 1
		elif (self.rect_or_mask == 1):       # grabcut with mask
			cv.grabCut(self.img2, self.grabcut_mask, None, bgdmodel, fgdmodel, 1, cv.GC_INIT_WITH_MASK) # self.grabcut_mask, bgdmodel, fgdmodel ARE UPDATED HERE

		self.binary_mask = ( (self.grabcut_mask==FOREGROUND["val"]) | (self.grabcut_mask==PROBABLY_FG["val"]) ).astype('uint8') * 255


	def onmouse(self, event, x, y, flags, param):

		if event == cv.EVENT_LBUTTONDOWN:

			# Draw Rectangle
			if self.rect_over == False:
				self.rectangle = True
				self.ix, self.iy = x,y

			# Draw touchup curves
			else:
				self.drawing = True
				cv.circle(self.img,  (x,y), self.thickness, self.value['color'], -1)
				cv.circle(self.grabcut_mask, (x,y), self.thickness, self.value['val'], -1)

		elif event == cv.EVENT_LBUTTONUP:
			if self.drawing == True:
				self.drawing = False
				cv.circle(self.img, (x, y), self.thickness, self.value['color'], -1)
				cv.circle(self.grabcut_mask, (x, y), self.thickness, self.value['val'], -1)
			else:
				self.rectangle = False
				self.rect_over = True
				cv.rectangle(self.img, (self.ix, self.iy), (x, y), BLUE, 2)
				self.rect = (min(self.ix, x), min(self.iy, y), abs(self.ix - x), abs(self.iy - y))
				self.rect_or_mask = 0
				print(" Now press the key 'n' a few times until no further change \n")


		elif event == cv.EVENT_MOUSEMOVE:
			if self.rectangle == True:
				self.img = self.img2.copy()
				cv.rectangle(self.img, (self.ix, self.iy), (x, y), BLUE, 2)
				self.rect = (min(self.ix, x), min(self.iy, y), abs(self.ix - x), abs(self.iy - y))
				self.rect_or_mask = 0

			elif self.drawing == True:
				cv.circle(self.img, (x, y), self.thickness, self.value['color'], -1)
				cv.circle(self.grabcut_mask, (x, y), self.thickness, self.value['val'], -1)



	def run(self):

		while(1):

			cv.imshow('output', self.output)
			cv.imshow('input', self.img)
			k = cv.waitKey(1)

			# key bindings
			if k == ESCAPE_KEY: # Esc to exit
				break

			elif k == ord('b'): # BG drawing
				print(" mark background regions\n")
				self.value = BACKGROUND

			elif k == ord('f'): # FG drawing
				print(" mark foreground regions\n")
				self.value = FOREGROUND

			elif k == ord('2'): # PR_BG drawing
				self.value = PROBABLY_BG

			elif k == ord('3'): # PR_FG drawing
				self.value = PROBABLY_FG

			elif k == ord('s'): # save image
				bar = np.zeros((self.img.shape[0], 5, 3), np.uint8)
				res = np.hstack((self.img2, bar, self.img, bar, self.output))
				cv.imwrite('grabcut_output.png', res)
				print(" Result saved as image \n")

			elif k == ord('r'): # reset everything
				print("resetting \n")
				self.rect = (0,0,1,1)
				self.drawing = False
				self.rectangle = False
				self.rect_or_mask = 100
				self.rect_over = False
				self.value = FOREGROUND
				self.img = self.img2.copy()
				self.grabcut_mask = np.zeros(self.img.shape[:2], dtype = np.uint8) # mask initialized to PR_BG
				self.output = np.zeros(self.img.shape, np.uint8)           # output image to be shown
			
			elif k == ord('n'): # segment the image
				self.segment_with_grabCut()


			self.output = cv.bitwise_and(self.img2, self.img2, mask=self.binary_mask)


if __name__ == '__main__':

	# Loading images
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	else:
		print("No input image given, so loading default image, lena.jpg \n")
		print("Correct Usage: python 2_label_instance_segmentation.py <filename> \n")
		filename = 'lena.jpg'

	print(__doc__)
	InstanceSegmentator(filename).run()
	cv.destroyAllWindows()
