# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:44:12 2021

@author: yuzt
"""
from PIL import Image
import qrcode
import matplotlib.pyplot as plt
def qrCode1():
    qr=qrcode.QRCode(
         version=6,
         error_correction=qrcode.constants.ERROR_CORRECT_H,
         box_size=10,
         border=1
        )
    # 调用qrcode的make()方法传入url或者想要展示的内容
    qr.add_data("今天是七夕，我在上图")
    qr.make(fit=True)# 填充数据        
    img = qr.make_image(fill_color="green", back_color="white")
    img = img.convert("RGBA")
    # 添加logo，打开logo照片
    icon = Image.open("yzt.jpg").convert("RGBA")
    # 获取图片的宽和搞
    img_w, img_h = img.size
    # 参数设置logo的大小
    factor = 3
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
     # 得到画图的x，y坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    '''
    img.paste(path,where,mask=None)
    其中，img为image对象；path为所添加图片；where为tuple,如：(x,y)，表示图片所在二维码的横纵坐标
    '''
    # 黏贴logo照
    img.paste(icon, (w, h), icon)
    img.save("我的CSDN二维码.png")
    # img.show()# 自动打开图片
    # 终端显示图片
    plt.imshow(img)
    plt.show()

if __name__=='__main__':
    qrCode1()