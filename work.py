import time
import pyautogui
import random
from pynput import mouse,keyboard

m = mouse.Controller()
k = keyboard.Controller()

def ctrl_tab_multiple_times(tab_count):
    # Press and hold the Ctrl key
    pyautogui.keyDown('ctrl')
    
    # Press the Tab key multiple times
    for _ in range(tab_count):
        pyautogui.press('tab')
    
    # Release the Ctrl key
    pyautogui.keyUp('ctrl')

def mouse_scroll():
	m.position = (900, 500)
	scroll_step = random.randrange(-200, 200)
	m.scroll(0, scroll_step)
	print("scroll")

def keyboard_input():
	index = random.randrange(0,25)
	keys = "abcdefghijklmnopqrstuvwxyz"

	k.press(keys[index])
	k.release(keys[index])
	t_i = random.randrange(0,10)
	time.sleep(t_i)
	k.press(keyboard.Key.backspace)
	k.release(keyboard.Key.backspace)
	if(t_i < 5):
		k.press(keyboard.Key.enter)
		k.release(keyboard.Key.enter)
	time.sleep(1)
	print("keypress")

def main():
	while True:
		flag = random.randrange(0,50)
		print(flag)
		if flag > 20:
			mouse_scroll()
		else:
			keyboard_input()
		if(flag < 5):
			ctrl_tab_multiple_times(flag)
			mouse_scroll()
			time.sleep(1)
		time.sleep(1)

if __name__ == '__main__':
	main()