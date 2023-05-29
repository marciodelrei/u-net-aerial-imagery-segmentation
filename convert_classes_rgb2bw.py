# Applying mask recursively on all color masks

import os
from glob import glob
from PIL import Image

from enum import Enum

class MaskColorMap(Enum):
    unlabeled = (0, 0, 0)
    paved_area = (128, 64, 128)
    dirt = (130, 76, 0)
    grass = (0, 102, 0)
    gravel = (112, 103, 87)
    water = (28, 42, 168)
    rocks = (48, 41, 30)
    pool = (0, 50, 89)
    vegetation = (107, 142, 35)
    roof = (70, 70, 70)
    wall = (102, 102, 156)
    window = (254, 228, 12)
    door = (254, 148, 12)
    fence = (190, 153, 153)
    fence_pole = (153, 153, 153)
    person = (255, 22, 96)
    dog = (102, 51, 0)
    car = (9, 143, 150)
    bicycle = (119, 11, 32)
    tree = (51, 51, 0)
    bald_tree = (190, 250, 190)
    ar_marker = (112, 150, 146)
    obstacle = (2, 135, 115)
    conflicting = (255, 0, 0)

# old_color = 255, 0, 255, 255
# black = (0, 0, 0)
# white = (255, 255, 255)


terrain_colors = []

noterrain_colors = []
noterrain_colors.append(MaskColorMap.unlabeled.value)
noterrain_colors.append(MaskColorMap.car.value)
noterrain_colors.append(MaskColorMap.tree.value)
noterrain_colors.append(MaskColorMap.pool.value)
noterrain_colors.append(MaskColorMap.roof.value)
noterrain_colors.append(MaskColorMap.fence_pole.value)
noterrain_colors.append(MaskColorMap.wall.value)
noterrain_colors.append(MaskColorMap.door.value)
noterrain_colors.append(MaskColorMap.window.value)
noterrain_colors.append(MaskColorMap.obstacle.value)
noterrain_colors.append(MaskColorMap.vegetation.value)
noterrain_colors.append(MaskColorMap.rocks.value)



colors_list = []
print("Packing colors masks")
for j, cls in enumerate(MaskColorMap):
    colors_list.append(cls.value)

converted_path = r"semantic\Tile 1\masks_bw"
if not os.path.exists(converted_path):
    os.mkdir(converted_path)

black = (0, 0, 0)
white = (255, 255, 255)

file_list = sorted(glob(r"semantic\Tile 1\masks\*.png"))
size_file_list = len(file_list)
for idx, mask_path in enumerate(file_list):
    print(f"Working in file {idx+1}/{size_file_list}: {mask_path}...")
    filename_ = os.path.basename(mask_path)
    filename = filename_.split(".")[0]
    ext = filename_.split(".")[1]
    bw_path = os.path.join(converted_path, f"{filename}.png")
    
    if not os.path.exists(bw_path):
        im = Image.open(mask_path)
        width, height = im.size

        pix = im.load()
        for x in range(0, width):
            for y in range(0, height):
                color = pix[x,y]

                if color in noterrain_colors:
                    im.putpixel((x, y), black)

                else:
                    im.putpixel((x, y), white)
                    
        im = im.convert('1')
        im.save(bw_path)