class animalBaseClass:
	animallegs = 4
	def walk(self):
		print('walk')
	def cry(self):
		print('cry')

class dogClass(animalBaseClass):
	dog = 'IamDog'
	def __init__(self):
		print("I am Dog")

class animalClass:
	def __init__(self, num):
		self.animallegs = num
		print(self.animallegs)

	def walk(self):
		print('walk')
	
	def cry(self):
		print('cry')

	def getLegsNum(self):
		print(self.animallegs)

class snakeClass(animalClass):
	def __init__(self, num):
		parant_class = super(snakeClass, self)#자식클래스 이름, 인스턴스
		parant_class.__init__(num)
		print('snake')

