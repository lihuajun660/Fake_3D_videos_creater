import os
import cv2
def images_to_video(input_filepath,output_filename): 
    fps = 24 # 帧率
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    videoWriter = cv2.VideoWriter(output_filename, fourcc, fps, (1280, 720))   #(1360,480)为视频大小
    for i in range(0,900):
        img12 = cv2.imread(input_filepath +'/Imagecropped%d.jpg' %i)
        videoWriter.write(img12)

if __name__ == '__main__':
    images_folder_path = 'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/test_run/merged_new'
    filename = 'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/test_run/001.avi'
    images_to_video(images_folder_path, filename)
    print('视频生成完毕！')