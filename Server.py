from socket import *
from time import ctime
import label_image
import bitmapTranferBase64
# 1 定义域名和端口号  192.168.1.104     192.168.43.172
HOST,PORT ='',666
# 2 定义缓冲区(缓存)
BUFFER_SIZE = 409600
ADDR=(HOST,PORT)
# 3 创建服务器套接字 AF_INET:IPv4  SOCK_STREAM:协议
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
# 4 绑定域名和端口号
tcpServerSocket.bind(ADDR)
# 5 监听连接  最大连接数
tcpServerSocket.listen(6)
# 6 定义一个循环 目的:等待客户端的连接
print('服务器创建成功，等待客户端的连接。。。')
while True:
	# 6.1 打开一个客户端对象 同意连接
	tcpClientSocket,addr = tcpServerSocket.accept()
	print('连接服务器的客户端对象',addr)
	#6.2 接收数据
	while True:
		#6.3 拿到数据
		data=tcpClientSocket.recv(BUFFER_SIZE).decode()
		if not data:
			break
		print('data=',data)
		print('len=', len(data))
		#识别
		img=bitmapTranferBase64.base64ToBitmap(data)
		result=label_image.predict(img)
		print(len(result))
		#6.4 发送数据
		tcpClientSocket.send(('%s'%(result)).encode())
	# 7 关闭资源
	tcpClientSocket.close()
tcpServerSocket.close()




