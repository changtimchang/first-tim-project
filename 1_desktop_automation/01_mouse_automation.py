import pyautogui
import time

#1. 화면크기 출력
# print(pyautogui.size())

#2. 마우스위치 출력
# time.sleep(2)
# print(pyautogui.position())

#3. 마우스 이동

# pyautogui.moveTo(1326, 307, 2)
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval =1 )

pyautogui.moveTo(1326,307, 2)
pyautogui.dragTo(1326,100, 2)