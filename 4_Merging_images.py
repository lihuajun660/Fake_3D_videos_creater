import os
from PIL import Image
import numpy as np
from natsort import natsorted
import re
def blend_images(fore_image, base_image, output_path):
    """
    将抠出的人物图像换背景
    fore_image: 前景图片，抠出的人物图片
    base_image: 背景图片
    """
    # 读入图片 取出不含路径的文件名
    houtput_pic = output_path + os.path.basename(fore_image)
    base_image = Image.open(base_image).convert('RGB')
    fore_image = Image.open(fore_image).resize(base_image.size)

    # 图片加权合成
    scope_map = np.array(fore_image)[:,:,-1] / 255
    scope_map = scope_map[:,:,np.newaxis]
    scope_map = np.repeat(scope_map, repeats=3, axis=2)
    res_image = np.multiply(scope_map, np.array(fore_image)[:,:,:3]) + np.multiply((1-scope_map), np.array(base_image))
    
    #保存图片
    res_image = Image.fromarray(np.uint8(res_image))
    res_image.save(houtput_pic)

#两个目录合并

def merging_images(fore_image_path, base_image_path,output_path):
    num_re = re.compile(r'\d*')
    f = os.walk(fore_image_path)  
    for path, dir_list, file_list in f:
        file_list = natsorted(file_list)    
        for file_name in file_list:  
            humanseg_pic = os.path.join(path, file_name)
            name1 = num_re.findall(str(humanseg_pic))
            #name1.remove(' ')
            #图像操作 背景路径循环
            b = os.walk(base_image_path)
            for path1,dir_list1,file_list1 in b:  
                file_list1 = natsorted(file_list1) 
                for file_name1 in file_list1:
                    background_pic = os.path.join(path1, file_name1)
                    name2 = num_re.findall(str(background_pic))
                    #合成
                    #print(humanseg_pic , background_pic)
                    if name1[-6] == name2[-6]:
                        blend_images(humanseg_pic , background_pic, output_path)
if __name__ == '__main__':
    input_Path = r'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/test_run/Segmented_human'
    base_Path = r'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/test_run/background'
    output_Path = r'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/test_run/Merged/2Create'
    merging_images(input_Path, base_Path, output_Path)
    print('合成图片文件夹生成完毕！')
