import thread
import time
def five(stuff):
    time.sleep(stuff)
    print "5 sec have passed %s" % stuff
def one(stuff):
    time.sleep(1)
    print "\n one second has passed %s" % stuff
	
def two():
	time.sleep(2)
	print "\n 2 seconds have passed"
	
thread.start_new_thread(five, ('1',))
thread.start_new_thread(one, ('2',))
thread.start_new_thread(two, ())

time.sleep(0.1)
raw_input('?')
	
