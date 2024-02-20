import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Charger l'image
image_path = 'yo.jpg'
image = cv2.imread(image_path)

# Prétraitement de l'image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Appliquer une binarisation pour séparer le texte du fond
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Initialiser le détecteur de texte d'EasyOCR pour la langue anglaise
reader = easyocr.Reader(['en'])

# Détecter les mots dans l'image avec un seuil de confiance
result = reader.readtext(binary, min_size=0, slope_ths=0.1, ycenter_ths=0.5, height_ths=0.5, width_ths=0.5, 
                         y_ths=0.5, x_ths=1.0, add_margin=0.5, text_threshold=0.7, low_text=0.4, link_threshold=0.4, 
                         canvas_size=2560, mag_ratio=1.0)

# Dessiner des rectangles rouges autour des mots détectés
image_with_boxes = image.copy()
for detection in result:
    # Récupérer les coordonnées du rectangle
    box = detection[0]
    points = box[:4]
    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]
    xmin = min(x_coordinates)
    xmax = max(x_coordinates)
    ymin = min(y_coordinates)
    ymax = max(y_coordinates)
    # Dessiner le rectangle rouge
    cv2.rectangle(image_with_boxes, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)
    print(detection[1])

# Afficher l'image avec les rectangles rouges
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
