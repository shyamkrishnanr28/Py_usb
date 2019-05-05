import sched, time

s = sched.scheduler(time.time, time.sleep)
t = time.time()

def timed_event(a='1'):
    global t
    print(time.time() - t)
    s.enter(2, 2, timed_event, argument=('10',))
    t = time.time()
	
s.enter(2, 2, timed_event, argument=('0',))
s.run()
