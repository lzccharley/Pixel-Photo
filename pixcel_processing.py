#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@FileName: pixcel_processing.py
@Software: PyCharm
@Function: ...

@Modify Time        @Author        @Version        @Description
------------        -------        --------        ------------
2022/9/11 22:31     Zhengchen Li   1.0             None
"""

import os
import shutil
import cv2
import numpy as np

IMG_ROOT = "./original_images"
PIXEL_ROOT = "./pixels"
PIXEL_BASE = 128

class PixelProcessing:
    def __init__(self, img_root=IMG_ROOT, pixel_root=PIXEL_ROOT, is_clear=True):
        self.IMG_ROOT = img_root
        self.Pixel_ROOT = pixel_root
        if not os.path.exists(self.Pixel_ROOT):  # 不存在像素目录
            os.mkdir(self.Pixel_ROOT)  # 则新建该目录
        elif is_clear:  # 存在该目录且需要清空
            shutil.rmtree(self.Pixel_ROOT)  # 则删除文件夹和附属内容
            os.mkdir(self.Pixel_ROOT)  # 则新建该目录
        self.imgs_name = os.listdir(self.IMG_ROOT)

    def processing1(self, size=(PIXEL_BASE, PIXEL_BASE)):
        for img_name in self.imgs_name:
            img = cv2.imread(os.path.join(self.IMG_ROOT, img_name))
            img = cv2.resize(img, size)
            average_rgb = [int(np.mean(img[:, :, i]) * 100) for i in range(3)]  # 计算图像的平均RGB
            average_rgb = list(map(str, average_rgb))
            new_img_name = '_'.join(average_rgb) + '_' + img_name
            cv2.imwrite(os.path.join(self.Pixel_ROOT, new_img_name), img)


pp = PixelProcessing()
pp.processing1()
