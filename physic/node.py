from cyx_util import enum_operator_type as eot;
from cyx_util import enum_operator_map as eom;
from physic import message;
import threading;
import sys;
sys.path.append("..");
from strategy.manager import default_hop;
from strategy.manager import default_send;

class node:
	'物理节点'
	def __init__(self, name, pos, radius, l, control):
		self.m_pos = pos;
		self.m_radius = radius;
		self.m_ld = l;
		self.m_id = name;
		self.__control = control;
		self.__msgqueue = [];
		self.m_msg_lock = threading.Lock();
		self.m_ld_lock = threading.Lock();

	def send(self):
		msg = "";
		self.m_msg_lock.acquire();
		if len(self.__msgqueue) != 0:
			msg = self.__msgqueue[0];
			del self.__msgqueue[0];
			msg.m_hopcount -= 1;
			msg.m_sendnums -= 1;
			if msg.m_sendnums > 0 and msg.m_hopcount > 0:
				self.__msgqueue.append(msg);
		self.m_msg_lock.release();

		if msg.m_hopcount==0:
			return;
		msg.m_src = self.m_id;
		self.__consume(eot.eot.SEND);
		self.__control.send(msg);

	def recv(self, msg):
		self.__consume(eot.eot.RECV);
		self.m_msg_lock.acquire();
		self.__msgqueue.append(msg);
		self.m_msg_lock.release();
		print("%d from %d recv a msg: %s" % (self.m_id, msg.m_src, msg.m_msg));

	def getmsgqueue(self):
		return self.__msgqueue;

	def __consume(self,enum_operator):
		self.m_ld_lock.acquire();
		if self.m_ld <= 0.0:
			print("电量不足...");
			self.m_ld_lock.release();
			exit(1);
		self.m_ld -= eom.eom[enum_operator];
		self.m_ld_lock.release();

	def start(self):
		msg = message.message("test",self.m_id,default_hop,default_send);
		self.__msgqueue.append(msg);

