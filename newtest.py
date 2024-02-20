import numpy as np
from PIL import ImageGrab
import cv2

# Fonction pour détecter les zones délimitées par une couleur spécifique
def detect_zones(image, color_lower, color_upper, min_contour_area=100):
    # Convertir l'image en format RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convertir l'image en format HSV (teinte, saturation, valeur)
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Créer un masque pour la couleur spécifique
    mask = cv2.inRange(hsv_image, color_lower, color_upper)
    
    # Trouver les contours dans le masque
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dessiner des rectangles autour des zones détectées pour le débogage
    for contour in contours:
        # Filtrer les petits contours indésirables
        if cv2.contourArea(contour) > min_contour_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Dessiner un rectangle rouge
    
    return image

# Couleur spécifique à détecter en HSV
color_lower = np.array([85, 80, 85])
color_upper = np.array([105, 120, 120])

# Capturer un screenshot de l'écran
screenshot = np.array(ImageGrab.grab())

# Détecter les zones délimitées par la couleur spécifique et dessiner des rectangles rouges
processed_image = detect_zones(screenshot, color_lower, color_upper)

# Afficher l'image avec les rectangles dessinés
cv2.imshow('Debug', processed_image)

# Attendre jusqu'à ce que la touche 'q' soit pressée pour fermer la fenêtre
cv2.waitKey(0)

# Fermer la fenêtre lorsque la touche 'q' est pressée
cv2.destroyAllWindows()
