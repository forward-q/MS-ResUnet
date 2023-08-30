import glob
import cv2

path = glob.glob("/content/drive/MyDrive/super-resolution/SRCNN-PyTorch/data/CTtrain/*.bmp")

i = 1
for img in path:
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    backtorgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
    cv2.imwrite(f"/content/drive/MyDrive/super-resolution/SRCNN-PyTorch/data/CTtrainRGB/{i:04d}.png",backtorgb)
    i = i + 1
    print('ok')
