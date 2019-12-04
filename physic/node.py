from cyx_util import enum_operator_type as eot;
from cyx_util import enum_operator_map as eom;

class node:
	'物理节点'
	m_pos = (0.0,0.0);
	m_radius = 0.0;
	m_sendnums = 0.0;
	m_ld = 0.0;
	m_singleconsu = 0.0;
	__control = 0;

	def __init__(self, pos, radius, sendnums, ld, singleconsu, control):
		self.m_pos = pos;
		self.m_radius = radius;
		self.m_sendnums = sendnums;
		self.m_ld = ld;
		self.m_singleconsu = singleconsu;
		__control = control;

	def send(self, msg):
		self.__consume(eot.eot.SEND);
		self.__control.send(msg);

	def recv(self, org, msg):
		self.__consume(eot.eot.RECV);
		print("from %s recv a msg: %s" % (org, msg));

	def __consume(enum_operator):
		if m_ld <= 0.0:
			print("电量不足...");
			exit(1);
		m_ld -= eom.eom[enum_operator];

