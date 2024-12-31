#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-11 23:16'

from everybody_knows_design_patterns.ch1_observer.Observer import WaterHeater, WashingMode, DrinkingMode

class TestObserver:

    def testWaterHeater(self):
        heater = WaterHeater()
        washingObser = WashingMode()
        drinkingObser = DrinkingMode()
        heater.addObserver(washingObser)
        heater.addObserver(drinkingObser)
        heater.setTemperature(40)
        heater.setTemperature(60)
        heater.setTemperature(100)