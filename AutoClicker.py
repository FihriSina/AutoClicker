import pyautogui
import time
import keyboard  

# İlk ve ikinci tıklama konumları
pos1 = (1868, 271)
pos2 = (1746, 513)

# Bekleme süreleri
wait1 = 3
wait2 = 0.5

print("Program başlıyor. F tuşuna basılı tutarak işlemi durdurabilirsin.")
time.sleep(5)

try:
    for i in range(57):
        print(i, "Döngü Aşaması:")
        if keyboard.is_pressed('f'):
            print("\nF tuşuna basıldı, program durduruluyor.")
            break

        pyautogui.click(pos1)
        print(f"1. tıklama yapıldı: {pos1}")
        time.sleep(wait1)

        if keyboard.is_pressed('f'):
            print("\nF tuşuna basıldı, program durduruluyor.")
            break

        pyautogui.click(pos2)
        print(f"2. tıklama yapıldı: {pos2}")
        time.sleep(wait2)

except KeyboardInterrupt:
    print("\nCtrl+C ile durduruldu.")
