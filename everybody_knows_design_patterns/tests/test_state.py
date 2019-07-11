#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-11 23:17'


"""
cd ~/Python3Demo/everybody_knows_design_patterns

pytest --cov=./
pytest --cov=./ --cov-report=html

不明原因，要使用python -m pytest

run in terminal:
python -m pytest --cov=./

usage:

python -m pytest --cov=./  --cov-config ./tests/.coveragerc

# display print()
python -m pytest --cov=./  --cov-config ./tests/.coveragerc -s

# output report
python -m pytest --cov=./  --cov-config ./tests/.coveragerc --cov-report=html

"""
from everybody_knows_design_patterns.ch2_state.story_water import Wather, LiquidState, SolidState, GaseousState

class TestState:

    def test_liquid_state(self):
        water = Wather(LiquidState("液态"))
        water.behavior()
        water.setTemperature(-4)
        water.behavior()
        water.riseTemperature(18)
        water.behavior()
        water.riseTemperature(110)
        water.behavior()

    def test_solid_state(self):
        water = Wather(SolidState("固态"))
        water.behavior()

    def test_gaseous_state(self):
        water = Wather(GaseousState("气态"))
        water.behavior()