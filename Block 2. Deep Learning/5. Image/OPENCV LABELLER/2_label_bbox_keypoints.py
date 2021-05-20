
# https://stackoverflow.com/questions/55149171/how-to-get-roi-bounding-box-coordinates-with-mouse-clicks-instead-of-guess-che
# https://docs.opencv.org/master/db/d5b/tutorial_py_mouse_handling.html

import pandas as pd
import cv2
from pathlib import Path
#import os


########################### CONSTANTS


PATH_DATASET = Path("dataset")
PATH_MASK    = PATH_DATASET/"mask"
PATH_NOMASK  = PATH_DATASET/"no_mask"
PATH_BADMASK = PATH_DATASET/"bad_mask"

TEXT_FONT      = cv2.FONT_HERSHEY_SIMPLEX 
TEXT_COORDS    = (30, 50) 
TEXT_SCALE     = 0.8
TEXT_COLOR     = (255, 0, 0)  # Blue (BGR)
TEXT_THICKNESS = 2 # 2 px 

BBOX_LEN       = 100
BBOX_COLOR     = (36,255,12) # light green (BGR)
BBOX_THICKNESS = 2

KEYPOINT_LEN       = 10
KEYPOINT_COLOR     = (36,12,255) # red (BGR)
KEYPOINT_THICKNESS = 2



########################### BOUNDING BOX Labeler

class BoundingBoxLabeler():

	def __init__(self, img):

		self.img_original = img
		self.img_bbox = self.img_original.copy()
		self.top_left_coords = None
		self.clicked = False
		self.is_bbox = False

		cv2.namedWindow("image")
		cv2.setMouseCallback("image", self.mouse_events)

	def mouse_events(self, event, x, y, flags, parameters):
		
		# MOVE MOUSE -> Show fancy cursor
		if event == cv2.EVENT_MOUSEMOVE and self.clicked == False:
			self.img_bbox = self.img_original.copy()
			cv2.line(self.img_bbox, (x,y), (x+BBOX_LEN,y), BBOX_COLOR, thickness=BBOX_THICKNESS)
			cv2.line(self.img_bbox, (x,y), (x,y+BBOX_LEN), BBOX_COLOR, thickness=BBOX_THICKNESS)

		# MOUSE LEFT CLICK -> Save top left (x,y) coordinates
		elif event == cv2.EVENT_LBUTTONDOWN:
			self.clicked = True
			self.top_left_coords = (x,y)

		# MOVE CLICKED MOUSE -> Show current bounding box
		elif event == cv2.EVENT_MOUSEMOVE and self.clicked == True:
			self.img_bbox = self.img_original.copy()
			cv2.rectangle(self.img_bbox, self.top_left_coords, (x,y), BBOX_COLOR, BBOX_THICKNESS)

		# MOUSE RELEASE LEFT CLICK -> Save width and height
		elif event == cv2.EVENT_LBUTTONUP:
			self.clicked = False
			bottom_right_coords = (x,y)

			self.width  = bottom_right_coords[0] - self.top_left_coords[0]
			self.height = bottom_right_coords[1] - self.top_left_coords[1]
			self.is_bbox = True

	def wait_for_bbox(self):

		# Wait for bounding box (see mouse events)
		while not self.is_bbox:
			
			cv2.imshow("image", self.img_bbox)

			# Close program with keyboard "ESCAPE"
			key = cv2.waitKey(1)
			if key == 27:
				cv2.destroyAllWindows()
				exit(1)

		x = self.top_left_coords[0]
		y = self.top_left_coords[1]
		w = self.width
		h = self.height

		return x,y,w,h


########################### KEY_POINT Labeler


class KeyPointLabeler():

	def __init__(self, img, max_keypoints=2):

		self.img_original  = img
		self.img_keypoints = self.img_original.copy()
		self.max_keypoints = max_keypoints
		self.keypoints     = []

		cv2.namedWindow("image")
		cv2.setMouseCallback("image", self.mouse_events)


	def mouse_events(self, event, x, y, flags, parameters):
		
		# MOVE MOUSE -> Show fancy cursor
		if event == cv2.EVENT_MOUSEMOVE:
			self.img_keypoints = self.img_original.copy()
			cv2.line(self.img_keypoints, (x-KEYPOINT_LEN,y-KEYPOINT_LEN), (x+KEYPOINT_LEN,y+KEYPOINT_LEN), KEYPOINT_COLOR, thickness=KEYPOINT_THICKNESS)
			cv2.line(self.img_keypoints, (x-KEYPOINT_LEN,y+KEYPOINT_LEN), (x+KEYPOINT_LEN,y-KEYPOINT_LEN), KEYPOINT_COLOR, thickness=KEYPOINT_THICKNESS)

		# MOUSE RELEASE LEFT CLICK -> Save width and height
		elif event == cv2.EVENT_LBUTTONUP:
			cv2.line(self.img_original, (x-KEYPOINT_LEN,y-KEYPOINT_LEN), (x+KEYPOINT_LEN,y+KEYPOINT_LEN), KEYPOINT_COLOR, thickness=KEYPOINT_THICKNESS)
			cv2.line(self.img_original, (x-KEYPOINT_LEN,y+KEYPOINT_LEN), (x+KEYPOINT_LEN,y-KEYPOINT_LEN), KEYPOINT_COLOR, thickness=KEYPOINT_THICKNESS)
			self.keypoints.append((x,y))


	def wait_for_keypoints(self):

		# Wait for bounding box (see mouse events)
		while len(self.keypoints) < self.max_keypoints:
			
			cv2.imshow("image", self.img_keypoints)

			# Close program with keyboard "ESCAPE"
			key = cv2.waitKey(1)
			if key == 27:
				cv2.destroyAllWindows()
				exit(1)

		return self.keypoints




if __name__ == "__main__":

	df = pd.DataFrame()

	classes = {
		"MASK":     PATH_MASK,
		"NO_MASK":  PATH_NOMASK,
		"BAD_MASK": PATH_BADMASK,
	}

	for class_name, class_path in classes.items():

		#imgs_paths = os.listdir(class_path)    # This returns images_filenames
		imgs_paths = list(class_path.iterdir()) # This returns images_realive_paths

		for i, img_path in enumerate(imgs_paths): 

			if str(img_path).endswith(".jpg"):

				img = cv2.imread(str(img_path))

				cv2.putText(img, class_name+" "+str(i+1)+"/"+str(len(imgs_paths)), TEXT_COORDS, TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS, cv2.LINE_AA) 

				bbox_labeler = BoundingBoxLabeler(img=img)
				x,y,w,h      = bbox_labeler.wait_for_bbox()
				img = bbox_labeler.img_bbox

				kpoint_labeler  = KeyPointLabeler(img=img, max_keypoints=2)
				(x1,y1), (x2,y2) = kpoint_labeler.wait_for_keypoints()
				
				print(f"Image: {img_path}")
				print(f"class: {class_name}")
				print(f"x: {x}")
				print(f"y: {y}")
				print(f"w: {w}")
				print(f"h: {h}")
				print(f"x1: {x1}")
				print(f"y1: {y1}")
				print(f"x2: {x2}")
				print(f"y2: {y2}")

				df = df.append({
					"image": str(img_path),
					"class": class_name,
					"bbox_x": x,
					"bbox_y": y,
					"bbox_w": w,
					"bbox_h": h,
					"kp1_x": x1,
					"kp1_y": y1,
					"kp2_x": x2,
					"kp2_y": y2,
				}, ignore_index=True)

	int_variables = ["bbox_x", "bbox_y", "bbox_w", "bbox_h", "kp1_x", "kp1_y", "kp2_x", "kp2_y"]
	df[int_variables] = df[int_variables].astype(int) # float to int
	df = df[["image", "class", "bbox_x", "bbox_y", "bbox_w", "bbox_h", "kp1_x", "kp1_y", "kp2_x", "kp2_y"]]
	df.to_csv("dataset/mask_df.csv", index=False)