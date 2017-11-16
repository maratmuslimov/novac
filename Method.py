# -*- coding: UTF-8 -*-
""" Module of Methods """
import sys
print('calcObject')


# Общие для каждого объекта методы.
class CommonMethods():
    def calcVolume(self, VolumeBaseData):
        BD = VolumeBaseData
        V_a = round(0.01 * BD['P_1'] * BD['V_ap'], 3)
        V_1t = round(BD['q'] * BD['T'], 3)
        V_2t = 1
        i = 0
        while i < len(BD['dL']):
            V_2t = round(V_2t + BD['dL'][i+1] * ((BD['dL'][i]/2) ** 2), 3)
            i += 2
        V_2t = 0.01 * BD['P_2'] * 3.14 * V_2t
        V_t = V_1t + V_2t
        V_av = V_a + V_t
        VolumeOfCrash = dict(zip(['V_a', 'V_1t', 'V_2t', 'V_t', 'V_av'], [V_a, V_1t, V_2t, V_t, V_av]))
        print(VolumeOfCrash)
        return(VolumeOfCrash)

    # def calcPressureForEquipment(self, Dict):
