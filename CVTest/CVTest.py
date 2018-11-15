import cv2 as cv
img = cv.imread("cloud.jpg")
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()