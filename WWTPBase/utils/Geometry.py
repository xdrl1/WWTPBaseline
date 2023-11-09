import math


def pixel_coords_zoom_to_lat_lon(PixelX, PixelY, zoom):
    MapSize = 256 * math.pow(2, zoom)
    x = (PixelX / MapSize) - 0.5
    y = 0.5 - (PixelY / MapSize)
    lon = 360 * x
    lat = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi

    return lon, lat


def parse_tile_name(name):
    zoom, TileX, TileY = [int(x) for x in name.split(".")]
    return TileX, TileY, zoom


def pixel_coords_to_latlon(task_id, bbox_polygon):
    TileX, TileY, zoom = parse_tile_name(task_id)
    print(TileX, TileY, zoom)
    PixelX = TileX * 256
    PixelY = TileY * 256
    coords = bbox_polygon

    translated = [[PixelX + y, PixelY + x] for x, y in coords]

    return [list(pixel_coords_zoom_to_lat_lon(x, y, zoom)) for x, y in translated]
