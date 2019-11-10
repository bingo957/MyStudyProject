import qrcode
img = qrcode.make("http://www.zut.edu.cn")
img.save("xinxing.png")
