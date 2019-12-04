class message:
	m_msg = "";
	m_src = "";
	__hopcount = 0;

	def __init__(self, msg, src, hopcount):
		self.m_msg = msg;
		self.m_src = src;
		self.__hopcount = hopcount;

	def gethopcount(self):
		return self.__hopcount;

	def reducecount(self):
		--self.__hopcount;
