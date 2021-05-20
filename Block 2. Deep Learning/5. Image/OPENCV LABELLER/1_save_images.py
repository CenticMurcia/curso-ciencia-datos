import cv2
import time

########################### CONSTANTS

PERSON_NAME = "javi"
KEY_ESCAPE  = 27
KEY_B       = ord("b")
KEY_N       = ord("n")
KEY_M       = ord("m")
WIDTH       = cv2.CAP_PROP_FRAME_WIDTH   # 3
HEIGHT      = cv2.CAP_PROP_FRAME_HEIGHT  # 4


########################### SET CAMERA AT 640x480

cap = cv2.VideoCapture(0)

width  = cap.get(WIDTH)
height = cap.get(HEIGHT)
print(f"Original resolution {width}x{height}")

# Change the resolution
cap.set(WIDTH,  640)
cap.set(HEIGHT, 480)


########################### MAIN LOOP

count_mask     = 0
count_no_mask  = 0
count_bad_mask = 0

while True:
	_, frame = cap.read()

	cv2.imshow('selfie', frame) # Display the current selfie

	key = cv2.waitKey(delay=1)

	if key == KEY_N: # NO MASK
		cv2.imwrite(f"dataset/no_mask/{PERSON_NAME}_{int(time.time())}.jpg", frame)
		count_no_mask += 1
	
	elif key == KEY_M: # MASK
		cv2.imwrite(f"dataset/mask/{PERSON_NAME}_{int(time.time())}.jpg", frame)
		count_mask += 1
	
	elif key == KEY_B: # BAD USAGE OF MASK
		cv2.imwrite(f"dataset/bad_mask/{PERSON_NAME}_{int(time.time())}.jpg", frame)
		count_bad_mask += 1

	elif key == KEY_ESCAPE: # When everything done
		cap.release()           # release the capture (turn off the camara)
		cv2.destroyAllWindows() # Close the window
		break


