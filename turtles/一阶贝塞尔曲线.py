# -*- coding:utf-8 -*-
# @功能描述：使用turtle绘制一阶贝塞尔曲线
# @程序作者：老九学堂·窖头
# @版权信息：http://www.xuetang9.com
# @版本信息：0.0.1

from MagicFunctions import *
import turtle
import time

# 定义开始和结束的两个点坐标
x1, y1 = 0, 0
x2, y2 = 100, -100
speed = 1           # 移动速度
show_count = 20     # 贝塞尔函数的取样次数
turtle.setup(500, 400, 0, 0)
turtle.pensize(1)
turtle.speed(1)
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
for t in range(0, show_count + 1):              # 取样15次
    curr_x = Bezier(x1, x2, t / show_count)
    curr_y = Bezier(y1, y2, t / show_count)
    turtle.goto(curr_x, curr_y)
turtle.penup()
turtle.goto(curr_x, curr_y - 40)
turtle.write("一阶贝塞尔曲线绘制的线段", font=('华文新魏', 18,), align="right")
turtle.done()


