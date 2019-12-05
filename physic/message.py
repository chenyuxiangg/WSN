class message:
	def __init__(self, msg, src, hopcount, sendcount):
		self.m_msg = msg;
		self.m_src = src;
		self.m_hopcount = hopcount;
		self.m_sendnums = sendcount;
