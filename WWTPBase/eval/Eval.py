import geopandas
import os

from shapely.geometry import Polygon

from WWTPBase.utils.File import LoadPKL



def Estm2GDF(estmpath):
    """
    TODO
    """
    geo_series_list = []
    id = 0
    for feature in os.listdir(estmpath):
        pred_polygon = Polygon(feature['geometry']['coordinates'][0])
        geo_series = {
            'task_id': feature['properties']['task_id'],
            'score': feature['properties']['score'],
            'prediction_id': id,
            'type': feature['geometry']['type'],
            'if_correct': False,
            'geometry': pred_polygon
        }
        geo_series_list.append(geo_series)
        id += 1
    return geopandas.GeoDataFrame(geo_series_list)