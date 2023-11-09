from WWTPBase import PATH_VA_IMG_DIR, PATH_VA_LABEL, PATH_VA_ESTM, \
                     PATH_VA_ESTM_PLOT, PATH_VA_GEOJSON, \
                     PATH_TE_IMG_DIR, PATH_TE_LABEL, PATH_TE_ESTM, \
                     PATH_TE_ESTM_PLOT, PATH_TE_GEOJSON, \
                     CONFINDENCE
from WWTPBase.model.Op import Train, GetTrainedModel, GetEstimationByFolder
from WWTPBase.eval.Eval import Estm2GeoJson

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
Estm2GeoJson(PATH_VA_ESTM, PATH_VA_GEOJSON)
# te
GetEstimationByFolder(
    predictor,
    PATH_TE_IMG_DIR,
    PATH_TE_ESTM,
    imgFormat='jpg',
    plot=True,
    plotFolder=PATH_TE_ESTM_PLOT,
    labelDir=PATH_TE_LABEL)
Estm2GeoJson(PATH_TE_ESTM, PATH_TE_GEOJSON)
