import os


PATH_DATA = "./data"

PATH_TR_IMG_DIR = os.path.join(PATH_DATA, "train2017")
PATH_VA_IMG_DIR = os.path.join(PATH_DATA, "val2017")
PATH_TE_IMG_DIR = os.path.join(PATH_DATA, "test_sample")

PATH_ANNOTATION = os.path.join(PATH_DATA, "annotations")

PATH_TR_LABEL = os.path.join(PATH_ANNOTATION, "instances_train2017")
PATH_VA_LABEL = os.path.join(PATH_ANNOTATION, "instances_val2017")
PATH_TE_LABEL = os.path.join(PATH_ANNOTATION, "test_sample.json")
