Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> pyautogui.moveTo(100,200)
>>> pyautogui.moveTo(100,200,duration=2)
>>> pyautogui.position()
Point(x=961, y=307)
>>> pyautogui.moveRel(-100,100,duration=1)
>>> pyautogui.poition();pyautogui.click();pyautogui.typewrite('txt');pyautogui.typewrite(['enter'])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pyautogui.poition();pyautogui.click();pyautogui.typewrite('txt');pyautogui.typewrite(['enter'])
AttributeError: module 'pyautogui' has no attribute 'poition'
>>> pyautogui.position();pyautogui.click();pyautogui.typewrite('txt');pyautogui.typewrite(['enter'])
Point(x=1640, y=373)
>>> pyautogui.position();pyautogui.click();pyautogui.typewrite('txt');pyautogui.typewrite(['enter'])
Point(x=346, y=1079)
>>> pyautogui.moveTo(346,1079,duration=2);pyautogui.click();pyautogui.typewrite('txt');pyautogui.typewrite(['enter'])
>>> 