import math


def CoordZoom2LonLat(coordX, coordY, zoom):
    mapSize = 256 * math.pow(2, zoom)
    x = (coordX / mapSize) - 0.5
    y = 0.5 - (coordY / mapSize)
    lon = 360 * x
    lat = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi
    return lon, lat  # x, y


def ParseTileName(name):
    zoom, tileX, tileY = [int(x) for x in name.split(".")]
    return zoom, tileX, tileY


def Coord2LonLat(task_id, coords):
    zoom, tileX, tileY = ParseTileName(task_id)
    tileW = tileX * 256
    tileH = tileY * 256
    translated = [[tileW + x, tileH + y] for x, y in coords]
    return [list(CoordZoom2LonLat(x, y, zoom)) for x, y in translated]
