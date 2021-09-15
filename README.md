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
<br>
<img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/ok.PNG?raw=true" style="height: 240px;"> &nbsp;&nbsp;&nbsp; <img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/1.PNG?raw=true" style="height: 240px;">

### Step 2
Convert it into gray scale for further processing.
<br>
<img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/2.PNG?raw=true" style="height: 240px;">

### Step 3
Blur the image using Gaussian blur to reduce noise.
<br>
<img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/3.PNG?raw=true" style="height: 240px;">

### Step 4
Find the edges using adaptive threshold.
<br>
<img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/4.PNG?raw=true" style="height: 240px;">

### Step 5
Blur the original image using median blur to apply colors to the edges.
<br>
<img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/5.PNG?raw=true" style="height: 240px;">

### Step 6 
Mask the color image and the edges using bitwise_and() and save the image using imwrite().
<br>
<img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/Screenshot%20(443).png?raw=true" style="height: 240px;"> &nbsp;&nbsp;&nbsp; <img src="https://github.com/sharu606/Cartoonify/blob/main/Screen%20shots/6.PNG?raw=true" style="height: 240px;">
