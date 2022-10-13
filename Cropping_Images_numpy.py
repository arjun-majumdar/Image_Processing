

import numpy as np
import imageio
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


"""
Cropping images using numpy


If the center coordinates within the bounding box are (xc, yc)-
1. startX = xc - (image width / 2)
2. startY = yc - (image height / 2)
3. endX = startX + image width
4. endY = startY + image height

startX, startY is the top left corner of the bounding box. While, endX, endY is the
bottom right corner of the bounding box.

The coordinate (0, 0) is the top left corner of the image. Going down increases the Y-axis,
or, the image height. Going to the RHS increases the X-axis, or, the image width.
"""


# Read in image using 'imageio'-
img = imageio.v3.imread("lena.jpg")

# (height, width, channels)-
img.shape
# (1125, 2000, 3)

# Define boundig box dimensions-
width_bbox = height_bbox = 100

# Get/define center coordinates-
xc = 1019
yc = 583

# Compute coordinates for bounding box-
startX = int(xc - (width_bbox / 2))
startY = int(yc - (height_bbox / 2))
endX = int(startX + width_bbox)
endY = int(startY + height_bbox)

startX, startY, endX, endY
# (969, 533, 1069, 633)

# Extract image patch-
extracted_img = img[startY:endY, startX:endX]

extracted_img.shape
# (100, 100, 3)


"""
# define Matplotlib figure and axis-
fig, ax = plt.subplots(figsize = (9, 8))

ax.imshow(img)
ax.set_title("GT img")

# Say that the randomly chosen center has coordinates:
# x = 1019, y = 583

# Draw a circle around the randomly chosen detected point-
ax.add_patch(
    Circle(
    	xy = (xc, yc), radius = 10,
    	edgecolor = 'red', fill = False,
    	lw = 0.5
    	)
)

'''
# Draw a rectangle around the randomly chosen & detected point-
ax.add_patch(
    Rectangle(
        xy = (data['RGB00004.exr'][random_gt_coord][0] - (width_bbox / 2), data['RGB00004.exr'][random_gt_coord][1] - (height_bbox / 2)),
        width = width_bbox, height = height_bbox,
        color = "red", fill = False,
        lw = 0.5
    )
)
'''

# get current axes-
ax = plt.gca()

# hide x-axis-
# ax.get_xaxis().set_visible(False)

# hide y-axis-
# ax.get_yaxis().set_visible(False)

# plt.savefig('8x8_centroids.png')

plt.show()
"""



