import pyautogui
import time

# Kullanıcı Escape tuşuna basana kadar sol fare tıklamasına sürekli basacak
try:
    while True:
        pyautogui.click()  # Sol fare tıklaması yap
        time.sleep(0.1)  # 100ms bekle
except KeyboardInterrupt:
    print("Program durduruldu.")
