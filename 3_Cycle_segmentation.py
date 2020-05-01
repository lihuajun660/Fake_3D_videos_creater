import os
import paddlehub as hub
from natsort import natsorted

def Cycle_seg(fore_image_path, paddlehub_out_path):
    g = os.walk(fore_image_path)
    for path, dir_list, file_list in g: 
        file_list = natsorted(file_list)
        for file_name in file_list:
            #取出一个前景文件
            front_pic = [os.path.join(path, file_name)]
            #加载hub模型
            module = hub.Module(name="deeplabv3p_xception65_humanseg")
            input_dict = {"image": front_pic}
            results = module.segmentation(data=input_dict,use_gpu = True,batch_size = 128,output_dir=paddlehub_out_path)

if __name__ == '__main__':
    input_Path = r'C:/Users/Administrator/Desktop/PaddlePaddle/2seg'
    output_Path = r'C:/Users/Administrator/Desktop/PaddlePaddle/res'
    Cycle_seg(input_Path, output_Path)
    print('图片人像扣除完毕！')