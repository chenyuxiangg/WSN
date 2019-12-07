class message:
	def __init__(self, seq, msg, src, hopcount, sendcount):
		self.m_id = seq;
		self.m_msg = msg;
		self.m_src = src;
		self.m_hopcount = hopcount;
		self.m_sendnums = sendcount;
