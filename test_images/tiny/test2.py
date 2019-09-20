import cv2
import numpy as np

# img = np.array(cv2.imread('a.tif'))
# img2 = cv2.imread('alpha.tif')
# print(img)

alphaIn = cv2.imread('alpha.tif')
colIn = cv2.imread('col.tif')
backIn = cv2.imread('window.jpg')
print(backIn.shape)
compOut = np.zeros(backIn.shape)
row = len(backIn)
column = len(backIn[0])
for r in range(0, row):
    for c in range(0, column):
        a = alphaIn[r][c][0]/255.0
        compOut_bgr = colIn[r][c] + ((1-a) * backIn[r][c])
        compOut[r,c] = np.array(compOut_bgr)
cv2.imwrite('new.jpg', compOut)

