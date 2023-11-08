import os


PATH_DATA = "./data"

PATH_TR_IMG_DIR = os.path.join(PATH_DATA, "train2017")
PATH_VA_IMG_DIR = os.path.join(PATH_DATA, "val2017")
PATH_TE_IMG_DIR = os.path.join(PATH_DATA, "test_sample")

PATH_ANNOTATION = os.path.join(PATH_DATA, "annotations")

PATH_TR_LABEL = os.path.join(PATH_ANNOTATION, "instances_train2017.json")
PATH_VA_LABEL = os.path.join(PATH_ANNOTATION, "instances_val2017.json")
PATH_TE_LABEL = os.path.join(PATH_ANNOTATION, "test_sample.json")

PATH_MODEL_OUTPUT = "./WWTPBase/model/output"

PATH_TMP = "./tmp"
PATH_VA_ESTM = os.path.join(PATH_TMP, "VAEstm")
PATH_TE_ESTM = os.path.join(PATH_TMP, "TEEstm")
PATH_VA_ESTM_PLOT = os.path.join(PATH_TMP, "VAEstmPlot")
PATH_TE_ESTM_PLOT = os.path.join(PATH_TMP, "TEEstmPlot")

CONFINDENCE = 0.2
