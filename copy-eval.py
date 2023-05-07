from PIL import Image

img1 = Image.open('kc1.jpg')
# img1.show()
# 按像素缩放图片
# 将每个像素都扩大2倍
# Image.eval(img1, lambda x: x*2).show()

# 按尺寸进行缩放图片
# 复制图片
# img2 = img1.copy()
# img1.show()
# img2.thumbnail((800, 600))
# img2.show()

# 粘贴和裁剪
imgb = img1.copy()
imgc = img1.copy()

imgb_crop = imgb.crop((200, 200, 450, 450))
imgc.paste(imgb_crop, (30, 30))
imgc.show()