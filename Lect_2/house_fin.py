from graph import *

def main():
	windowSize(500, 600)
	paint_house(100, 200, 300, 400)
	x = 100
	y = 200
	width = 300
	height = 400
	run() # запускает холст

def paint_house(x, y, width, height):
	paint_walls(x, y, width, height//2)
	paint_roof(x, y, width, height//2)
	w_height = height//6
	w_width = width//2
	paint_window(x + w_width, y//2 + w_height, w_width, w_height)

def paint_walls(x, y, width, height):
	print("Рисую стны", x, y)
	pass
def paint_roof(x, y, width, height):
	pass
def paint_window(x, y, w_width, w_height):
	pass

main()


