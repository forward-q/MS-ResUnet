import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 如果要显示中文字体,则在此处设为：SimHei
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

x = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])

RDCAGAN = np.array([
    29.07, 29.68, 30.08, 30.13, 30.17, 30.45, 30.54, 30.66, 30.88, 30.87,
    30.56, 31.07, 31.09, 31.18, 31.69, 31.88, 32.01, 32.03, 32.09, 32.18,
    32.37, 32.36, 31.15, 32.19, 32.28, 32.29, 32.37, 32.39, 32.67, 32.68,
    33.01, 33.13, 33.15, 33.16, 33.04, 33.17, 33.16, 33.19, 33.28, 33.39,
    33.40, 33.22, 32.87, 32.26, 33.36, 33.36, 33.25, 33.39, 33.38, 33.39,  # 50
    33.39, 33.38, 33.32, 33.35, 33.29, 33.36, 33.38, 33.44, 33.07, 33.05,
    33.13, 33.26, 33.26, 33.17, 33.30, 33.21, 33.28, 33.32, 33.35, 33.29,
    33.19, 33.23, 33.28, 33.34, 33.36, 33.12, 33.23, 33.30, 33.19, 33.23,
])
RCAN = np.array([
    29.07, 29.98, 30.28, 30.43, 30.57, 30.65, 30.84, 30.96, 30.980, 30.87,
    31.86, 31.87, 31.69, 31.98, 31.99, 32.08, 32.21, 32.43, 32.59, 32.68,
    32.67, 32.66, 31.95, 32.59, 32.58, 32.59, 32.67, 32.89, 33.07, 33.08,
    33.15, 33.37, 33.39, 33.46, 33.44, 33.47, 33.56, 33.59, 33.58, 33.51,
    33.61, 33.62, 32.87, 32.66, 33.36, 33.36, 33.55, 33.59, 33.58, 33.59,  # 50
    33.49, 33.58, 33.62, 33.35, 33.59, 33.66, 33.68, 33.54, 33.67, 33.55,
    33.53, 33.46, 33.56, 33.47, 33.50, 33.51, 33.58, 33.62, 33.55, 33.59,
    33.49, 33.53, 33.58, 33.44, 33.46, 33.52, 33.53, 33.50, 33.49, 33.53,
])
EDSR = np.array([

29.07, 29.98, 30.08, 30.23, 30.37, 30.55, 30.64, 30.86, 30.88, 30.97,
    30.76, 31.87, 31.69, 31.88, 31.89, 31.88, 32.11, 32.33, 32.39, 32.59,
    32.65, 32.60, 31.83, 32.46, 32.43, 32.40, 32.55, 32.76, 32.97, 32.98,
    33.09, 33.29, 33.25, 33.34, 33.36, 33.47, 33.46, 33.49, 33.48, 33.41,
    33.41, 33.42, 32.57, 32.56, 33.46, 33.46, 33.55, 33.49, 33.48, 33.39,  # 50
    33.39, 33.48, 33.42, 33.35, 33.69, 33.46, 33.38, 33.44, 33.47, 33.35,
    33.33, 33.46, 33.36, 33.37, 33.40, 33.41, 33.28, 33.32, 33.35, 33.49,
    33.39, 33.43, 33.48, 33.34, 33.26, 33.32, 33.43, 33.40, 33.39, 33.43,
])
ESRGAN = np.array([
    29.07, 29.48, 30.08, 30.03, 30.07, 30.15, 30.34, 30.46, 30.68, 30.67,
    30.76, 31.07, 31.09, 31.08, 31.59, 31.68, 32.01, 32.02, 32.07, 32.15,
    32.17, 32.16, 31.12, 32.14, 32.29, 32.27, 32.25, 32.29, 32.47, 32.48,
    33.05, 33.17, 33.19, 33.16, 33.02, 33.15, 33.16, 33.16, 33.26, 33.31,
    33.21, 33.22, 32.67, 33.16, 33.16, 33.26, 33.25, 33.32, 33.18, 33.19,  # 50
    33.29, 33.28, 33.22, 33.15, 33.29, 33.34, 33.18, 33.44, 33.04, 33.07,
    33.13, 33.23, 33.24, 33.17, 33.20, 33.01, 33.08, 33.12, 33.15, 33.19,
    33.21, 33.23, 33.28, 33.04, 33.06, 33.12, 33.13, 33.10, 33.09, 33.13,
])
SRGAN= np.array([
    29.07, 29.38, 30.08, 30.01, 30.05, 30.07, 30.14, 30.36, 30.58, 30.47,
    30.66, 31.07, 31.10, 31.09, 31.39, 31.58, 32.01, 32.03, 32.09, 32.18,
    32.12, 32.11, 31.15, 32.19, 32.08, 32.09, 32.07, 32.09, 32.37, 32.38,  # 23
    33.05, 33.07, 33.09, 33.06, 33.04, 33.17, 33.16, 33.19, 33.28, 33.21,
    33.11, 33.19, 32.57, 33.06, 33.16, 33.06, 33.15, 33.29, 33.13, 33.15,  # 43
    33.29, 33.08, 33.21, 33.13, 33.24, 33.26, 33.08, 33.34, 33.07, 33.05,
    33.11, 33.36, 33.33, 33.15, 33.19, 33.00, 33.18, 33.10, 33.25, 33.29,
    33.19, 33.03, 33.28, 33.14, 33.03, 33.10, 33.03, 33.20, 33.06, 33.03,
])
DRRN = np.array([
    29.07, 29.18, 29.38, 29.43, 29.67, 29.95, 30.04, 30.16, 30.28, 30.27,
    30.36, 30.77, 30.89, 30.98, 31.29, 31.28, 31.51, 31.83, 31.79, 31.68,
    31.77, 31.86, 31.55, 31.79, 31.98, 32.09, 32.07, 31.89, 31.87, 31.68,  # 23
    31.75, 31.87, 31.99, 32.46, 32.34, 32.47, 32.36, 32.49, 32.38, 32.41,
    32.41, 32.52, 31.87, 32.36, 32.46, 32.36, 32.45, 32.49, 32.58, 32.49,  # 43
    32.39, 32.38, 32.42, 32.35, 32.49, 32.46, 32.08, 32.34, 32.37, 32.45,
    32.33, 32.36, 32.46, 32.37, 32.40, 32.41, 32.38, 32.32, 32.45, 32.49,
    32.39, 32.43, 32.28, 32.54, 32.46, 32.42, 32.53, 32.40, 32.49, 32.53,
])
VDSR = np.array([
    29.07, 29.18, 29.28, 29.63, 29.77, 29.85, 30.04, 30.16, 30.08, 30.17,
    30.26, 30.67, 30.79, 30.68, 31.19, 31.08, 31.61, 31.83, 31.79, 31.78,
    31.67, 31.76, 31.45, 31.69, 31.88, 32.09, 32.07, 31.69, 31.77, 31.58,  # 23
    31.65, 31.77, 31.89, 32.26, 32.34, 32.27, 32.36, 32.39, 32.28, 32.31,
    32.21, 32.32, 31.67, 32.36, 32.36, 32.36, 32.25, 32.39, 32.38, 32.29,  # 43
    32.29, 32.18, 32.22, 32.35, 32.39, 32.26, 32.08, 32.24, 32.17, 32.25,
    32.13, 32.26, 32.36, 32.17, 32.30, 32.21, 32.38, 32.32, 32.25, 32.29,
    32.39, 32.33, 32.38, 32.44, 32.36, 32.32, 32.43, 32.30, 32.39, 32.43,
])
FSRCNN = np.array([
    29.07, 29.08, 29.18, 29.43, 29.57, 29.75, 30.04, 30.16, 30.08, 30.17,
    30.16, 30.47, 30.59, 30.58, 31.19, 31.08, 31.31, 31.53, 31.69, 31.58,
    31.47, 31.46, 31.25, 31.59, 31.68, 32.09, 32.07, 31.49, 31.57, 31.38,  # 23
    31.45, 31.57, 31.69, 32.26, 32.04, 32.17, 32.26, 32.29, 32.18, 32.31,
    32.21, 32.12, 31.57, 32.26, 32.26, 32.16, 32.25, 32.29, 32.18, 32.29,  # 43
    32.29, 32.18, 32.32, 32.25, 32.29, 32.26, 32.08, 32.04, 32.17, 32.25,
    32.13, 32.06, 32.26, 32.17, 32.20, 32.11, 32.28, 32.12, 32.25, 32.39,
    32.29, 32.13, 32.28, 32.34, 32.16, 32.22, 32.33, 32.10, 32.19, 32.23,
])
SRCNN = np.array([
    29.02, 29.06, 29.18, 29.33, 29.47, 29.55, 30.04, 30.16, 30.08, 30.17,
    30.06, 30.37, 30.39, 30.48, 31.19, 31.08, 31.11, 31.33, 31.59, 31.48,
    31.27, 31.36, 31.05, 31.49, 31.48, 32.09, 32.07, 31.39, 31.27, 31.38,  # 23
    31.35, 31.47, 31.39, 32.26, 32.04, 32.17, 32.16, 32.19, 32.08, 32.21,
    32.11, 32.12, 31.47, 32.16, 32.06, 32.06, 32.15, 32.19, 32.18, 32.29,  # 43
    32.19, 32.28, 32.12, 32.25, 32.19, 32.36, 32.08, 32.04, 32.07, 32.25,
    32.13, 32.06, 32.26, 32.07, 32.10, 32.11, 32.18, 32.02, 32.15, 32.29,
    32.09, 32.13, 32.18, 32.04, 32.16, 32.12, 32.33, 32.20, 32.09, 32.13,
])
# 对x和y1进行插值，使图像圆滑
# x_smooth = np.linspace(x.min(), x.max(), 50)
# RDCAGAN_smooth = make_interp_spline(x, RDCAGAN)(x_smooth)
# plt.plot(x_smooth, RDCAGAN_smooth, color="darkgreen", label='Score', linewidth=2.0)
# 正常展示
plt.plot(x, RDCAGAN, color="darkgreen", label='RDCAGAN(our)', linewidth=1.0)
plt.plot(x, ESRGAN, color="dodgerblue", label='ESRGAN', linewidth=1.0)
plt.plot(x, RCAN, color="r", label='RCAN', linewidth=1.0)
plt.plot(x, EDSR, color="navy", label='EDSR', linewidth=1.0)
plt.plot(x, SRGAN, color="c", label='SRGAN', linewidth=1.0)
plt.plot(x, DRRN, color="magenta", label='DRRN', linewidth=1.0)
plt.plot(x, VDSR, color="slategray", label='VDSR', linewidth=1.0)
plt.plot(x, FSRCNN, color="lawngreen", label='FSRCNN', linewidth=1.0)
plt.plot(x, SRCNN, color="darkorange", label='SRCNN', linewidth=1.0)

plt.xticks(fontsize=12, fontweight='bold')  # 默认字体大小为10
plt.yticks(fontsize=12, fontweight='bold')
plt.xlabel("epoch", fontsize=13, fontweight='bold')
plt.ylabel("PSNR", fontsize=13, fontweight='bold')
plt.xlim(-0.5, 81)  # 设置x轴的范围
plt.ylim(29.00, 34.25)

plt.legend()  # 显示各曲线的图例
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=8)  # 设置图例字体的大小和粗细
plt.show()
