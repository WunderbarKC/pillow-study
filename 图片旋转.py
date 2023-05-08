from PIL import Image

img = Image.open("./kc1.jpg")
# 图像的旋转
img.rotate(180).show()