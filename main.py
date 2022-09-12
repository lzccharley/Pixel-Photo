#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@FileName: main.py
@Software: PyCharm
@Function: ...

@Modify Time        @Author        @Version        @Description
------------        -------        --------        ------------
2022/9/12 21:23     Zhengchen Li   1.0             None
"""
from pixcel_processing import PixelProcessing
from pixel_fusion import PixelFusion

if __name__ == "__main__":
    pp = PixelProcessing()
    pp.processing1()
    PF = PixelFusion()
    PF.rgb_fusion()
