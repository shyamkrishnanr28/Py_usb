
#=============================== Macros ================================
# 2 Hr interval 
PUMP_ON_INTERVAL = 0.1 #60*60*2
# For 1 Minute
PUMP_ON_TIME = 0.5 #60*1


#======================== Global variables =============================
import sched, time
import datetime
from gpiozero import LED


#======================== Global variables =============================
SchedCnt=0


# =========================== pump_on ==================================
def pump_on(a='0'):

    # Turn on pump
    led.off()
    global SchedCnt
    SchedCnt+=1
    print"=================== \npump_on :", SchedCnt

    # Write last pump on time to file
    file = open("watering_log.txt","w")
    file.write(str(datetime.datetime.now()))
    file.close()

    # configure the stop time 
    s.enter(PUMP_ON_TIME, 1, pump_off, argument=('0'))


# =========================== pump_off ==================================
def pump_off(a='0'):
    # Turn off pump
    led.on()
    print("pump_off")
    
    # configure the next on time
    s.enter(PUMP_ON_INTERVAL, 1, pump_on, argument=('0'))


# =========================== main.py ==================================

""" Read watering_log.txt and decide when to shcedule next pump_on()
    This is needed to handle auto script restarting feature 
"""

# GPIO init
led = LED(3)

s = sched.scheduler(time.time, time.sleep)
s.enter(PUMP_ON_INTERVAL, 1, pump_on, argument=('0'))
s.run()
