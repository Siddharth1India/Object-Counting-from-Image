# Importing opencv library and checking version just to be sure that it is getting imported just fine

import cv2
print(cv2.__version__)


# Reading image, resizing it so It is fit on screen and performing crop 
# to remove side (in case image is taken manually, it helps removing borders)

img = cv2.imread("Siddharth_P\Q2\count=10.jpeg")
img = cv2.resize(img, (640, 480))
img = img[:-10, :-10]

# Canny operation with th1 as 550 and th2 as 50 values. Selected after trial and error
canny = cv2.Canny(img, 550, 50)
# Blur operation on canny as canny usually returns sharp edges but bluring image makes one object
# easier to identify, Kernel and Standard Deviation set after trying to visualize stuff
blur = cv2.GaussianBlur(canny,(25,25),4)

# Defining contours with CHAIN_APPROX_SIMPLE but CHAIN_APPROX_NONE will also give similar results here (tested)
# Using blur copy because I wanted to preserve blur as it is for future use
cnt, hierarchy = cv2.findContours(blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Drawing contours on original image, Color == Red, Width of marker == 2 and 1 because I want to draw all 
# contours
cv2.drawContours(img, cnt, -1, (0,0,255), 2)
cv2.imshow("Output", img)
cv2.waitKey(0)

print(f"Number of Objects: {len(cnt)}")