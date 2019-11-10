# coding: utf-8
"""
filename: qrcode.py
Created by Tacey Wong at 16-9-22 下午10:34 
"""
import qrcode
from PIL import Image
import os, sys
import zbar

def gen_qrcode(string, path, logo=""):
    """
    生成中间带logo的二维码
    需要安装qrcode, PIL库
    @参数 string: 二维码字符串
    @参数 path: 生成的二维码保存路径
    @参数 logo: logo文件路径
    @return: None
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=1
    )
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    if logo and os.path.exists(logo):
        try:
            icon = Image.open(logo)
            img_w, img_h = img.size
        except Exception as e:
            print(e) 
            sys.exit(1)
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
    img.save(path)
    # 调用系统命令打开图片
    # xdg - open(opens a file or URL in the user's preferred application)
    os.system('xdg-open %s' % path)


def decode_qrcode(path):
    """
    解析二维码信息
    @参数 path: 二维码图片路径
    @return: 二维码信息
    """
    # 创建图片扫描对象
    scanner = zbar.ImageScanner()
    # 设置对象属性
    scanner.parse_config('enable')
    # 打开含有二维码的图片
    img = Image.open(path).convert('L')
    # 获取图片的尺寸
    width, height = img.size
    # 建立zbar图片对象并扫描转换为字节信息
    qrCode = zbar.Image(width, height, 'Y800', img.tobytes())
    scanner.scan(qrCode)
    # 组装解码信息
    data = ''
    for s in qrCode:
        data += s.data
    # 删除图片对象
    del img
    # 输出解码结果
    return data


if __name__ == "__main__":
    info = "http://www.zut.edu.cn"
    pic_path = "qr.png"
    logo_path = "logo.png"
    #gen_qrcode(info, pic_path,logo_path )
    print(decode_qrcode(pic_path))
