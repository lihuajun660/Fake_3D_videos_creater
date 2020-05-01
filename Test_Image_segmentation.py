test_img_path = [r"C:/Users/Administrator/Pictures/Camera Roll/Moonbyul_Fourth_Universe_Reality_in_BLACK.jpg"]

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

img = mpimg.imread(test_img_path[0]) 

#展示待预测图片
# plt.figure(figsize=(10,10))
# plt.imshow(img) 
# plt.axis('off') 
# plt.show()

import paddlehub as hub
module = hub.Module(name="deeplabv3p_xception65_humanseg")
input_dict = {"image": test_img_path}

# execute predict and print the result
results = module.segmentation(data=input_dict)
for result in results:
    print(result)

# 预测结果展示
# test_img_path = "./humanseg_output/" + "Moonbyul_Fourth_Universe_Reality_in_BLACK.png"
# img = mpimg.imread(test_img_path)
# plt.figure(figsize=(10,10))
# plt.imshow(img) 
# plt.axis('off') 
# plt.show()


from PIL import Image
import numpy as np

def blend_images(fore_image, base_image):
    """
    将抠出的人物图像换背景
    fore_image: 前景图片，抠出的人物图片
    base_image: 背景图片
    """
    # 读入图片
    base_image = Image.open(base_image).convert('RGB')
    fore_image = Image.open(fore_image).resize(base_image.size)

    # 图片加权合成
    scope_map = np.array(fore_image)[:,:,-1] / 255
    scope_map = scope_map[:,:,np.newaxis]
    scope_map = np.repeat(scope_map, repeats=3, axis=2)
    res_image = np.multiply(scope_map, np.array(fore_image)[:,:,:3]) + np.multiply((1-scope_map), np.array(base_image))

    #保存图片
    res_image = Image.fromarray(np.uint8(res_image))
    res_image.save("blend_res_img.jpg")
    
    
blend_images('./humanseg_output/Moonbyul_Fourth_Universe_Reality_in_BLACK.png', r'C:/Users/Administrator/Pictures/wallpapers_cyberpunk/914670.jpg')

# 展示合成图片
plt.figure(figsize=(10,10))
img = mpimg.imread("./blend_res_img.jpg")
plt.imshow(img) 
plt.axis('off') 
plt.show()