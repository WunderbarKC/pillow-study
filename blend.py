from PIL import Image
# img1 = Image.open('kc1.jpg').convert(mode="RGB")
# img2 = Image.new("RGB", img1.size, 'blue')


# 混合两幅图
# Image.blend(img1, img2, alpha=0.5).show()

# 遮罩混合处理
img1 = Image.open('kc1.jpg')
img2 = Image.open('kc2.jpg')
img2 = img2.resize(img1.size)
r, g, b = img2.split()
Image.composite(img1, img2, b).show()