# File: Subscriber.py
#
# brief: code to receive messages from the Publisher.
#
# Description:
# This code receives the message we are sending from the publisher using
# Zero MQ and prints the message.
#
# author: Sudeep Kumar
# date: 21/03/2021

import zmq, sys, pickle, time

#initializing a ZMQ context
context=zmq.Context()
#set the context as a subscriber
socket=context.socket(zmq.SUB)
#connecting to the IP address of the publisher
socket.connect('tcp://127.0.1.1:8081')
socket.setsockopt(zmq.SUBSCRIBE,b'')

try:
    while True:
        #start receiving the messages
        message = socket.recv()
        #decoding the message from UTF-8 format
        decoded_message=pickle.loads(message)
        #printing the message
        print(decoded_message)
except KeyboardInterrupt:
    #stopping when interuppted
    print("Interrupt received, stopping.")
finally:
    socket.close()
    context.term()
