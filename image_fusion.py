#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@FileName: image_fusion.py
@Software: PyCharm
@Function: ...

@Modify Time        @Author        @Version        @Description
------------        -------        --------        ------------
2022/9/11 23:26     Zhengchen Li   1.0             None
"""
import os
import cv2
import numpy as np

TARGET_ROOT = "./targets"
PIXEL_ROOT = "./pixels"
RESULT_ROOT = "./results"
PIXEL_BASE = 8


class PixelFusion:
    def __init__(self, pixel_root=PIXEL_ROOT, target_root=TARGET_ROOT, result_root=RESULT_ROOT):
        self.pixel_root = pixel_root
        self.target_root = target_root
        self.result_root = result_root
        if not os.path.exists(self.result_root):  # 不存在保存结果的目录
            os.mkdir(self.result_root)  # 则新建该目录
        self.targets_name = os.listdir(self.target_root)
        self.pixels_name = os.listdir(self.pixel_root)

    def fusion(self):
        for target_name in self.targets_name:
            target = cv2.imread(os.path.join(self.target_root, target_name))
            height = target.shape[0] // PIXEL_BASE
            width = target.shape[1] // PIXEL_BASE
            target = cv2.resize(target, (width, height))
            cv2.imshow('1', target)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
            # target = cv2.resize(target, target.)


PF = PixelFusion()
PF.fusion()
