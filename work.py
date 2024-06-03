import math
import time
import random
from pynput import mouse,keyboard


m = mouse.Controller()
k = keyboard.Controller()

def mouse_scroll():
	m.position = (800, 500)
	scroll_step = random.randrange(-5, 5)
	m.scroll(0, scroll_step)

def keyboard_input():
	index = random.randrange(0,25)
	keys = "abcdefghijklmnopqrstuvwxyz"
	k.press(keys[index])
	k.release(keys[index])
	if random.randrange(0,10) == 1:
		k.press(keyboard.Key.enter)
		k.release(keyboard.Key.enter)


def main():
	while True:
		if random.randrange(0,25) > -1:
			mouse_scroll()
		else:
			keyboard_input()
		time.sleep(2)


if __name__ == '__main__':
	main()