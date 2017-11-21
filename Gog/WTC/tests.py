# from django.test import TestCase
#!/usr/bin/env python
# coding:utf8

import time
import os
import sys
import subprocess

workdir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(workdir)


def fn8(IP):
    import socket
    for ip in ('115.236.19.25', '115.236.19.29'):
        for i in range(5):
            info = ''
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(30)
                s.connect((ip, 9090))
                s.sendall(open('./upload_client_login.bin', 'rb').read())
                r = s.recv(2048)
                s.close()
                if r == open('./result_weberror.bin', 'rb').read():
                    print("%s 调用接口失败" % ip)
                    break
                elif r == open('./result.bin', 'rb').read():
                    print("%s 登录正常" % ip)
                    break
            except BaseException as e:
                info = "登录超时"

            if i >= 2:
                # error notify
                print("上传客户端不能登陆了 %s%s" % (ip, info))
                if ip == IP:
                    subprocess.call("/etc/init.d/UploadServer restart", shell=True)
                else:
                    break
            time.sleep(1)

if __name__ == "__main__":
    IP = "115.236.19.29"
    print(time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time())))
    fn8(IP)
#    time.sleep(3)