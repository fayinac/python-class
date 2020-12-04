#paint calculator
length = input('Enter length of the room in feet: ')
width = input('Enter width of the room in feet: ')
height = input('Enter height of the room in feet: ')
doors = input('Enter number of doors: ')
windows = input('Enter number of windows: ')

length = int(length)
width = int(width)
height = int(height)
doors = int(doors)
windows = int(windows)

wall_area = (2 * length * height) + (2 * width * height)
wall_area = int(wall_area)
nopaintarea = 20 * doors + 15 * windows
nopaintarea = int(nopaintarea)
paint_area = wall_area - nopaintarea
paint_area = int(paint_area)

print('-----------------')
print('Total surface area to paint: ', paint_area)

gallons = paint_area / 350
print('Number of gallons of paint needed: ', gallons)
