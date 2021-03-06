# -*- coding: UTF-8 -*-
""" Module Treatment of data """
import Method, json, sys

import CalculationBlock
import locale
import codecs

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
def getpreferredencoding(do_setlocale = True):
    return "utf-8"
locale.getpreferredencoding = getpreferredencoding

class TextConvertor():
	def TextToDict(self, text):
		exec('Dict = ' + text)
		return(Dict)
	def DictTojText(self, Dict):
		text = json.dumps(Dict, ensure_ascii=False)
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

def MethodChoice(Dict):
	if Dict['calcObject'] == 'EG':
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
	D = {'C_nkpr': 16, 't_vsp': 16, 'q': 1.5, 'T': 120.0, 'V_ap': 5.0, 'P_2': 50.0, 'P_1': 50.0, 't_r': 50.0, 'M': 7.0, 'Q_sg': 40.0, 'Z': 0.1, 'r': 30.0, 'calcObject': 'EG'}
	f = MethodChoice(D)
	G = TextConvertor().DictTojText(Dict = f)

	print(f)
	print(G)
