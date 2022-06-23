import socket  # 导入socket模块

s = socket.socket()  # 创建socket对象
host = '180.215.197.247'  # 设置本地主机
port = 80  # 设置端口


if __name__ == '__main__':
    while True:
        # 1.创建socket
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. 链接服务器
        server_addr = (host, port)
        tcp_socket.connect(server_addr)

        # 3. 发送数据
        send_data = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        tcp_socket.send(send_data.encode("gbk"))
        # 4. 关闭套接字
        tcp_socket.close()
        print(1)