import os

from shapely.geometry import Polygon

from WWTPBase.utils.File import LoadPKL, SaveJson
from WWTPBase.utils.Geometry import pixel_coords_to_latlon



def Estm2GeoJson(estmpath, tarFileDir):
    """
    TODO
    """
    predDict = {
        "type": "FeatureCollection",
        "features":[]
    }
    id = 0
    for pklName in os.listdir(estmpath):
        bboxes, scores = LoadPKL(os.path.join(estmpath, pklName))
        for bbox, score in zip(bboxes, scores):
            x1, y1, x2, y2 = bbox
            bboxPlgn=[(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)]
            bboxCoords = pixel_coords_to_latlon(pklName[:-4], bboxPlgn)
            thisPred = {
                "type": "Feature",
                "properties": {
                    "task_id": pklName[:-4],
                    "prediction_id": id,
                    "prediction_class": int(0),
                    "score": float(score),
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [bboxCoords]
                }
            }
            id += 1
            predDict["features"].append(thisPred)
    SaveJson(predDict, tarFileDir)
