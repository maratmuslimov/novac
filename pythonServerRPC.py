import zerorpc
import sys
import CalculationBlock

class StreamingRPC(object):
    def streaming_range(self, text):
        message = text
        V = CalculationBlock.ListMaker()
        List = V.CreateList(message)
        VolumeData = CalculationBlock.VolumeOfCrash()

        DictVD = VolumeData.makeDictVolumeData(List)
        DictCVD = VolumeData.CalculateVolumeOfCrash(DictVD)
        textResultCVD = VolumeData.TextFormerData(DictCVD)
        return(textResultCVD)

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()

# import zerorpc
#
# class HelloRPC(object):
#     def hello(self, name):
#         return "Hello, %s" % name
#
# s = zerorpc.Server(HelloRPC())
# s.bind("tcp://0.0.0.0:4242")
# s.run()
