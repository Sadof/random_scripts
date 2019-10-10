class Person:

	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	@property	
	def age(self):
		return self.__age

	@age.setter	
	def age(self,age):
		if age:
			self.__age = age
		else:
			print("You are trying to set incorrect age")


	@property		
	def name(self):
		return self.__name

	def __str__(self):
		return ("Name: {}, age: {}".format(self.__name,self.__age))




class Employee(Person):

	def __init__(self,name,age,company):
		Person.__init__(self,name,age)
		self.__company = company

	@property
	def company(self):
		return self._company

	@company.setter
	def company(self, company_name):
		self.__company = company_name

	def __str__(self):
		return ("Name: {}, age: {}, working at: {}".format(self.name,self.age,self.__company))

class Student(Person):

	def __init__(self,name,age,university):
		super().__init__(name,age)
		self.__university = university

	@property
	def university(self):
		return self.__university
	
	@university.setter
	def university(self,name):
		# condition like name in [university_name_arr]
		self.__university = name

	def __str__(self):
		return super().__str__() + (" studying at: {}".format(self.__university))

	#def __str__(self):
	#	return ("{},{},{}". format(self.name,self.age,self.__university))


#	print("Person part <!--")
#	person1 = Person("Max",23)
#	print(person1.age)
#	person1.age = 33
#	print(person1.age)
#	print(person1)
#	print("--!> person part end")

#	worker = Employee("Tema",28,"idk")
#	print(worker)
#	worker.age = 30
#	worker.company = "smth"
#	print(worker)

student = Student("Olya",22,"banking")
print(student)
student.age = 30
print(dir(student))
student.university = "economic"
print(student)

	

