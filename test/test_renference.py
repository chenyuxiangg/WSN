class A:
	m_nodelist = [];

	def __init__(self, nodelist):
		m_nodelist = nodelist;

nodelist = [];
a = A(nodelist);
nodelist.append(1);
print("A.nodelist:");
print(A.m_nodelist);
print("a.nodelist:");
print(a.m_nodelist);
