# 🖱️ AutoClicker

This project is a simple Python AutoClicker application that automatically clicks on specific screen positions. It is built using the `pyautogui` and `keyboard` libraries.

## 📦 Contents

- `AutoClicker.py` → Main auto-clicking script.
- `AutoClickerTest.py` → Utility to detect mouse position.

## 🚀 Installation

### Requirements

Make sure you have Python 3.x installed.

You also need to install the following libraries:

```bash
pip install pyautogui keyboard
````

## ⚙️ Usage

### 1. Determine Click Positions

Run `AutoClickerTest.py` to detect the current mouse position:

```bash
python AutoClickerTest.py
```

You will have 5 seconds to move your mouse to the desired position. The coordinates will then be printed to the terminal. Copy these values into the `pos1` and `pos2` variables in `AutoClicker.py`.

### 2. Start the AutoClicker

```bash
python AutoClicker.py
```

* There is a 5-second delay before the clicking starts.
* The program will click on `pos1` and `pos2` sequentially, up to 57 times.
* You can stop the execution at any moment by holding the `F` key.
* Alternatively, you can manually stop it using `Ctrl+C`.

## 🧠 How It Works

* `pyautogui.click((x, y))`: Clicks at the given coordinates.
* `keyboard.is_pressed('f')`: Stops the loop if the `F` key is pressed.
* `time.sleep(seconds)`: Adds a delay between actions.

## 📌 Notes

* Automation works only when the program is in the foreground.
* Coordinates depend on your screen resolution.

---

# 🖱️ AutoClicker

Bu proje, belirli noktalara otomatik olarak tıklama yapan basit bir Python AutoClicker uygulamasıdır. `pyautogui` ve `keyboard` kütüphaneleri kullanılarak oluşturulmuştur.

## 📦 İçerik

- `AutoClicker.py` → Ana otomatik tıklama uygulaması.
- `AutoClickerTest.py` → Mouse konumunu öğrenmek için yardımcı araç.

## 🚀 Kurulum

### Gereksinimler

Python 3.x yüklü olmalıdır.

Aşağıdaki kütüphanelerin yüklenmiş olması gerekir:

```bash
pip install pyautogui keyboard
````

## ⚙️ Kullanım

### 1. Tıklama Konumlarını Belirle

`AutoClickerTest.py` dosyasını çalıştırarak mouse’un pozisyonunu öğrenebilirsin:

```bash
python AutoClickerTest.py
```

5 saniye içinde istediğin konuma mouse'u getir, ardından terminalde pozisyon gözükecektir. Bu konumları `AutoClicker.py` dosyasında `pos1` ve `pos2` değişkenlerine yaz.

### 2. AutoClicker'ı Başlat

```bash
python AutoClicker.py
```

* Başlamadan önce 5 saniyelik gecikme vardır.
* Program, sırayla `pos1` ve `pos2` konumlarına 57 defaya kadar tıklar.
* `F` tuşuna basarak işlemi anlık olarak durdurabilirsin.
* `Ctrl+C` ile de program manuel olarak durdurulabilir.

## 🧠 Nasıl Çalışır?

* `pyautogui.click((x, y))`: Verilen koordinata tıklama yapar.
* `keyboard.is_pressed('f')`: Kullanıcı `F` tuşuna basarsa döngü kırılır.
* `time.sleep(saniye)`: Tıklamalar arasında gecikme sağlar.

## 📌 Notlar

* Otomasyon araçları masaüstünde aktif olarak çalışır. Arka planda çalışmaz.
* Koordinatlar ekran çözünürlüğüne göre değişebilir.
