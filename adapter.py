class endUser:

	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone

	def getName(self):
		pass

	def getEmail(self):
		pass

	def phone(self):
		pass



class Student(NYUPushover):

	def __init__(self, endUser):
		self.endUser = endUser

	def createStudent(self):
		self.endUser.name()
		self.endUser.email()
		self.endUser.phone()




class NYUPushover:

	def createStudent(self):
		pass







