#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/16 11:02
# @file: CompareImage
# @project: ZS22A_UI

import cv2
import requests
import numpy as np
from skimage.metrics import structural_similarity as ssim
import skimage.io
import cv2

"""比较两张照片是否相同(逐像素)"""
def compare_images(image_path1, image_path2, threshold=10):
    """
    比较两张图片是否在允许的误差范围内相同（像素级别比较，比较照片的尺寸格式需要一致）
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :param threshold: 允许的最大像素差异值，如果两张图片的像素差异在这个值以下，则认为它们是相同的
    :return: 如果在误差范围内相同返回True，否则返回False
    """
    # 读取图像
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # 确保图像尺寸一致
    if image1.shape != image2.shape:
        raise ValueError("两张照片的尺寸不一致")

    # 计算图像差异
    difference = cv2.subtract(image1, image2)
    difference = np.abs(difference)  # 取绝对值

    # 检查差异是否在阈值内
    result = np.all(difference <= threshold)

    return result

"""比较两张照片是否相同(SSIM结构相似性指数)"""
def compare_images_ssim(image_path1, image_path2, ssim_threshold=0.95, win_size=11):
    """
    :param image_path1:第一张照片路径
    :param image_path2:第二张照片路径
    :param ssim_threshold:SSIM比较的阈值，阈值越接近1，两张照片相似度越高
    :param win_size:SSIM计算中使用的窗口大小。必须是奇数，且不大于图像的较小边长。默认为11。
    :return:
    """
    # 读取图像
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        raise ValueError("文件错误！")

    # 确保图像尺寸一致且至少为7x7
    if image1.shape[0] < 7 or image1.shape[1] < 7 or image2.shape[0] < 7 or image2.shape[1] < 7:
        raise ValueError("图像的大小必须至少为7x7像素")

    # 调整win_size以确保不超过图像尺寸
    win_size = min(win_size, image1.shape[0], image1.shape[1], image2.shape[0], image2.shape[1])
    win_size = max(7, win_size)  # 确保win_size至少为7

    # 转换图像到YUV颜色空间
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2YUV)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2YUV)

    # 计算SSIM
    ssim_value = ssim(image1, image2, multichannel=True, win_size=win_size, channel_axis=2)

    # 检查SSIM是否在阈值内
    return ssim_value >= ssim_threshold

"""比较两张照片亮度"""
def compare_images_brightness(image_path1, image_path2):
    """
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :return: 1 第一张照片亮度大于第二张  2 第一张照片亮度小于第二张   3 第一张照片亮度等于第二张
    """
    # 读取图像
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # 转为灰度图
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 计算亮度
    brightness1 = np.mean(gray1)
    brightness2 = np.mean(gray2)

    # 比较亮度
    if brightness1 > brightness2:
        return 1
    elif brightness1 < brightness2:
        return 2
    else:
        return 3

"""比较两张照片对比度"""
def compare_images_contrast(image_path1, image_path2):
    """
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :return: 1 第一张照片对比度大于第二张  2 第一张照片对比度小于第二张   3 第一张照片对比度等于第二张
    """
    # 读取图片
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # 使用像素强度范围计算对比度指标
    max1, min1 = np.max(image1), np.min(image1)
    max2, min2 = np.max(image2), np.min(image2)
    contrast1 = max1 - min1
    contrast2 = max2 - min2

    # 比较对比度
    if contrast1 > contrast2:
        return 1
    elif contrast1 < contrast2:
        return 2
    else:
        return 3

"""比较两张照片锐度"""
def compare_images_sharpness(image_path1, image_path2):
    """
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :return: 1 第一张照片锐度大于第二张  2 第一张照片锐度小于第二张   3 第一张照片锐度等于第二张
    """
    # 读取图片
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # 计算拉普拉斯算子
    laplacian1 = cv2.Laplacian(image1, cv2.CV_64F)
    laplacian2 = cv2.Laplacian(image2, cv2.CV_64F)

    # 计算方差
    variance1 = np.var(laplacian1)
    variance2 = np.var(laplacian2)

    if variance1 > variance2:
        return 1
    elif variance1 < variance2:
        return 2
    else:
        return 3

"""比较两张照片细节强度"""
def compare_images_detail(image_path1, image_path2):
    """
    :param image_path1: 第一张照片路径
    :param image_path2: 第二张照片路径
    :return: 1 第一张照片细节强度大于第二张  2 第一张照片细节强度大于第二张   3 第一张���片��节��度等于第二张
    """
    # 读取图片
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # 使用拉普拉斯算子计算图像的二阶导数
    laplacian1 = cv2.Laplacian(image1, cv2.CV_64F)
    laplacian2 = cv2.Laplacian(image2, cv2.CV_64F)

    # 计算拉普拉acian图像的绝对值
    abs_laplacian1 = np.abs(laplacian1)
    abs_laplacian2 = np.abs(laplacian2)

    # 计算细节强度，这里使用方差
    detail_strength1 = np.var(abs_laplacian1)
    detail_strength2 = np.var(abs_laplacian2)

    # 比较细节强度
    if detail_strength1 > detail_strength2:
        return 1
    elif detail_strength1 < detail_strength2:
        return 2
    else:
        return 3

"""下载照片"""
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
    print(compare_images_ssim(r"D:\Google_download\IR_Common_20240628_104440480.jpg",
                             r"D:\Google_download\IR_Common_20240628_10444940.jpg"))
