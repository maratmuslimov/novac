import zerorpc
import sys, os.path
import CalculationBlock
import json

class StreamingRPC(object):
    def streaming_range(self, text):
        Dict = CalculationBlock.TextConvertor().jTextToDict(text)
        Volume = CalculationBlock.CalcVolumeOfCrash().calcVolume(Dict)
        result = CalculationBlock.TextConvertor().DictTojText(Volume)
        return(result)

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
