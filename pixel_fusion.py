#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@FileName: pixel_fusion.py
@Software: PyCharm
@Function: ...

@Modify Time        @Author        @Version        @Description
------------        -------        --------        ------------
2022/9/11 23:26     Zhengchen Li   1.0             None
"""
import os
import cv2
import re
from scipy.spatial import cKDTree
import numpy as np
from tqdm import tqdm

TARGET_ROOT = "./targets"
PIXEL_ROOT = "./pixels"
RESULT_ROOT = "./results"
# 目标图像缩小比例
TARGET_REDUCTION = 16


class PixelFusion:
    def __init__(self, pixel_root=PIXEL_ROOT, target_root=TARGET_ROOT, result_root=RESULT_ROOT):
        """
        :param pixel_root: 拼图素材目录
        :param target_root: 目标图像目录
        :param result_root: 结果保存目录
        """
        self.pixel_root = pixel_root
        self.target_root = target_root
        self.result_root = result_root
        if not os.path.exists(self.result_root):  # 不存在保存结果的目录
            os.mkdir(self.result_root)  # 则新建该目录
        self.targets_name = os.listdir(self.target_root)
        self.pixels_name = os.listdir(self.pixel_root)
        self.pixels_detail = []
        for pixel_name in self.pixels_name:
            pixel_rgb100 = re.match(r"(\d+)_(\d+)_(\d+)_.+jpg", pixel_name)
            self.pixels_detail.append((pixel_rgb100.group(1), pixel_rgb100.group(2), pixel_rgb100.group(3)))
        self.pixels_tree = cKDTree(self.pixels_detail)  # KDTree加速寻找最相近的像素图像
        # print(self.pixels_tree.query([22249, 23341, 24678]))

    def rgb_fusion(self, reduction=TARGET_REDUCTION):
        """
        使用rgb最相近的图片来拼出目标图片
        :param reduction: 目标图像的缩放比例
        :return:
        """
        for target_name in tqdm(self.targets_name):
            target = cv2.imread(os.path.join(self.target_root, target_name))
            height = target.shape[0] // reduction
            width = target.shape[1] // reduction
            target = cv2.resize(target, (width, height))
            row = []
            for w in range(width):
                col = []
                for h in range(height):
                    target_rgb = list(map(lambda x: 100 * x, list(target[h][w])))
                    distance, pixel_num = self.pixels_tree.query(target_rgb)
                    pixel = cv2.imread(os.path.join(self.pixel_root, self.pixels_name[pixel_num]))
                    col.append(pixel)
                img = np.concatenate(col, 0)
                row.append(img)
            img = np.concatenate(row, 1)
            cv2.imwrite(os.path.join(self.result_root, target_name), img)
