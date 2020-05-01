import os
import cv2
import numpy as np
import imghdr
import time
import re
from natsort import natsorted
#扫描生成输出图片列表
def eachFile(filepath):
    list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        list.append(child)
    return list

def cropping(filePath_bak): 
# 指定待预测图片路径，遍历剪裁图片周围的黑框及图片左右两道黑柱
    files = eachFile(filePath)
    count = 0
    files = natsorted(files)
    for file in files:
        print(file)
        img = cv2.imread(file)
        #上下两边留出黑色区域
        img[0: 70, 0: 1280] = [0,0,0] 
        img[650: 720, 0:1280] = [0,0,0]
        #中间切除两块黑色长条区域
        img[0:720, 360:380] = [0,0,0]
        img[0:720, 900:920] = [0,0,0]
        cv2.imwrite(filePath_bak + 'Imagecropped%d.jpg'  %count , img)
        count += 1

if __name__ == '__main__':
    filePath = r"C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/work"
    filePath_bak = r"C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/test_run/background/"
    cropping(filePath_bak)
    # print(eachFile(filePath))
    print('视频背景图片裁剪完毕！')