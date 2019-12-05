import numpy as np;
from numpy.linalg import cholesky;
import random;
import sys;
import math;
sys.path.append("..");

from physic import node;
from physic import message;
from physic import control;
from strategy import manager;
from strategy.enum_strategy import enum_strategy as es;

# 生成sampleNo个节点的半径
mu = random.randint(1, 9);
sigma = random.randint(0, 4);
sampleNo = 110;
rs = np.random.normal(mu,sigma,sampleNo);
# 绝对化
for i in range(len(rs)):
	if rs[i] < 0:
		rs[i] = math.fabs(rs[i]);

# 生成sampleNo个节点的坐标
xlist = np.random.randint(low=0,high=100,size=sampleNo);
ylist = np.random.randint(low=0,high=100,size=sampleNo);

# 生成sampleNo个节点
nodelist = [];
contr = control.control(nodelist);
for i in range(sampleNo):
	n = node.node(i,(xlist[i],ylist[i]),rs[i],100000000,contr);
	print("pos:(%d,%d), r: %f" % (n.m_pos[0],n.m_pos[1],n.m_radius));
	nodelist.append(n);

# 生成管理器
manager = manager.manager(nodelist);
manager.setstrategy(es.ST_NORMAL);
manager.adjuststrategy();

# 开始模拟
#i = random.randint(0,sampleNo-1);
#nodelist[i].start();
#index = 0;
#pre_index = index;
#flag = True;
#while flag:
#	if len(nodelist[index].getmsgqueue()) != 0:
#		nodelist[index].send();
#		pre_index = index-1;
#	index = (index+1)%sampleNo;
#	if index == pre_index:
#		if len(nodelist[index+1].getmsgqueue()) == 0:
#			flag = False;
#	if pre_index < 0:
#		if len(nodelist[0].getmsgqueue()) == 0:
#			flag = False;
	
