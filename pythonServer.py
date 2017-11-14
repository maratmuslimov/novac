# -*- coding: utf-8 -*-

import zmq
import time
import sys
import CalculationBlock

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    V = CalculationBlock.ListMaker()
    List = V.CreateList(message)
    VolumeData = CalculationBlock.VolumeOfCrash()

    DictVD = VolumeData.makeDictVolumeData(List)
    DictCVD = VolumeData.CalculateVolumeOfCrash(DictVD)
    textResultCVD = VolumeData.TextFormerData(DictCVD)

    print("Received request: ", message)
    # time.sleep (1)
    socket.send_string(textResultCVD)
