import io
from flask import Flask, request, make_response, send_file
from PIL import Image, ImageChops, ImageStat
import requests
import numpy as np
import math

str_url = "http://sp23-cs340-080.cs.illinois.edu:9013/reduceMosaic"
def_url = "http://sp23-cs340-adm.cs.illinois.edu:1989/"

app = Flask(__name__)


def compare_tiles(base_tile, tile1, tile2):
    diff1 = ImageChops.difference(base_tile, tile1).convert("L")
    diff2 = ImageChops.difference(base_tile, tile2).convert("L")
    
    return 1 if sum(diff1.getdata()) <= sum(diff2.getdata()) else 2

def mosaic_reducer(base_image, mosaic1, mosaic2, tiles_across, rendered_tile_size, fileFormat):
    base_image = Image.open(base_image)
    mosaic1 = Image.open(mosaic1).resize(base_image.size)
    mosaic2 = Image.open(mosaic2).resize(base_image.size)

    

    reduced_mosaic = Image.new("RGB", base_image.size)

    d = mosaic1.size[0] / tiles_across
    vertical_tiles = int(base_image.size[1] / d)

    for y in range(0, base_image.size[1], int(d)):
        for x in range(0, base_image.size[0], int(d)):
            base_tile = base_image.crop((x, y, x + d, y + d))
            mosaic1_tile = mosaic1.crop((x, y, x + d, y + d))
            mosaic2_tile = mosaic2.crop((x, y, x + d, y + d))

            selected_mosaic = compare_tiles(base_tile, mosaic1_tile, mosaic2_tile)

            if selected_mosaic == 1:
                reduced_mosaic.paste(mosaic1_tile, (x, y))
            else:
                reduced_mosaic.paste(mosaic2_tile, (x, y))

    # Calculate the final mosaic size directly using tiles_across and rendered_tile_size
    final_mosaic_size = math.floor(tiles_across * rendered_tile_size), math.floor(vertical_tiles * rendered_tile_size)

    reduced_mosaic = reduced_mosaic.resize(final_mosaic_size)

    output = io.BytesIO()
    reduced_mosaic.save(output, format=fileFormat.upper())
    output.seek(0)
    return output

@app.route("/reduceMosaic", methods=["POST"])
def reduce():
    print("_________")
    baseImage = request.files["baseImage"]
    mosaic1 = request.files["mosaic1"]
    mosaic2 = request.files["mosaic2"]

    renderedTileSize = int(request.args.get("renderedTileSize"))
    tilesAcross = int(request.args.get("tilesAcross"))
    fileFormat = request.args.get("fileFormat")

    # Your reduce logic here:
    mosaic_reduction = mosaic_reducer(baseImage, mosaic1, mosaic2, tilesAcross, renderedTileSize, fileFormat)

    # Return a reduced mosaic that combines the best of mosaic1 and mosaic2:
    return make_response(mosaic_reduction)


reducer_data = {
    "url": str_url,
    "author": "Pranav Penaganti"
}

response = requests.put("http://sp23-cs340-adm.cs.illinois.edu:1989/registerReducer", data=reducer_data)