import base64
image_path = "flower_photos/daisy/488202750_c420cbce61.jpg"
def base64ToBitmap(str):
    img = base64.b64decode(str)
    return img


# 将图片encode为二进制字符串方法一
def imgTobase64_1(image_path):
    with open(image_path, 'rb') as f:
        str = base64.b64encode(f.read())
    print(str)

# 将图片encode为二进制字符串方法二
def imgTobase64_2(image_path):
    f = open(image_path, 'rb')
    f_str = base64.b64encode(f.read())
    f.close()
    print(type(f_str))

# 将二进制字符串（图片）decode为图片
def base64Toimg(f_str):
    str = f_str
    file_str = open('2.jpg', 'wb')
    file_str.write(base64.b64decode(str))
    file_str.close()
