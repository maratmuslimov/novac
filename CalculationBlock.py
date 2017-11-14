# -*- coding: UTF-8 -*-
""" This block contain classes for calculate volume of crash, mass of crash, explosion pressure and catigory
Class MakeDictVolumeData"""

import sys, math, os.path

class VolumeOfCrash():
    def makeDictVolumeData(self, VolumeData):
        if len(VolumeData) == 6:
            VolumeDataDict = dict(zip(['P1', 'V', 'q', 'T', 'P2', 'rL'], VolumeData))
        else:
            print('Base Data Error')
            VolumeDataDict = {'P1': 50.0, 'V': 30.0, 'q': 22.0, 'T': 246.0, 'P2': 134.0, 'rL': [468.0, 26.0, 468.0]}
        return(VolumeDataDict)
    def CalculateVolumeOfCrash(self, VolumeDataDict):
        print(type(VolumeDataDict))
        for key in VolumeDataDict:
            if type(VolumeDataDict[key]) == list:
                ListPart = []
                for elem in VolumeDataDict[key]:
                    elem = elem * 2
                    ListPart.append(elem)
                VolumeDataDict[key] = ListPart
            else:
                VolumeDataDict[key] = VolumeDataDict[key] * 2
        print(VolumeDataDict)
        return(VolumeDataDict)
    def TextFormerData(self, VolumeDataDict):
        message = ''
        for key in VolumeDataDict:
            message = message + str(key) + ' = ' + str(VolumeDataDict[key]) + '; '
        return(message)

class ListMaker():
    def CreateList(self, text):
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
        return (FinalList)

if __name__ == '__main__':
    V = ListMaker()
    # List = V.CreateList('123; a; 234, 13, 234; 165; 23, 67, 87')
    List = V.CreateList('23; 15; 11; 123; 67; 234, 13, 234')
    VolumeData = VolumeOfCrash()
    DictVD = VolumeData.makeDictVolumeData(List)
    DictCVD = VolumeData.CalculateVolumeOfCrash(DictVD)
    textResultCVD = VolumeData.TextFormerData(DictCVD)
