import numpy as np
import cv2 as cv
from numpy.linalg import inv
# img = cv.imread('a.tif')
# max_num = 0
# b, g, r= cv2.split(img)
# print(img)


compA = cv.imread('c1.jpg',cv.IMREAD_UNCHANGED)
backA = cv.imread('b1.jpg',cv.IMREAD_UNCHANGED)
compB = cv.imread('c2.jpg')
backB = cv.imread('b2.jpg',cv.IMREAD_UNCHANGED)
print('imgae dtype', compA.dtype)
print('image dtype', backA.dtype)
cA_b, cA_g, cA_r = cv.split(compA)
bA_b, bA_g, bA_r = cv.split(backA)
cB_b, cB_g, cB_r = cv.split(compB)
bB_b, bB_g, bB_r = cv.split(backB)
row = len(compA)
column = len(compA[0])
alphOut = np.zeros(compA.shape)
colOut = np.zeros(compA.shape)
print(compA.shape)
print(backA.shape)
for r in range(0,row):
    for c in range(0,column):
        b = np.array([int(cA_b[r][c]) - int(bA_b[r][c]), 
                      int(cA_g[r][c]) - int(bA_g[r][c]), 
                      int(cA_r[r][c]) - int(bA_r[r][c]), 
                      int(cB_b[r][c]) - int(bB_b[r][c]), 
                      int(cB_g[r][c]) - int(bB_g[r][c]), 
                      int(cB_r[r][c]) - int(bB_r[r][c])])
        A = np.array([[1,0,0,-int(bA_b[r][c])],
                      [0,1,0,-int(bA_g[r][c])],
                      [0,0,1,-int(bA_r[r][c])],
                      [1,0,0,-int(bB_b[r][c])],
                      [0,1,0,-int(bB_g[r][c])],
                      [0,0,1,-int(bB_r[r][c])]])
        x = np.clip(np.linalg.pinv(A).dot(b),0,255)
        # print(x[3])
        # print(x)
        colOut[r,c] = np.array([x[0], x[1], x[2]])
        # colOut[r,c] = np.array(x[0], x[1], x[2])
        alphOut[r,c] = np.array([(255 * x[3]), (255 * x[3]), (255 * x[3])])
print(alphOut)
cv.imwrite('c.tif',colOut)
cv.imwrite('a.tif', alphOut)
# print(colOut)
print(alphOut)
# print(img)
# print(b)
# new = img +100
# cv2.imshow("windows name", new)
# cv2.waitKey(0)
# print(img.shape)
# for i in img:
# 	print(i)
