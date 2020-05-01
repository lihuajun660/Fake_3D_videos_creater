import cv2
#视频分帧
def video_to_images(file_name,filepath): #路径要带 '/'
    vidcap = cv2.VideoCapture(file_name)
    success, image = vidcap.read()
    count = 0
    success = True
    angle=90
    while success:
        success,image = vidcap.read()
        if success==True:
            cv2.imwrite(filepath + "frame%d.jpg" % count, image)   # save frame as JPEG file
            count = count + 1
#调用方式   把"work/test_video.mp4"视频,分解到"work/video2image"目录 路径要带 '/'
video_to_images(r'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/work/Irene_ad.mp4',
                r'C:/Users/Administrator/Desktop/PaddlePaddle/PaddleHub/Image_segmentation_human/work/seg_frames')