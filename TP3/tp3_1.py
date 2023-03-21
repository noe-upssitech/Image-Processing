import cv2 as cv
import fonctions

img_originale = cv.imread("TP3/image.png")
img = img_originale[:,:,0]

# Bruitage
#img_bruitee = fonctions.bruitage(img, nombre_pixel_bruite = 10_000)

# Filtre Median
#img_median = fonctions.filtrage_median(img, 10)

# Erreur quadratique moyenne
fonctions.display_EQM_graph(img, debut=67_500, fin=72_500, pas=100) # Croisement à environ 68_100p

"""
cv.imshow("Image originale", img_originale)
cv.imshow("Image bruitee", img_bruitee)
cv.imshow("Image filtre median", img_median)
cv.waitKey(0)
cv.destroyAllWindows()
"""