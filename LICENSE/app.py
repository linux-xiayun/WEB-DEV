#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

#处理函数index
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8')

#decorator装饰器:init = asyncio.coroutine(init)
#@asyncio.coroutine把一个generator标记为coroutine类型，然后，就把这个coroutine扔到eventloop中去执行
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop) #创建WEB服务器 app
    # 将处理函数index 注册进其应用路径(Application.router)add_route(method, path, handler, *, name=None, expect_handler=None)，该方法将处理函数（其参数名为handler）与对应的URL（HTTP方法metho，URL路径path）绑定，浏览器敲击URL时返回处理函数的内容
    app.router.add_route('GET', '/', index)
    # yield from 返回一个创建好的，绑定IP、端口、HTTP协议簇的监听服务的协程。yield from的作用是使srv的行为模式和 loop.create_server()一致
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000) #yield from 返回一个创建好的，绑定IP、端口、HTTP协议簇的监听服务的协程。yield from的作用是使srv的行为模式和 loop.create_server()一致
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop() #loop = asyncio.get_event_loop()，为asyncio.BaseEventLoop的对象，协程的基本单位
loop.run_until_complete(init(loop)) #运行协程，直到完成，BaseEventLoop.run_until_complete(future)
loop.run_forever() #运行协程，直到调用 stop()，BaseEventLoop.run_forever()



