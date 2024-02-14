import keyboard
import pyautogui
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dsi_jto\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def on_triggered():
    # Détecte la position de la souris
    mouse_x, mouse_y = pyautogui.position()
    print(f"Ctrl + F détecté ! Position de la souris : ({mouse_x}, {mouse_y})")

    # Capture d'écran autour de la position de la souris
    screenshot = ImageGrab.grab(bbox=(mouse_x, mouse_y - 20, mouse_x + 300, mouse_y + 20))
    # OCR pour détecter le texte dans la capture d'écran
    text = pytesseract.image_to_string(screenshot)
    print("Texte détecté à droite de la souris:", text)

keyboard.add_hotkey('ctrl+f', on_triggered)

input("Appuyez sur Entrée pour quitter...\n")