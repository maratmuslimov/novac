# -*- coding: utf-8 -*-

import zmq
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)
for request in range (1):
    print("Sending request ", request,"...")
    socket.send_string('25; 15; 11; 123; 67; 234, 13, 234')
    #  Get the reply.
    message = socket.recv_string()
    print("Result of calculation [ ", message, " ] ")
