from PIL import Image
img1 = Image.open("kc1.jpg")
img2 = Image.open("kc2.jpg")
img2 = img2.resize(img1.size)

# 分割
r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()

tmp = [r1, g1, b2]
img = Image.merge('RGB', tmp)
img.show()