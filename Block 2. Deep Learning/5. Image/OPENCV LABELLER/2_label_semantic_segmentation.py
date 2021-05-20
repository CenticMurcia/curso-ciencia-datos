'''
====================================================================
Interactive Semantic Segmentation using GrabCut algorithm.

USAGE:

	python 2_label_semantic_segmentation.py <img_filename>

	Two windows will show up, one for input and one for output.
	At first, in input window, draw lines on the areas you want.

	Key 'b' - To select areas of sure background
	Key 'f' - To select areas of sure foreground
	Key '+' - To make the brush bigger
	Key '-' - To make the brush smaller
	Key 'r' - To reset the setup
	Key 's' - To save the results

====================================================================
'''

import numpy as np
import cv2   as cv
import sys


SCREEN_WINDOW_POS = {"top": 500, "left": 500}
ESCAPE_KEY = 27

BLUE       = [255,  0,  0]
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


class SemanticSegmentator():

	def __init__(self, img_path):

		self.img_path     = img_path
		self.img_original = cv.imread(cv.samples.findFile(self.img_path))
		self.img_drawn    = self.img_original.copy()
		self.img_show     = self.img_original.copy() # a copy of original image
		self.grabcut_mask = np.full(shape      = self.img_original.shape[:2], # mask initialized to PR_BG
			                        fill_value = PROBABLY_BG["val"],
			                        dtype      = np.uint8)
		self.binary_mask = np.zeros(self.img_original.shape[:2], dtype=np.uint8) # output image to be shown


		self.drawing   = False      # State for brush drawing or not
		self.brush     = FOREGROUND # drawing initialized to FG
		self.brush_size = 5         # brush thickness

		self.mouse_x = 0
		self.mouse_y = 0
		
		# input and output windows
		cv.namedWindow('input')
		cv.namedWindow('output')
		cv.moveWindow('input',  x=SCREEN_WINDOW_POS["top"],                            y=SCREEN_WINDOW_POS["left"])
		cv.moveWindow('output', x=SCREEN_WINDOW_POS["top"]+self.img_original.shape[1], y=SCREEN_WINDOW_POS["left"])
		cv.setMouseCallback('input', self.mouse_events)


	def mouse_events(self, event, x, y, flags, param):

		if event == cv.EVENT_LBUTTONDOWN:
			self.drawing = True
			cv.circle(self.img_drawn, (x, y), self.brush_size, self.brush['color'], -1)
			cv.circle(self.grabcut_mask, (x, y), self.brush_size, self.brush['val'], -1)
			self.img_show = self.img_drawn.copy()

		elif event == cv.EVENT_LBUTTONUP:
			self.drawing = False
			self.segment_with_grabCutMask()

		elif event == cv.EVENT_MOUSEMOVE:
			self.mouse_x = x
			self.mouse_y = y

			if not self.drawing:
				self.img_show = self.img_drawn.copy()
				cv.circle(self.img_show, (x, y), self.brush_size, self.brush['color'], -1)
			else:
				cv.circle(self.img_drawn, (x, y), self.brush_size, self.brush['color'], -1)
				cv.circle(self.grabcut_mask, (x, y), self.brush_size, self.brush['val'], -1)
				self.img_show = self.img_drawn.copy()

		elif event == cv.EVENT_MOUSEWHEEL:
			if flags > 0: #scroll up
				self.change_brush_size(self, +5)
			else: # scroll down
				self.change_brush_size(self, -5)
		
	def change_brush_type(self, new_brush):
		self.brush = new_brush
		self.img_show = self.img_drawn.copy()
		cv.circle(self.img_show, (self.mouse_x, self.mouse_y), self.brush_size, self.brush['color'], -1)

	def change_brush_size(self, increment):
		if self.brush_size + increment > 0:
			self.brush_size = self.brush_size + increment
			self.img_show = self.img_drawn.copy()
			cv.circle(self.img_show, (self.mouse_x, self.mouse_y), self.brush_size, self.brush['color'], -1)

	def segment_with_grabCutMask(self):
		# GC_INIT_WITH_RECT marks all pixels outside the given rect as "background"
		# and all pixels inside the rect as "probably foreground"

		bgdmodel = np.zeros((1, 65), np.float64)
		fgdmodel = np.zeros((1, 65), np.float64)
		cv.grabCut(self.img_original, self.grabcut_mask, None, bgdmodel, fgdmodel, 1, cv.GC_INIT_WITH_MASK) # self.grabcut_mask, bgdmodel, fgdmodel ARE UPDATED HERE

		self.binary_mask = ( (self.grabcut_mask==FOREGROUND["val"]) | (self.grabcut_mask==PROBABLY_FG["val"]) ).astype('uint8') * 255


	def run(self):

		while(1):

			cv.imshow('input', self.img_show)

			output = cv.bitwise_and(self.img_original, self.img_original, mask=self.binary_mask)
			cv.imshow('output', output)
			
			key = cv.waitKey(1)

			# key bindings
			if key == ESCAPE_KEY: # Esc to exit
				break

			elif key == ord('+'):
				self.change_brush_size(+10)

			elif key == ord('-'):
				self.change_brush_size(-10)

			elif key == ord('b'): # BG drawing
				self.change_brush_type(BACKGROUND)

			elif key == ord('f'): # FG drawing
				self.change_brush_type(FOREGROUND)

			elif key == ord('s'): # save image
				print("Saving img_masked.png")
				img_masked = np.dstack((self.img_original, self.binary_mask)) # Put mask into alpha channel
				cv.imwrite("img_masked.png", img_masked)

			elif key == ord('r'): # reset everything
				print("resetting \n")
				self.__init__(self.img_path)

if __name__ == '__main__':

	# Loading images
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	else:
		print("No input image given, so loading default image, lena.jpg \n")
		print("Correct Usage: python 2_label_semantic_segmentation.py <filename> \n")
		filename = 'lena.jpg'

	print(__doc__)
	SemanticSegmentator(filename).run()
	cv.destroyAllWindows()
