# File: Publisher.py
#
# brief: code to send messages as a Publisher.
#
# Description:
# This code sends messages we are sending as a publisher using
# Zero MQ.
#
# author: Sudeep Kumar
# date: 21/03/2021


import zmq, time, sys

#initializing a ZMQ context
context=zmq.Context();
#set the context as a publisher
socket=context.socket(zmq.PUB)
#binding to the desired IP address
socket.bind('tcp://127.0.1.1:8081')
#initializing the message
message="Hello from the server"

try:
    while True:
    	#send the message
        socket.send_pyobj(message)
        #sleeping for 1 second to prevent spamming messages
        time.sleep(1)
except KeyboardInterrupt:
	#stopping when interuppted
    print("Interrupt received, stopping.")
finally:
    socket.close()
    context.term()