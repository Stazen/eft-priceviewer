import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dsi_jto\AppData\Local\Programs\Tesseract-OCR\Tesseract.exe'
# Charger l'image
image = cv2.imread("yo.jpg")
# Convertir en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un seuillage pour obtenir les zones de texte en blanc
_, threshold = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY)
# Inverser les couleurs pour avoir le texte en blanc sur fond noir
#threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
#cv2.imshow("Step 1", threshold)
#cv2.waitKey(0)

threshold = cv2.bitwise_not(threshold)
cv2.imshow("Step 2", threshold)
cv2.waitKey(0)


# Utiliser Tesseract pour détecter le texte
custom_config = r'--oem 3 --psm 6'  # Configuration personnalisée pour Tesseract
text = pytesseract.image_to_string(threshold, config=custom_config)

# Diviser le texte en mots
words = text.split()

# Obtenir les coordonnées des mots détectés par Tesseract
boxes = pytesseract.image_to_boxes(threshold)

# Dessiner les rectangles autour des mots détectés
for b in boxes.splitlines():
    b = b.split()
    # Dessiner un rectangle autour du mot
    cv2.rectangle(image, (int(b[1]), image.shape[0] - int(b[2])), (int(b[3]), image.shape[0] - int(b[4])), (0, 0, 255), 1)

# Afficher l'image avec les rectangles autour des mots détectés
cv2.imshow("Mots détectés", image)
cv2.waitKey(0)
