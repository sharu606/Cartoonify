# Cartoonify
Cartoonify an image using OpenCV.

# Packages used
* cv2
* os
* tkinter
* sys
* easygui
* matplotlib.pyplot

## Steps Involved
### Step 1
Read the image and confirm that an image is chosen.
Convert the image into RBG scale.

### Step 2
Convert it into gray scale for further processing.

### Step 3
Blur the image using Gaussian blur to reduce noise.

### Step 4
Find the edges using adaptive threshold.

### Step 5
Blur the original image using median blur to apply colors to the edges.

### Step 6 
Mask the color image and the edges using bitwise_and() and save the image using imwrite().
