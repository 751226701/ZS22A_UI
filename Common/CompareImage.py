#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/16 11:02
# @file: CompareImage
# @project: ZS22A_UI

import cv2
import requests
import numpy as np


def compare_images(image_path1, image_path2):
    """
    比较两张图片是否相同
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :return:
    """
    # 读取图像
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # print(image1.shape)
    # print(image2.shape)

    # 比较图像
    difference = cv2.subtract(image1, image2)
    result = not np.any(difference)

    return result


def are_images_equal(image_path1, image_path2):
    """
    比较两张图片是否相同
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :return:
    """
    return compare_images(image_path1, image_path2)


def download_image(url, save_path):
    """
    下载图片到指定路径
    :param image_url: 图片链接地址
    :param save_path: 保存路径
    :return:
    """
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    image_path_actual = r'D:\APP\pycharm\project\ZS22A_UI\TestFiles\ACTUAL_LOGO.png'
    image_path_expected = r'D:\APP\pycharm\project\ZS22A_UI\TestFiles\EXPECT_LOGO.png'
    if are_images_equal(image_path_actual, image_path_expected):
        print("图像相同")
    else:
        print("图像不同")




