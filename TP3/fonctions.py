import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv



def bruitage(img, nombre_pixel_bruite):

    result = img.copy() # On prend une copie sinon on modifie aussi l'originale
    mapping = lambda a: 255 if a > 0.5 else 0 #Fonction lambda pour le bruitage

    for n in range(0,nombre_pixel_bruite):
        x = np.random.randint(0,img.shape[0] - 1)
        y = np.random.randint(0,img.shape[1] - 1)
        result[x,y] = mapping(np.random.rand())

    return result



def filtrage_median(img, pattern_size=5):
    
    result = img.copy()

    for i in range(0, result.shape[0]):
        for j in range(0, result.shape[1]):
            zone = sorted(list(np.reshape(img[i:i + pattern_size, j:j + pattern_size], -1)))
            median_value = zone[len(zone)//2]
            result[i,j] = median_value

    return result



def EQM_value(img_originale, img_modifiee):
    return ((img_originale - img_modifiee)**2).mean()



def display_EQM_graph(img_originale, debut, fin, pas):

    print("Computing ...")

    EQM_bruit = []
    EQM_median = []

    for nombre_pixel_bruit in range(debut, fin, pas):
            
            img_bruitee = bruitage(img_originale, nombre_pixel_bruit)
            img_median = filtrage_median(img_bruitee)

            EQM_bruit.append((nombre_pixel_bruit, EQM_value(img_originale, img_bruitee)))
            EQM_median.append((nombre_pixel_bruit, EQM_value(img_originale, img_median)))

    print("Done !")

    plt.plot(*zip(*EQM_bruit), color='r', label="EQM bruit")
    plt.plot(*zip(*EQM_median), color='g', label="EQM median")

    plt.xlabel("Nombre de pixel de bruit")
    plt.ylabel("EQM")
    plt.legend()

    plt.show()
    


def floutage(img, ksize=5): # MARCHE PAS
    return cv.blur(img.copy(), ksize)