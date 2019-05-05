import sched, time

s = sched.scheduler(time.time, time.sleep)
t = 0

def print_time(a='1'):
    global t
    print(time.time() - t)
    s.enter(4, 2, print_time, argument=('10',))
    t = time.time()
	
def print_some_times():
    s.enter(4, 2, print_time, argument=('0',))
    s.run()
	
print_some_times()
