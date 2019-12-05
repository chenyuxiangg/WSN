class A:
	x = 0;
	def __init__(self):
		pass

	@staticmethod
	def func():
		x = 9;

	def getx(self):
		return self.x;

a = A();
A.func();
print(a.getx());
