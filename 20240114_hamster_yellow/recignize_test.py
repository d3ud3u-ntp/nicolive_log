from PIL import Image
import csv

# カラーコードのリストを読み込む
with open("colors.tsv", "r") as f:
    csv_reader = csv.reader(f, delimiter="\t")
    color_codes = [row[0] for row in csv_reader]

# 画像を開く
image = Image.open("./frame/frame00001.jpg")

# ピクセルデータをロードする
pixels = list(image.getdata())

# カラーコードのリストに画像中の各ピクセルがあてはまっているか、true/falseで返す
result = []
for pixel in pixels:
    color = "#{:02x}{:02x}{:02x}".format(*pixel)
    result.append(color in color_codes)

# 結果をtsvファイルに書き込む
with open("result.tsv", "w") as f:
    csv_writer = csv.writer(f, delimiter="\t")
    csv_writer.writerow(["is_in_list"])
    for r in result:
        csv_writer.writerow([r])