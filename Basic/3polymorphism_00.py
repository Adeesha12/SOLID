class SriLanka():
	def capital(self):
		print("Colombo is the capital of Sri Lanka.")

	def language(self):
		print("Sinhala is the most widely spoken language of Sri Lanka.")

	def status(self):
		print("Sri Lanka is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def status(self):
		print("USA is a developed country.")

def func(obj):    #// this is a example for duck typing in polymorphism 
	obj.capital()
	obj.language()
	obj.status()

obj_sri = SriLanka()
obj_usa = USA()

func(obj_sri)
func(obj_usa)
