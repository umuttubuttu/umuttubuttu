import pyautogui
import time

# Kullanıcı Escape tuşuna basana kadar Space tuşuna sürekli basacak
try:
    while True:
        pyautogui.press('space')  # Space tuşuna bas
        time.sleep(0.1)  # 100ms bekle
except KeyboardInterrupt:
    print("Program durduruldu.")
