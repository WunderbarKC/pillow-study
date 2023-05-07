from PIL import Image

im = Image.open("./c24c52e243547b96018f0b75a75084f.jpg")

im.show()

print('图片格式:', im.format)
print('图片大小，格式是（宽度，高度）：', im.size)
print('图像宽度：', im.width, "图像高度:", im.height)
print('读取坐标在（100， 100）处的像素的信息：', im.getpixel((100, 100)))