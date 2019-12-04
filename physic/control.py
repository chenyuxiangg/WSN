import math;
import random;
import threading;

class control:
	__nodelist = [];
	__threadlist = [];
	
	def __init__(self):
		pass
	
	def addnode(self, node):
		self.__nodelist.append(node);
		
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
				
			distance = math.sqrt(math.pow((pos[0] - des_pos[0]),2) - math.pow((pos[1] - des_pos[1]),2));
			if distance > radius:
				continue;
				
			# 求出通信成功率
			t = 1- (distance / (radius * node.m_radius));
			# 模拟通信成功
			tflag = 100 * t;
			flag = random.choice(range(100));
			if flag <= tflag:
				t = threading.Thread(target=wake, args=(self, node, msg));
				self.__threadlist.append(t);
				t.start();
				
		for t in self.__threadlist:
			t.join();
				
	def wake(self, node, msg):
		node.recv(msg);
		msg.m_hopcount--;
		node.send(msg);
