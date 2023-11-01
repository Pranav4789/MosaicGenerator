from flask import Flask, jsonify, render_template, request, send_file
import base64
from PIL import Image
from scipy import spatial
import numpy as np
import filetype
import sys
import threading
import os
import requests

app = Flask(__name__)
tile_templates = []
outputs = []

str_url = "http://sp23-cs340-080.cs.illinois.edu:9000/makeMosiac"
def_url = "http://sp23-cs340-adm.cs.illinois.edu:1989/"

return_json = dict()
return_json["name"] = "art"
return_json["url"] = str(str_url)
return_json["author"] = "Pranav Penaganti"
return_json["tileImageCount"] = 60

response = requests.put(f"{def_url}/addMMG", data=return_json)

@app.route('/', methods=["GET"])
def GET_index():
    '''Route for "/" (frontend)'''
    return render_template("index.html")


@app.route('/makeMosiac', methods=["POST"])
def main():
    global outputs
    image = request.files["image"]
    tilesAcross = int(request.args.get("tilesAcross"))
    renderedTileSize = int(request.args.get("renderedTileSize"))
    fileFormat = (request.args.get("fileFormat"))
    width_temp = tilesAcross
    
    img_location = []
    img_pixels = []
    pix_color = []

    try:
        for img in os.listdir("tile_folder/art"):
            img_location.append(img)

        for i in img_location:
            p = os.path.join("tile_folder/art", i)

            if (filetype.is_image(p)):
                x = Image.open(p)
                changed_img = x.resize((renderedTileSize, renderedTileSize))
                img_pixels.append(changed_img)
                mean_color = np.array(changed_img).mean(axis=0).mean(axis=0)
                pix_color.append(mean_color)
                if len(mean_color) != 3:
                    print(str(mean_color) + " " + p)

        mosiac_img = Image.open(image)
        aspect_ratio = mosiac_img.size[1] / mosiac_img.size[0]
        new_height = int(width_temp * aspect_ratio)

        d = mosiac_img.size[0] // tilesAcross

        width_trimmed = d * tilesAcross
        height_trimmed = (mosiac_img.size[1] // d) * d

        cropped_mosiac = mosiac_img.crop((0, 0, width_trimmed, height_trimmed))
        changed_mosiac = cropped_mosiac.resize((tilesAcross, new_height))

        color_KD = spatial.KDTree(pix_color)
        color_res = np.zeros((tilesAcross, new_height), dtype=np.uint32)

        for row_pix in range(tilesAcross):
            for col_pix in range(new_height):
                color = color_KD.query(changed_mosiac.getpixel((row_pix, col_pix)))
                color_res[row_pix, col_pix] = color[1]

        output = Image.new('RGB', (tilesAcross * renderedTileSize, new_height * renderedTileSize))

        for row_pix in range(width_temp):
            for col_pix in range(new_height):
                index = color_res[row_pix, col_pix]
                output.paste(img_pixels[index], (row_pix * renderedTileSize , col_pix * renderedTileSize))

        f_str = image.filename
        out_str = "tile_folder/art"

        if fileFormat == "PNG":
            print(" xxx ")
            output_path = "mosiacs/" + f_str + out_str[12:] + "mosiac.png"
            output.save(output_path)
            outputs.append(output_path)
            return send_file(output_path)
        if fileFormat == "JPEG":
            output_path = "mosiacs/" + f_str + out_str[12:] + "mosiac.jpeg"
            output.save(output_path)
            outputs.append(output_path)
            return send_file(output_path)
    except:
        return "fail", 400
