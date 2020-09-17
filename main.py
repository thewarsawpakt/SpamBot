import pynput
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

length = input("Enter attack length: ")
for i in range(3):
    time.sleep(1)
print("Attack ready...")
try:
    for i in range(int(length)):
        missiles = abs(int(i) - int(length))
        keyboard.type(f"This is an attack from the CreePakt allaiance. The attack will be over in {missiles} missiles. Please do not fret.")
        time.sleep(0.5)
        keyboard.press(Key.enter)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
keyboard.type(f"Attack over.")
keyboard.press(Key.enter)