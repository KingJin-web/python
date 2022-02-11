# -*- coding:utf-8 -*-
# @功能描述：绘制魔法少女所使用的函数
# @程序作者：老九学堂·窖头
# @版权信息：http://www.xuetang9.com
# @版本信息：0.0.1

import turtles

WriteStep = 15      # 贝塞尔函数的取样次数
Speed = 5
Width = 600         # 界面宽度
Height = 500        # 界面高度
Xh = 0              # 记录前一个贝塞尔函数的手柄
Yh = 0


def Bezier(p0, p1, t):
    """
    一阶贝塞尔函数，由P0至P1的连续点描述的一条线段
    :param p0:  起始点
    :param p1:  终点
    :param t:   时间
    :return:    返回对应时间点的中间坐标值
    """
    return (1 - t) * p0 + t * p1


def Bezier_2(x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
    turtles.goto(x1, y1)
    turtles.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        turtles.goto(x, y)
    turtles.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):  # 三阶贝塞尔函数
    x1 = -Width / 2 + x1
    y1 = Height / 2 - y1
    x2 = -Width / 2 + x2
    y2 = Height / 2 - y2
    x3 = -Width / 2 + x3
    y3 = Height / 2 - y3
    x4 = -Width / 2 + x4
    y4 = Height / 2 - y4  # 坐标变换
    turtles.goto(x1, y1)
    turtles.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        turtles.goto(x, y)
    turtles.penup()


def Moveto(x, y):  # 移动到svg坐标下（x，y）
    turtles.penup()
    turtles.goto(-Width / 2 + x, Height / 2 - y)


def line(x1, y1, x2, y2):  # 连接svg坐标下两点
    turtles.penup()
    turtles.goto(-Width / 2 + x1, Height / 2 - y1)
    turtles.pendown()
    turtles.goto(-Width / 2 + x2, Height / 2 - y2)
    turtles.penup()


def lineto(dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    turtles.pendown()
    turtles.goto(turtles.xcor() + dx, turtles.ycor() - dy)
    turtles.penup()


def Lineto(x, y):  # 连接当前点和svg坐标下（x，y）
    turtles.pendown()
    turtles.goto(-Width / 2 + x, Height / 2 - y)
    turtles.penup()


def Horizontal(x):  # 做到svg坐标下横坐标为x的水平线
    turtles.pendown()
    turtles.setx(x - Width / 2)
    turtles.penup()


def horizontal(dx):  # 做到相对横坐标为dx的水平线
    turtles.seth(0)
    turtles.pendown()
    turtles.fd(dx)
    turtles.penup()


def vertical(dy):  # 做到相对纵坐标为dy的垂直线
    turtles.seth(-90)
    turtles.pendown()
    turtles.fd(dy)
    turtles.penup()
    turtles.seth(0)


def polyline(x1, y1, x2, y2, x3, y3):  # 做svg坐标下的折线
    turtles.penup()
    turtles.goto(-Width / 2 + x1, Height / 2 - y1)
    turtles.pendown()
    turtles.goto(-Width / 2 + x2, Height / 2 - y2)
    turtles.goto(-Width / 2 + x3, Height / 2 - y3)
    turtles.penup()


def Curveto(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    turtles.penup()
    X_now = turtles.xcor() + Width / 2
    Y_now = Height / 2 - turtles.ycor()
    Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def curveto_r(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    turtles.penup()
    # turtles.xcor()是返回(海龟)箭头的x坐标
    print(x1, y1, x2, y2, x, y)
    X_now = turtles.xcor() + Width / 2
    print("x_now = {} + {}".format(turtles.xcor(), Width / 2))
    Y_now = Height / 2 - turtles.ycor()
    Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Smooth(x2, y2, x, y):  # 平滑三阶贝塞尔曲线到（x，y）
    global Xh
    global Yh
    turtles.penup()
    X_now = turtles.xcor() + Width / 2
    Y_now = Height / 2 - turtles.ycor()
    Bezier_3(X_now, Y_now, X_now + Xh, Y_now + Yh, x2, y2, x, y)
    Xh = x - x2
    Yh = y - y2


def smooth_r(x2, y2, x, y):  # 平滑三阶贝塞尔曲线到相对坐标（x，y）
    global Xh
    global Yh
    turtles.penup()
    X_now = turtles.xcor() + Width / 2
    Y_now = Height / 2 - turtles.ycor()
    Bezier_3(X_now, Y_now, X_now + Xh, Y_now + Yh,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    Xh = x - x2
    Yh = y - y2



