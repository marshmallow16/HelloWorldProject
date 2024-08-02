from abc import ABC,abstractmethod

class AbstractProductA(ABC):
	@abstractmethod
	def operation_a(self):
		pass

class AbstractProductB(ABC):
	@abstractmethod
	def operation_b(self):
		pass
	

class ConcreteProductA1(AbstractProductA):
	def operation_a(self):
		return "Concrete Product A!"

class ConcreteProductA2(AbstractProductA):
	def operation_a(self):
		return "concrete product A2"

class ConcreteProductB1(AbstractProductB):
	def operation_b(self):
		return "Operation from B"

#now create abstract factory, concrete factory and then clientCode
class AbstractFactory(ABC):
	@abstractmethod
	def create_product_a(self):
		pass
	@abstractmethod
	def create_product_b(self):
		pass

class ConcreteFactory1(AbstractFactory):
	def create_product_a(self):
		return ConcreteProductA1()

	def create_product_b(self):
		return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
	def create_product_a(self):
		return ConcreteProductA2()
	def create_product_b(self):
		pass

factory = ConcreteFactory1()
factory2 = ConcreteFactory2()
product_a = factory.create_product_a()
product_a2 = factory2.create_product_a()

print(product_a.operation_a())
print(product_a2.operation_a())