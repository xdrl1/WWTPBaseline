from WWTPBase import PATH_VA_IMG_DIR, PATH_VA_LABEL, PATH_VA_ESTM, PATH_VA_ESTM_PLOT, \
                     PATH_TE_IMG_DIR, PATH_TE_LABEL, PATH_TE_ESTM, PATH_TE_ESTM_PLOT, \
                     CONFINDENCE
from WWTPBase.model.Op import Train, GetTrainedModel, GetEstimationByFolder

RETRAIN = False

if RETRAIN:
    Train(loadTrainedModel=False)

predictor = GetTrainedModel("model_final.pth", confindence=CONFINDENCE)

# va
GetEstimationByFolder(
    predictor,
    PATH_VA_IMG_DIR,
    PATH_VA_ESTM,
    imgFormat='png',
    plot=True,
    plotFolder=PATH_VA_ESTM_PLOT,
    labelDir=PATH_VA_LABEL)

# te
GetEstimationByFolder(
    predictor,
    PATH_TE_IMG_DIR,
    PATH_TE_ESTM,
    imgFormat='jpg',
    plot=True,
    plotFolder=PATH_TE_ESTM_PLOT,
    labelDir=PATH_TE_LABEL)
