import matplotlib;
import matplotlib.pyplot as plt;
import matplotlib.animation as animation;
import numpy as np;

class visual:
	def __init__(self, control):
		self.__control = control;
		self.fig, self.ax = plt.subplots();
		tmp = [];
		for i in range(len(control.getnodelist())+1):
			tmp.append(50);
		self.col = np.array(tmp);

		self.ani = animation.FuncAnimation(self.fig,self.update_dot,frames=self.gen_dot,interval=100,init_func=self.init);

	def init(self):
		self.ax.set_xlim(0,100);
		self.ax.set_ylim(0,100);
		x = [];
		y = [];
		for node in self.__control.getnodelist():
			x.append(node.m_pos[0]);
			y.append(node.m_pos[1]);
		self.scat = self.ax.scatter(x,y,s=25,c='b');
		return self.scat,;

	def gen_dot(self):
		for node in self.__control.m_result:
			yield node;

	def update_dot(self,node):
		index = node.m_id;
		self.col[index] = 60;
		self.scat.set_array(self.col);
		return self.scat,;

def vplay(control):
	matplotlib.use('TkAgg');
	vis = visual(control);
	plt.show();
