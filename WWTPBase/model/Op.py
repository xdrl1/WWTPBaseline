import os

from detectron2.engine import DefaultTrainer, DefaultPredictor
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

from WWTPBase.model.config import *
from WWTPBase.utils.File import LoadImg, LoadJson, ReloadDir, SavePKL


def Train(loadTrainedModel=False, checkPointModel="model_final.pth"):
    """
    The training process will first load a pre-trained model provided by
    detectron2 library (from Meta). If `isContinue` is true, then the
    trainer will load `checkPointModelName` in `cfg.OUTPUT_DIR` instead
    to continue unfinished training process.
    """
    cfg = GetBaseConfig(_loadTrainedModel=loadTrainedModel, _checkPointModel=checkPointModel)
    os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
    trainer = DefaultTrainer(cfg)
    trainer.resume_or_load(resume=False)
    trainer.train()


def GetTrainedModel(model, confindence):
    """
    the model should be within `cfg.OUTPUT_DIR`
    """
    cfg = GetBaseConfig(_loadTrainedModel=True, _checkPointModel=model)
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = confindence
    return DefaultPredictor(cfg)


def GetEstimation(predictor, img):
    out = predictor(img[:, :, ::-1])  # to BGR mode
    bboxes = out["instances"].pred_boxes.tensor.to("cpu")
    scores = out["instances"].scores.to("cpu")
    assert bboxes.size(0) == scores.size(0)
    return bboxes.numpy(), scores.numpy()


def GetEstimationByFolder(predictor, srcFolder, tarFolder, imgFormat='jpg', plot=False, plotFolder=None, labelDir=None):
    ReloadDir(tarFolder)
    if plot:
        ReloadDir(plotFolder)

    for imgFileName in os.listdir(srcFolder):
        thisImg = LoadImg(os.path.join(srcFolder, imgFileName))
        # box is (x1, y1, x2, y2) 1=tl, 2=br
        # see: https://detectron2.readthedocs.io/en/latest/_modules/detectron2/structures/boxes.html
        bboxes, scores = GetEstimation(predictor, thisImg)
        SavePKL([bboxes, scores], os.path.join(tarFolder, imgFileName.replace(imgFormat, 'pkl')))
        if plot:
            # find label is...
            plt.figure(figsize=(11, 5), dpi=300.0)
            plt.subplot(121)
            plt.imshow(thisImg)
            plt.title("origin img")

            plt.subplot(122)
            plt.imshow(thisImg)
            ax = plt.gca()
            for box in bboxes:
                x1, y1, x2, y2 = box
                ax.add_patch(Rectangle((x1, y1), x2-x1, y2-y1, linewidth=1, edgecolor='r', facecolor='none'))
            plt.title("estimation")

            plt.savefig(os.path.join(plotFolder, imgFileName), dpi='figure')
            plt.close()
