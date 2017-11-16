# -*- coding: UTF-8 -*-
""" This block contain classes for calculate volume of crash, mass of crash, explosion pressure and catigory
Class MakeDictVolumeData"""
import sys, math, json

class TextConvertor():
    def TextToDict(self, text):
        exec('Dict = ' + text)
        return(Dict)
    def DictTojText(self, Dict):
        text = json.dumps(Dict)
        return(text)
    def jTextToDict(self, text):
        Dict = json.loads(text)
        return(Dict)
    def CreateList(self, text):
        try:
            text = text.split("; ")
            List = list(text)
            FinalList = []
            for value in List:
                try:
                    value = float(value)
                except ValueError:
                    value = value.split(",")
                    sublist = list(value)
                    SubList = []
                    for val in sublist:
                        try:
                            val = float(val)
                            SubList.append(val)
                        except ValueError:
                            print('ERROR!! STR TYPE IN DATA')
                            SubList = None
                    value = SubList
                FinalList.append(value)
        except SyntaxError:
            FinalList = 'Text fails to meet the requirements\nTaken argument must be string\nExample: 1; 2; 3; 4, 5, 6\nResult: [12.0, 32.0, 54.0, [4.0, 5.0, 7.0]]'
        except AttributeError:
            FinalList = 'Text fails to meet the requirements\nTaken argument must be string\nExample: 1; 2; 3; 4, 5, 6\nResult: [12.0, 32.0, 54.0, [4.0, 5.0, 7.0]]'
        print (FinalList)
        return (FinalList)

class CalcVolumeOfCrash():
    def calcVolume(self, VolumeBaseData):
        BD = VolumeBaseData
        V_a = round(0.01 * BD['P_1'] * BD['V_ap'], 3)
        V_1t = round(BD['q'] * BD['T'], 3)
        V_2t = 1
        # i = 0
        # while i < len(BD['dL']):
        #     V_2t = round(V_2t + BD['dL'][i+1] * ((BD['dL'][i]/2) ** 2), 3)
        #     i += 2
        V_2t = 0.01 * BD['P_2'] * 3.14 * V_2t
        V_t = V_1t + V_2t
        V_av = V_a + V_t
        VolumeOfCrash = dict(zip(['V_a', 'V_1t', 'V_2t', 'V_t', 'V_av'], [V_a, V_1t, V_2t, V_t, V_av]))
        print(VolumeOfCrash)
        return(VolumeOfCrash)

if __name__ == '__main__':
    t = '{"P_1": 50.0, "V_ap": 5.0, "q": 1.5, "T": 120.0, "P_2": 50.0, "dL": [0.024, 6.0, 0.024, 6.0]}'
    Dict = TextConvertor().jTextToDict(t)
    Volume = CalcVolumeOfCrash().calcVolume(Dict)
