# # 导入需要的模块
# from glob import glob
# from PIL import Image
# import os
#
# # 图片路径
# # 使用 glob模块 获得文件夹内所有jpg图像
# img_path = glob("B:\\MulScale_ResUnet\\results\\test\\MSRU_x8\\*.png")
# # 存储（输出）路径
# path_save = "B:\\MulScale_ResUnet\\results\\test\\MSRU_x888"
#
# for i, file in enumerate(img_path):
#     name = os.path.join(path_save, "%d.png" % i)
#     im = Image.open(file)
#     # im.thumbnail((720,1280))
#     reim = im.resize((500, 500))
#     print(im.format, reim.size, reim.mode)
#     reim.save(name, im.format)
from PIL import Image
from os import listdir
import numpy as np


def resize_img(input_path, out_path, x, y):
    fp = open(input_path, 'rb')
    pic = Image.open(fp)
    pic_array = np.array(pic)
    fp.close()
    img = Image.fromarray(pic_array)
    print("修改前: ", img.size)
    new_img = img.resize((x, y))
    new_img.save(out_path)
    print("修改后: ", new_img.size)


if __name__ == '__main__':
    inpath = "results\\test\\MSRU_x8"  # 在此输入图片输入路径
    outpath = "results\\test\\MSRU_x888"  # 在此输入图片输出路径
    x = 500  # 图片水平长度
    y = 500  # 图片垂直长度

    for i in listdir(inpath):
        resize_img(inpath + '\\' + i, outpath + '\\' + i, x, y)
        print("--------------------")