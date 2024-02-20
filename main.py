import keyboard
import pyautogui
import pytesseract
from PIL import ImageGrab
import item_network

DATAITEMS = []


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dsi_jto\AppData\Local\Programs\Tesseract-OCR\Tesseract.exe'

def on_triggered():
    # Détecte la position de la souris
    mouse_x, mouse_y = pyautogui.position()
    print(f"Ctrl + F détecté ! Position de la souris : ({mouse_x}, {mouse_y})")

    # Capture d'écran autour de la position de la souris
    screenshot = ImageGrab.grab(bbox=(mouse_x + 30, mouse_y - 20, mouse_x + 500, mouse_y + 20))
    # OCR pour détecter le texte dans la capture d'écran
    text = pytesseract.image_to_string(screenshot)
    print("Texte détecté à droite de la souris:", text)
    
    #for item in DATAITEMS:
    #    print("Name:", item.name)
    #    print("Short Name:", item.short_name)
    #    print("Normalized Name:", item.normalized_name)
    #    print("Sell For:")
    #    for price in item.sell_for:
    #        print("- Vendor:", price.vendor.name)
    #        print("  Price:", price.price)
    #        print("  Currency:", price.currency)
    #    print()

keyboard.add_hotkey('ctrl+f', on_triggered)

input("Appuyez sur Entrée pour quitter...\n")


def main():
    DATAITEMS = item_network.GetInformation();


if __name__ == "__main__":
    main()