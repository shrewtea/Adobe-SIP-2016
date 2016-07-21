class Dog():
	def __init__(self, furColor, weight, eyeColor, name):
		self.furColor = furColor
		self.weight = weight
		self.eyeColor = eyeColor
		self.name = name

		#function
	def bark(self):
		print("Woof")

	def wag(self):
		print("Wagging Tail")

Toto = Dog("brown", 25, "Blue", "Toto")
Toto.bark()
print("testing")