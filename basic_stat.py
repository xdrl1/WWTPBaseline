import os
import statistics

from WWTPBase import PATH_TR_IMG_DIR
from WWTPBase.utils.File import LoadImg


imgDir = PATH_TR_IMG_DIR
# this is really dumb though...
r = []
g = []
b = []
nImg = len(os.listdir(imgDir))
for imgName in os.listdir(imgDir):
    img = LoadImg(os.path.join(imgDir, imgName))
    imgR = img[:, :, 0].flatten().tolist()
    imgG = img[:, :, 1].flatten().tolist()
    imgB = img[:, :, 2].flatten().tolist()
    r += imgR
    g += imgG
    b += imgB
print(statistics.mean(r), statistics.mean(g), statistics.mean(b))
# 90.39885420874151 99.5118328394066 88.92560153182265
print(statistics.stdev(r), statistics.stdev(g), statistics.stdev(b))
# 49.071554532775444 41.866186751015704 38.826466744058635
