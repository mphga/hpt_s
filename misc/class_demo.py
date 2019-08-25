class Rectangle():

	def __init__(self):

		width = input('Enter width (inches): ')
		height = input('Enter height (inches): ')

		self.width = int(width)
		self.height = int(height)

	def get_size(self):

		print('Width: {}  Height: {}'.format(self.width, self.height))

	def area(self):

		print('Area is: {}'.format(self.width * self.height))

class Square(Rectangle):

	def __init__(self):

		side = input('Enter length of a side: ')

		self.width = int(side)
		self.height = self.width


r = Rectangle()
s = Square()

r.area()
s.area()