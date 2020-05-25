from oop_assignment_001.car import Car
class Truck(Car):
	sound = 'Honk Honk'
	def __init__(self,color='',max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
		self._max_cargo_weight = max_cargo_weight
		self._applyload = 0
		Car.__init__(self,color,max_speed,acceleration,tyre_friction)
	def sound_horn(self):
		if self._is_engine_started == True:
			print(Truck.sound)
		else:
			print('Start the engine to sound_horn')
	def load(self,cargo_weight):
		if cargo_weight < 0:
			raise ValueError('Invalid value for cargo_weight')
		if self._applyload+cargo_weight >= self._max_cargo_weight:
			print('Cannot load cargo more than max limit: {}'.format(self._max_cargo_weight))
		elif self._current_speed ==0:
			self._applyload += cargo_weight
		else:
			print('Cannot load cargo during motion')
	def unload(self,cargo_weight):
		if cargo_weight < 0:
			raise ValueError('Invalid value for cargo_weight')\
	
		if self._current_speed == 0 :
			self._applyload -= cargo_weight
		else:
			print('Cannot unload cargo during motion')
	@property
	def max_cargo_weight(self):
		return self._max_cargo_weight
	@property	
	def applyload(self):
		return self._applyload



			
	
		
