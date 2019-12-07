import math;
import random;
import threading;

class control:
	def __init__(self, nodelist):
		self.__nodelist = nodelist;
		self.__threadlist = [];
		self.m_result = [];
		self.m_lock = threading.Lock();
	
	def send(self, msg):
		src_id = msg.m_src;
		src = "";
		for node in self.__nodelist:
			if node.m_id == src_id:
				src = node;
				break;
				
		radius = src.m_radius;
		pos = src.m_pos;
		for node in self.__nodelist:
			des_pos = node.m_pos;
			if pos == des_pos:
				continue;
				
			distance = math.sqrt(math.pow((pos[0] - des_pos[0]),2) + math.pow((pos[1] - des_pos[1]),2));
			#if distance > radius:
			#	continue;
				
			# success rate of communication
			t = 1- (math.pow(distance,2) / (radius * node.m_radius));
			# measure
			tflag = 100 * t;
			flag = random.choice(range(100));
			if flag <= tflag:
				t = threading.Thread(target=control.wake, args=(self, node, msg));
				self.__threadlist.append(t);
				t.start();
				
		for t in self.__threadlist:
			t.join();
				
	def wake(self, node, msg):
		node.recv(msg);
		msg.m_hopcount -= 1;
		self.m_lock.acquire();
		for n in self.m_result:
			if n == node:
				self.m_lock.release();
				return;
		self.m_result.append(node);
		self.m_lock.release();

	# for test
	def getnodelist(self):
		return self.__nodelist;
