import random
from PIL import Image, ImageDraw
from math import radians, cos, sin
import os
import shutil
import svgwrite
import csv

# キャンバスのサイズを指定にゃん
width = 300
# 黄金比
golden_ratio = (1 + 5**0.5) / 2
height = int(width * golden_ratio)

# def generate_golden_rectangle(angle, size):
#     width = size
#     height = size * golden_ratio
    
#     points = [
#         (0, 0),
#         (width, 0),
#         (width, height),
#         (0, height)
#     ]
    
#     rotated_points = []
#     for point in points:
#         x = point[0] * cos(radians(angle)) - point[1] * sin(radians(angle))
#         y = point[0] * sin(radians(angle)) + point[1] * cos(radians(angle))
#         rotated_points.append((x, y))

#     return rotated_points

def generate_rectangle(angle, size1, size2):
    width = size1
    height = size2
    
    points = [
        (0, 0),
        (width, 0),
        (width, height),
        (0, height)
    ]
    
    rotated_points = []
    for point in points:
        x = point[0] * cos(radians(angle)) - point[1] * sin(radians(angle))
        y = point[0] * sin(radians(angle)) + point[1] * cos(radians(angle))
        rotated_points.append((x, y))

    return rotated_points

def generate_random_triangle(angle, size):
    points = [
        (0, 0),
        (size, 0),
        (size // 2, int(size * 0.5**0.5))
    ]

    rotated_points = []
    for point in points:
        x = point[0] * cos(radians(angle)) - point[1] * sin(radians(angle))
        y = point[0] * sin(radians(angle)) + point[1] * cos(radians(angle))
        rotated_points.append((x, y))

    return rotated_points


def draw_image(i):
    # キャンバスを作成
    dwg = svgwrite.Drawing(f"./out_svg/output{i}.svg", size=(width, height), profile="tiny", debug=True)
    # 白い背景を作成
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill="white"))
    data = []
    # 白いキャンバスを作成にゃん
    canvas = Image.new("RGB", (width, height), "white")
    # draw = ImageDraw.Draw(canvas)
    # ランダムな縁どられた円を描画にゃん
    for _ in range(random.randint(0, 3)):
        x, y = random.randint(-width, width), random.randint(-height, height)
        radius = random.randint(20, 300)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black", width=2)
        dwg.add(dwg.circle(center=(x, y), r=radius, stroke="black", fill="none"))
        # data.append
    # ランダムな縁どられた四角形を描画にゃん
    # for _ in range(random.randint(0, 3)):
    #     x1, y1 = random.randint(-width, width), random.randint(-height, height)
    #     x2, y2 = random.randint(-width, width), random.randint(-height, height)
    #     draw.rectangle((x1, y1, x2, y2), outline="black", width=3)

    # 黄金比の四角形をランダムな角度と大きさで描画
    for _ in range(random.randint(1, 4)):
        angle = random.uniform(0, 360)
        size1 = random.uniform(30, 500)
        size2 = random.uniform(30, 500)
        points = generate_rectangle(angle, size1, size2)

        # 座標をランダムにオフセット
        x_offset = random.uniform(-width, width)
        y_offset = random.uniform(-height, height)
        points = [(x + x_offset, y + y_offset) for x, y in points]

        draw.polygon(points, outline='black', width=2)
        dwg.add(dwg.polygon(points=points, stroke="black", fill="none"))

    # 三角形をランダムな角度と大きさで描画
    for _ in range(random.randint(0, 3)):
        size = random.uniform(30, 300)
        angle = random.uniform(0, 360)

        points = generate_random_triangle(angle, size)

        # 座標をランダムにオフセット
        x_offset = random.uniform(0, width)
        y_offset = random.uniform(0, height)
        points = [(x + x_offset, y + y_offset) for x, y in points]

        draw.polygon(points, outline='black', width=2)
        dwg.add(dwg.polygon(points=points, stroke="black", fill="none"))
    # SVGファイルに保存
    dwg.save()
    return canvas
    # 画像を保存（必要に応じて）にゃん

def is_white_canvas(image):
    width, height = image.size
    white_pixel = (255, 255, 255)

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel != white_pixel:
                return False
    return True

def delete_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# ディレクトリ内のファイルを削除
directory_path_img = "./out_img"
delete_files_in_directory(directory_path_img)
directory_path_svg = "./out_svg"
delete_files_in_directory(directory_path_svg)

for i in range(1, 1000):
    canvas = draw_image(i)
    result = is_white_canvas(canvas)
    if not result:
        canvas.save(f"./out_img/random_shapes_{i}.png")

# canvas = draw_image(0)
# canvas.save("./random_shapes_"+str(0)+".png")
