import pyautogui
import time

print("Mouse konumunu öğrenmek için 5 saniye içinde istediğin yere git.")
time.sleep(5)
print(f"Mouse pozisyonu: {pyautogui.position()}")
