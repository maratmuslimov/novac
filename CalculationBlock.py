# -*- coding: UTF-8 -*-
""" This block contain classes for calculate volume of crash, mass of crash, explosion pressure and catigory
Class MakeDictVolumeData"""

import sys, math, os.path

class VolumeOfCrash():
    def makeDictVolumeData(self, VolumeData):
        if len(VolumeData) == 6:
            VolumeDataDict = dict(zip(['P1', 'V', 'q', 'T', 'P2', 'rL'], VolumeData))
        else:
            VolumeDataDict = {'ERROR: ': "BASE DATA PATTERN DON'T MATCH"}
        return(VolumeDataDict)
    def CalculateVolumeOfCrash(self, VolumeDataDict):
        if len(VolumeDataDict) == 6 and type(VolumeDataDict) == dict:
            for key in VolumeDataDict:
                if type(VolumeDataDict[key]) == list:
                    ListPart = []
                    for elem in VolumeDataDict[key]:
                        elem = elem * 2
                        ListPart.append(elem)
                    VolumeDataDict[key] = ListPart
                else:
                    VolumeDataDict[key] = VolumeDataDict[key] * 2
        return(VolumeDataDict)
    def TextFormerData(self, VolumeDataDict):
        message = ''
        if len(VolumeDataDict) == 1:
            message = "BASE DATA PATTERN DON'T MATCH"
        else:
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
    # List = V.CreateList('2435; 345; 7; 345')
    # List = V.CreateList('123; a; 234, 13, 234; 23, 67, 87')
    # List = V.CreateList('123; a; 234, 13, 234; 165; 23, 67, 87')
    # List = V.CreateList('23; 15; 11; 12; 67; 234, 13, 234')
    VolumeData = VolumeOfCrash()
    DictVD = VolumeData.makeDictVolumeData(List)
    DictCVD = VolumeData.CalculateVolumeOfCrash(DictVD)
    textResultCVD = VolumeData.TextFormerData(DictCVD)
