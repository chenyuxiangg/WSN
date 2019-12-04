import threading;

class A:
	def __init__(self):
		pass
		
	def run(self, x):
		print("thread: %s, arg: %d" % (threading.current_thread().name,x));
		

def start():
	threadlist = [];
	for i in range(10):
		a = A();
		t = threading.Thread(target=a.run, args=(i,));
		threadlist.append(t);
		t.start();
		
	for t in threadlist:
		t.join();
		

start();

		
