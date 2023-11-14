import os
import shutil
from WWTPBase import PATH_TE_IMG_DIR


"""
ONLY RUN ONCE, if there is no dot in file names.
"""

for imgName in os.listdir(PATH_TE_IMG_DIR):
    shutil.move(
        os.path.join(PATH_TE_IMG_DIR, imgName),
        os.path.join(PATH_TE_IMG_DIR, imgName[:2] + '.' + imgName[2:7] + '.' + imgName[7:])
    )
