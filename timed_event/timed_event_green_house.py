# 2 Hr interval 
PUMP_ON_INTERVAL = 60*60*2
# For 1 Minute
PUMP_ON_TIME = 60*1

SchedCnt=0

import sched, time
s = sched.scheduler(time.time, time.sleep)

def pump_on(a='0'):
	# Turn on GPIO
    global SchedCnt
    SchedCnt+=1
    print"=================== \npump_on :", SchedCnt
    s.enter(PUMP_ON_TIME, 1, pump_off, argument=('0',))

def pump_off(a='0'):
    print("pump_off")
	# Turn off GPIO
    s.enter(PUMP_ON_INTERVAL, 1, pump_on, argument=('0',))
	
s.enter(PUMP_ON_INTERVAL, 1, pump_on, argument=('0',))
s.run()
