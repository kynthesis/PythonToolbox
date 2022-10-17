# Importing all necessary libraries
import argparse
import cv2
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='Input video path')
args = parser.parse_args()

# Read the video from specified path
video_name = args.input.split('.')[0]
video = cv2.VideoCapture(args.input)

try:
	
	# creating a folder named data
	if not os.path.exists(video_name):
		os.makedirs(video_name)

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
	
	# reading from frame
	ret,frame = video.read()

	if ret:
		# if video is still left continue creating images
		name = f'./{video_name}/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name)

		# writing the extracted images
		cv2.imwrite(name, frame)

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1
	else:
		break

# Release all space and windows once done
video.release()
cv2.destroyAllWindows()
