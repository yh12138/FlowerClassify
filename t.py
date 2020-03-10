import base64
import tensorflow as tf

def ImgToResult(img):
    result=''
    img_path='image/'+img+'.jpg'
    with open(img_path, 'rb') as f:
        result = base64.b64encode(f.read())
    return result
