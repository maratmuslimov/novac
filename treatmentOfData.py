# -*- coding: UTF-8 -*-
""" Module Treatment of data """
import Method

def MethodChoice(Dict):
    if Dict['calcObject'] == 'EG':
        print('EG')
        result = Method.EG().calc(Dict)
        return(result)
    if Dict['calcObject'] == EMG:
        print('EMG')
        Result = Method.EMG().calc(Dict)
    if Dict['calcObject'] == EHIL:
        print('EHIL')
        Result = Method.EHIL().calc(Dict)
    if Dict['calcObject'] == ELG:
        print('ELG')
        Result = Method.ELG().calc(Dict)
    if Dict['calcObject'] == EFD:
        print('EFD')
        Result = Method.EFD().calc(Dict)
    if Dict['calcObject'] == EFM:
        print('EFM')
        Result = Method.EFM().calc(Dict)
    if Dict['calcObject'] == BG:
        print('BG')
        Result = Method.BG().calc(Dict)
    if Dict['calcObject'] == BMG:
        print('BMG')
        Result = Method.BMG().calc(Dict)
    if Dict['calcObject'] == BHIL:
        print('BHIL')
        Result = Method.BHIL().calc(Dict)
    if Dict['calcObject'] == BMHIL:
        print('BMHIL')
        Result = Method.BMHIL().calc(Dict)
    if Dict['calcObject'] == BFD:
        print('BFD')
        Result = Method.BFD().calc(Dict)
    if Dict['calcObject'] == BFM:
        print('BFM')
        Result = Method.BFM().calc(Dict)
    return(Result)

if __name__ == '__main__':
    D = {'q': 1.5, 'T': 120.0, 'V_ap': 5.0, 'P_2': 50.0, 'P_1': 50.0, 't_r': 50.0, 'M': 7.0, 'Q_sg': 40.0, 'Z': 0.1, 'r': 30.0, 'calcObject': 'EG'}

    calcData = MethodChoice(D)
