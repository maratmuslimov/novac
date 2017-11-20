#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
""" Module of Methods """
import sys
import math

import locale
import codecs
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='UTF-8', buffering=1)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
def getpreferredencoding(do_setlocale = True):
    return "utf-8"
locale.getpreferredencoding = getpreferredencoding
print(sys.getdefaultencoding())
print(locale.getpreferredencoding())
print(sys.stdout.encoding)

# Общие для каждого объекта методы.
class CommonMethods():
	def calcVolume(self, dataDict):
		BD = dataDict
		V_a = round(0.01 * BD['P_1'] * BD['V_ap'], 3)
		V_1t = round(BD['q'] * BD['T'], 3)
		V_2t = 1
		i = 0
		# while i < len(BD['dL']):
		#     V_2t = round(V_2t + BD['dL'][i+1] * ((BD['dL'][i]/2) ** 2), 3)
		#     i += 2
		V_2t = 0.01 * BD['P_2'] * 3.14 * V_2t
		V_t = V_1t + V_2t
		V_av = V_a + V_t
		VolumeOfCrash = dict(zip(['V_a', 'V_1t', 'V_2t', 'V_t', 'V_av'], [V_a, V_1t, V_2t, V_t, V_av]))
		return(VolumeOfCrash)

	def calcPressureForEquipment(self, dataDict, m):
		BD = dataDict
		m_pr = round(BD['Q_sg'] / 4.52 * m * BD['Z'], 3)
		P_vzr = round(101 * (0.8 * (m_pr)**0.33 / (BD['r']) + 3 * (m_pr)**0.66 / (BD['r']) ** 2 + 5 * m_pr / (BD['r'])**3), 3)
		i = round(123 * (m_pr)**0.66 / BD['r'], 3)
		result = dict(zip(['m_pr', 'P_vzr', 'i' ], [m_pr, P_vzr, i]))
		return (result)

	def calcRforHIL(self, dataDict, m, p):
		BD = dataDict
		R_nkpr = round(3.1501 * (BD['T_isp'] / 3600)**0.5 * (BD['P_n'] / BD['C_nkpr'])**0.813 * (m /(p * BD['P_n']))**0.333, 3)
		return(R_nkpr)

	def calcRforG(self, dataDict, m, p):
		BD = dataDict
		R_nkpr = round(14.5632 * (m /(p * BD['C_nkpr']))**0.333, 3)
		return(R_nkpr)

	def calcDensity(self, dataDict):
		BD = dataDict
		p = round(BD['M'] /(22.413 * (1 + 0.00367 * BD['t_r'])), 3)
		return(p)
# mass calculate
	def calcMass(self, p, V):
		m = round(p * V, 3)
		return(m)

	def calcMassForHIL(self, dataDict, V_av, eta, P_n):
		BD = dataDict
		if BD['F'] == 0:
			F = V_av * 1000 * BD['k']
		else:
			F = BD['F']
		if BD['W'] == 0:
			W = eta * (BD['M'])**0.5 * P_n # В степени 10^6
		else:
			W = BD['W']
		m = W * F * BD['T_isp']
		return(m)

	def calcOverHeatMass(self, dataDict, m):
		BD = dataDict
		m_per = min(0.8 * m, 2 * BD['C_p'] * (BD['T_j'] - BD['T_kip']) * m / BD['L_isp'])
		return(m_per)

	def calcMassForLG(self, dataDict):
		BD = dataDict
		alpha = BD['lambda'] / (BD['C_tv'] * BD['p_tv'])
		if BD['F'] == 0:
			F = V_av * 1000 * BD['k']
		else:
			F = BD['F']
		d = (4 * F / 3.14)**0.5
		Re = BD['U'] * d / BD['V_v']
		m_sug1 = BD['M'] / (BD['L_isp'] * BD['M']) * (BD['T_0'] - BD['T_j'])
		m_sug2 = 2 * BD['lambda_tv'] * (BD['T_isp'] / (3.14 * alpha))**0,5 + (5.1 * (Re)**0.5 * BD['lambda_v'] * BD['T_isp']) / d
		m_sug = m_sug1 * m_sug2
		result = dict(zip(['alpha', 'F', 'd', 'Re', 'm_sug'], [alpha, F, d, Re, m_sug]))
		return(result)

	def calcCatForE(self, dataDict, P_vzr, R_nkpr):
		BD = dataDict
		if P_vzr > 5 or R_nkpr > 30:
			if BD['t_vsp'] < 28:
				category = "А"
			else:
				category = "Б"
		else:
			category = "В"
		return(category)


""" КЛАСС ОБЪЕКТОВ """

class EG(CommonMethods):
	def calc(self, Dict):
		V = CommonMethods().calcVolume(Dict)
		p = CommonMethods().calcDensity(Dict)
		m = CommonMethods().calcMass(p = p, V = V['V_av'])
		R_nkpr = CommonMethods().calcRforG(dataDict = Dict, m = m, p = p)
		P = CommonMethods().calcPressureForEquipment(dataDict = Dict, m = m)
		cat = CommonMethods().calcCatForE(dataDict = Dict, P_vzr = P['P_vzr'], R_nkpr = R_nkpr)
		calcData = dict(zip(['p', 'm', 'R_nkpr', 'cat'], [p, m, R_nkpr, cat]))
		calcData.update(P)
		calcData.update(V)
		print(type(calcData))
		return(calcData)

class EMG(CommonMethods):
	def calc(self, Dict):
		print('work')


class EHIL(CommonMethods):
	def calc(self, Dict):
		print('work')

class ELG(CommonMethods):
	def calc(self, Dict):
		print('work')

class EFD(CommonMethods):
	def calc(self, Dict):
		print('work')

class EFM(CommonMethods):
	def calc(self, Dict):
		print('work')

class BG(CommonMethods):
	def calc(self, Dict):
		print('work')

class BMG(CommonMethods):
	def calc(self, Dict):
		print('work')

class BHIL(CommonMethods):
	def calc(self, Dict):
		print('work')

class BMHIL(CommonMethods):
	def calc(self, Dict):
		print('work')

class BFD(CommonMethods):
	def calc(self, Dict):
		print('work')

class BFM(CommonMethods):
	def calc(self, Dict):
		print('work')
if __name__ == '__main__':
	D = {'C_nkpr': 16, 't_vsp': 16, 'q': 1.5, 'T': 120.0, 'V_ap': 5.0, 'P_2': 50.0, 'P_1': 50.0, 't_r': 50.0, 'M': 7.0, 'Q_sg': 40.0, 'Z': 0.1, 'r': 30.0, 'calcObject': 'EG'}
	R = EG().calc(D)
	print(R)
