from strategy.enum_strategy import enum_strategy as es;

default_hop = 10;
default_send = 5;

class manager:
	def __init__(self, nodelist, strategy = es.ST_NORMAL):
		self.__strategy = strategy;

	def setstrategy(self, enum_strategy):
		self.__strategy = enum_strategy;
	
	def adjuststrategy(self):
		if self.__strategy == es.ST_NORMAL:
			return;
		if self.__strategy == es.ST_ADVANCE:
			return;
		if self.__strategy == es.ST_HIGH:
			return;
		else:
			return;
