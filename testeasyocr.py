import easyocr
import cv2
import matplotlib.pyplot as plt

# Charger l'image
image_path = 'yo.jpg'
image = cv2.imread(image_path)

# Initialiser le détecteur de texte d'EasyOCR
reader = easyocr.Reader(['en'])

# Détecter les mots dans l'image
result = reader.readtext(image)

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
