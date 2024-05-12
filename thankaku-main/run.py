from PIL import Image
import random
import math
from itertools import chain
from collections import OrderedDict

# 画像を読み込む
img = Image.open('./resource/input.png')

# 画像のサイズを取得する
width, height = img.size

# RGB値を指定 (red, green, blue)
color = (0, 0, 255) # この例では赤色

# 点の座標を保持するリスト
points = []

# 100個のランダムな点を打つ
for _ in range(100):

    # 1から10までのランダムな整数を生成する
    x_pos = random.randint(0, width - 1)
    y_pos = random.randint(0, height - 1)
    # ピクセルの位置を指定 (x座標, y座標)
    position = (x_pos, y_pos)
    
    # 点の座標をリストに追加
    points.append(position)

for point in points:

    # 指定した位置に指定した色のドットを打つ
    img.putpixel(point, color)

# すべての点のペアについて距離を計算し、最小距離を持つ点のペアを見つける
min_distance = float('inf')  # 初期距離を無限大に設定

for point in points:
    closest_points_most_near = None
    closest_points_second_from_top = None

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # 2点間の距離を計算
            distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)

            # もし新たに計算した距離が現在の最小距離より小さければ更新する
            if distance < min_distance:
                min_distance = distance
                closest_points_second_from_top = closest_points_most_near
                closest_points_most_near = (points[i], points[j])

    rectangle_points_complex = [closest_points_second_from_top, closest_points_most_near]

    # リストを平坦化し、各要素をタプルに変換
    flattened = list(chain.from_iterable(rectangle_points_complex))
    flattened = [tuple(lst) for lst in flattened]

    # 重複要素を削除しながら順序を保つ
    unique = list(OrderedDict.fromkeys(flattened))

    # 最後に、リストのリストに戻す
    rectangle_points = [list(lst) for lst in unique]
    print(rectangle_points)

    # 3つの点の重心を計算
    centroid_x = sum(p[0] for p in points) // 3
    centroid_y = sum(p[1] for p in points) // 3
    centroid = (centroid_x, centroid_y)

# 重心の座標を表示
print("Centroid:", centroid)

# 画像を保存する（必要な場合）
img.save('./output/output.png')