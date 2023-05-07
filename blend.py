from PIL import Image
img1 = Image.open('kc1.jpg').convert(mode="RGB")
img2 = Image.new("RGB", img1.size, 'blue')


##混合两幅图
Image.blend(img1, img2, alpha=0.5).show()