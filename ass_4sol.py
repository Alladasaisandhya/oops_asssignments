import math
class ComplexNumber:
	def __init__(self,real_part=0,imaginary_part=0):
		
		if type(real_part) is str and type(imaginary_part) is str:
			raise ValueError('Invalid value for real and imaginary part')
		if type(real_part) is str:
			raise ValueError('Invalid value for real part')
		else:
			self.real_part = real_part
		
		if type(imaginary_part) is str:
			raise ValueError('Invalid value for imaginary part')
		else:
			self.imaginary_part = imaginary_part
		
		
	def __str__(self):
		return f'{self.real_part}{self.imaginary_part:+}i'
	
	def conjugate(self):
		return ComplexNumber(self.real_part,-self.imaginary_part)
	def __add__(self,other):
		return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
	def __sub__(self,other):
		return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
	def __mul__(self,other):
		return ComplexNumber(self.real_part*other.real_part-self.imaginary_part*other.imaginary_part,self.imaginary_part*other.real_part+other.imaginary_part*self.real_part)
	
	def __truediv__(self,other):
		num1,den1,num2,den2 = self.real_part,self.imaginary_part,other.real_part,other.imaginary_part
		d = float(num2**2 + den2**2)
		return ComplexNumber((num1*num2 + den1*den2)/d,(den1*num2-num1*den2)/d)
		
	'''def __truediv__(self, other):
		sr, si, orr, oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part # short forms
		r = float(orr**2 + oi**2)
		return ComplexNumber((sr*orr+si*oi)/r, (si*orr-sr*oi)/r)'''
		
	def __abs__(self):
		return round(math.sqrt(self.real_part**2+self.imaginary_part**2),3)
		
	def __eq__(self,other):
		if self.real_part == other.real_part and self.imaginary_part == other.imaginary_part:
			return True
		else:
			return False
	
    


