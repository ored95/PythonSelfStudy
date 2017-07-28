# Starting a new Thread
# -------------------------------------------------------------------------------
# To spawn another thread, you need to call following method available
# in thread module:
#       thread.start_new_thread ( function, args[, kwargs] )
#
# This method call enables a fast and efficient way to create new threads in both
# Linux and Windows.
#
# The method call returns immediately and the child thread starts and calls function
# with the passed list of agrs. When function returns, the thread terminates.
#
# Here, args is a tuple of arguments; use an empty tuple to call function without passing
# any arguments. kwargs is an optional dictionary of keyword arguments.
#
import thread
import time

# Define a functon for thread
def print_time( threadName, delay ):
    counter = 0
    while counter < 5:
        time.sleep( delay )
        counter += 1
        print("%s: %s" % (threadName, time.ctime( time.time() )))

# Create two threads as follows
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print("Error: unable to start thread")
while 1:
    pass

"to be continue..."
