import zerorpc
import os.path
import CalculationBlock
import json
import treatmentOfData

class StreamingRPC(object):
    def streaming_range(self, text):
        Dict = CalculationBlock.TextConvertor().jTextToDict(text)
        # Volume = CalculationBlock.CalcVolumeOfCrash().calcVolume(Dict)
        calcData = treatmentOfData.MethodChoice(Dict)
        result = CalculationBlock.TextConvertor().DictTojText(calcData)
        return(result)

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
