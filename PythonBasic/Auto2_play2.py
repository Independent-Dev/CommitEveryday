import pyautogui as pa
import time

# i = pa.locateCenterOnScreen('music.png')
# pa.doubleClick(i)

pa.screenshot('kogan.png', region=(1354, 273, 30, 30))
i = pa.locateCenterOnScreen('kogan.png')
pa.doubleClick(i)

time.sleep(1)
pa.typewrite(['space'])
