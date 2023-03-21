import cv2 as cv
import fonctions

img_originale = cv.imread("TP3/image.png")
img = img_originale[:,:,0]

img_floue = fonctions.floutage(img)

cv.imshow("Image originale", img_originale)
cv.imshow("Image floue", img_floue)
cv.waitKey(0)
cv.destroyAllWindows()