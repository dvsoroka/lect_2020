from graph import *

def main():
	windowSize(500, 600)
	paint_house(100, 200, 300, 400)
	x = 100
	y = 300
	width = 300
	height = 400
	run() # запускает холст

def paint_house(x, y, width, height):
	paint_walls(x, y, width, height//2)
	paint_roof(x, y, width, height//2)
	w_height = height//4
	w_width = width//2
	paint_window(x + w_width//2, y + w_height//2, w_width, w_height)

def paint_walls(x, y, width, height):
	print("Рисую стны", x, y)
	brushColor("green")
	rectangle(x, y, x + width, y + height)
def paint_roof(x, y, width, height):
	brushColor("gold")
	points = ((x, height), (x + width, height), (x + width//2, y - height//1.6), (x, height))
	polygon(points)
def paint_window(x, y, w_width, w_height):
	brushColor("white")
	rectangle(x, y, x + w_width, y + w_height)

main()


# python house_fin.py
# git add house_fin.py
# git commit -m #Вызвал функцию рисования домика. Пока это - функция-заглушка


