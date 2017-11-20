import zerorpc
import os.path
import treatmentOfData
# import json

class StreamingRPC(object):
    def streaming_range(self, text):
        Dict = treatmentOfData.TextConvertor().jTextToDict(text)
        calcData = treatmentOfData.MethodChoice(Dict)
        result = treatmentOfData.TextConvertor().DictTojText(calcData)
        print(result)
        return(result)

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
