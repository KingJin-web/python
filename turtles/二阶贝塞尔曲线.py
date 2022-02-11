# -*- coding:utf-8 -*-
# @功能描述：使用turtle绘制二阶贝塞尔曲线
# @程序作者：老九学堂·窖头
# @版权信息：http://www.xuetang9.com
# @版本信息：0.0.1

from MagicFunctions import *
import turtles
import time


def Bezier_2(p0, p1, p2, t):
    """
    二阶贝塞尔公式函数
    """
    return (1 - t) ** 2 * p0 + 2 * t * (1 - t) * p1 + t ** 2 * p2

# 二阶贝塞尔曲线需要三个控制点
x1, y1 = 0, 0
x2, y2 = 60, 80
x3, y3 = 140, 0
speed = 1           # 移动速度
show_count = 20     # 函数的取样次数

turtles.setup(500, 400, 0, 0)
turtles.pensize(1)
turtles.speed(1)
turtles.penup()
turtles.goto(x1, y1)
turtles.pendown()
for i in range(0, show_count + 1):
    # curr_x = Bezier_2(x1, x2, x3, i / show_count)
    # curr_y = Bezier_2(y1, y2, y3, i / show_count)
    # 也可以使用下面的方式，组合一阶函数来计算
    curr_x = Bezier(
                Bezier(x1, x2, i / show_count),
                Bezier(x2, x3, i / show_count),
                i / show_count
    )
    curr_y = Bezier(
                Bezier(y1, y2, i / show_count),
                Bezier(y2, y3, i / show_count),
                i / show_count
    )

    turtles.goto(curr_x, curr_y)

turtles.done()