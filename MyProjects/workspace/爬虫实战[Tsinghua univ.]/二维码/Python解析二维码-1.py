#-*-coding=utf-8-*-
import os 
import logging
from PIL import Image 
import zxing
import random
def ocr_qrcode_zxing(filename):
    #在当前目录生成临时文件
    img= Image.open(filename)
    ran= int(random.random()*100000)
    img.save('%s%s.jpg' %(os.path.basename(filename).split('.')[0],ran))
    zx = zxing.BarCodeReader()
    data =''
    zxdata = zx.decode('%s%s.jpg' %(os.path.basename(filename).split('.')[0],ran))
    #删除临时文件
    os.remove('%s%s.jpg' %(os.path.basename(filename).split('.')[0],ran))
    if zxdata:
        print(u'zxing识别二维码:%s,内容: %s' %(filename ,zxdata.data))
        data = zxdata.data
    else:
        print(u'识别zxing二维码出错:%s' %(filename))
        img.save('%s-zxing.jpg' %filename)  
    return data
if __name__ == '__main__': 
    filename ='xinxing.png-zxing.jpg'
    #zxing二维码识别
    ltext = ocr_qrcode_zxing(filename)
    print( u'[%s]Zxing二维码识别:[%s]!!!' %(filename,ltext))
    print(ltext)
