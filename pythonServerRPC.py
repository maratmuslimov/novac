import zerorpc
import sys
import CalculationBlock

class StreamingRPC(object):
    @zerorpc.stream
    def streaming_range(self, text):
        message = text
        V = CalculationBlock.ListMaker()
        List = V.CreateList(message)
        VolumeData = CalculationBlock.VolumeOfCrash()

        DictVD = VolumeData.makeDictVolumeData(List)
        DictCVD = VolumeData.CalculateVolumeOfCrash(DictVD)
        textResultCVD = VolumeData.TextFormerData(DictCVD)
        print(textResultCVD)
        return(textResultCVD)

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
