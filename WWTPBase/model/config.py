import os

from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.data.datasets import register_coco_instances

from . import PATH_MODEL_OUTPUT
from .. import PATH_TR_IMG_DIR, PATH_VA_IMG_DIR, PATH_TE_IMG_DIR, \
               PATH_TR_LABEL,   PATH_VA_LABEL,   PATH_TE_LABEL

register_coco_instances("WWTP_tr", {}, PATH_TR_LABEL, PATH_TR_IMG_DIR)
register_coco_instances("WWTP_va", {}, PATH_VA_LABEL, PATH_VA_IMG_DIR)
register_coco_instances("WWTP_te", {}, PATH_TE_LABEL, PATH_TE_IMG_DIR)


def GetBaseConfig(_loadTrainedModel=False, _checkPointModel="model_final.pth"):
    pretrained_cfg = "COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"  # from model zoo
    cfg = get_cfg()
    cfg.OUTPUT_DIR = PATH_MODEL_OUTPUT
    cfg.INPUT.FORMAT = "RGB"  # for statistics
    cfg.merge_from_file(model_zoo.get_config_file(pretrained_cfg))

    cfg.MODEL.PIXEL_MEAN = [90.39885420874151, 99.5118328394066, 88.92560153182265]
    cfg.MODEL.PIXEL_STD = [49.071554532775444, 41.866186751015704, 38.826466744058635]

    cfg.DATASETS.TRAIN = ("WWTP_tr",)
    cfg.DATASETS.TEST = ()
    cfg.DATALOADER.NUM_WORKERS = 1
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(pretrained_cfg)
    if _loadTrainedModel:
        cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, _checkPointModel)
    cfg.SOLVER.IMS_PER_BATCH = 32  # real batch size
    cfg.SOLVER.BASE_LR = 0.008  # LR
    cfg.SOLVER.MAX_ITER = 1000    # epoch
    cfg.MODEL.RPN.BATCH_SIZE_PER_IMAGE = 1024
    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 1024   # The "RoIHead batch size". 128 is faster, and good enough for this toy dataset (default: 512)
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # only has one class (icelake)
    return cfg
