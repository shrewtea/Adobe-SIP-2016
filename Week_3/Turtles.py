class turtles():
	def __init__(self, color, shell_pattern, neck_size, species):
		self.color=color
		self.shell_pattern=shell_pattern
		self.neck_size=neck_size
		self.species=species

	def walking(speed):
		print("The "+self.color+" colored turtle moves at "+speed+" mph")
	def eating():
		print(self.species+"eats grass everyday")
	def swimming(location):
		if self.neck_size > 10:
			print("A long neck will help the "+self.species+" swim in th ocean")
		if self.neck_size < 10:
			print("A small neck will help the "+self.species+" swim in a shallow pond")

turtle1=turtles("green", "spiral", 10,"African")
turtle1.walking(10)

