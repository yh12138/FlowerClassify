import os, sys
import tensorflow as tf
import base64
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# change this as you see fit
#image_path = "flower_photos/daisy/488202750_c420cbce61.jpg"
def predict(img):
    #结果
    result = ''
    #读取图片
    #image_data = tf.gfile.FastGFile(img, 'rb').read()
    image_data=img
    # 得到库中花卉种类
    label_lines = [line.rstrip() for line in tf.io.gfile.GFile("model/output_labels.txt")]

    #加载模型
    with tf.io.gfile.GFile("model/output_graph.pb", 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.compat.v1.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        #得到结果
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        #得到结果排序
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        #输出前三个结果
        i=0

        for node_id in top_k:
            if i==3:
                break
            i=i+1
            #结果
            human_string = label_lines[node_id]
            #图片base64
            baseimg=ImgToResult(human_string)

            #识别率
            score = predictions[0][node_id]
            score = "%.2f%%" % (score* 100)#百分数
            result=result+'%s;%s;%s;'%(baseimg,human_string, score)
            print('结果是%s' % result)
    print('结果是%s'%result)
    return result
#将图片转为base64
def ImgToResult(img):
    result=''
    img_path='image/'+img+'.jpg'
    with open(img_path, 'rb') as f:
        result = base64.b64encode(f.read())
        image = result.decode()
    return image
