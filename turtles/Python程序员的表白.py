import turtles
import time


# 画爱心的顶部
def LittleHeart():
    for i in range(200):
        turtles.right(1)
        turtles.forward(2)


# 输入表白的语句，默认I Love you
love = input('请输入表白语句，默认为输入为"I Love you": ')
# 输入署名或者赠谁，没有不执行
name = input('请输入您心上人的姓名或者昵称: ')
if love == '':
    love = 'I Love you'
# 窗口大小
turtles.setup(width=800, height=500)
# 颜色
turtles.color('red', 'pink')
# 笔粗细
turtles.pensize(5)
# 速度
turtles.speed(1)
# 提笔
turtles.up()
# 隐藏笔
turtles.hideturtle()
# 去到的坐标,窗口中心为0,0
turtles.goto(0, -180)
turtles.showturtle()
# 绘制左下的边
turtles.down()
turtles.speed(1)
turtles.begin_fill()
turtles.left(140)
turtles.forward(224)
# 调用绘制爱心左边的顶部
LittleHeart()
# 调用绘制爱心右边的顶部
turtles.left(120)
LittleHeart()
# 绘制右下的边
turtles.forward(224)
turtles.end_fill()
turtles.pensize(5)
turtles.up()
turtles.hideturtle()
# 在心中写字 一次
turtles.goto(0, 0)
turtles.showturtle()
turtles.color('#CD5C5C', 'pink')
# 在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置
turtles.write(love, font=('华文新魏', 30,), align="center")
turtles.up()
turtles.hideturtle()
time.sleep(2)
# 在心中写字 二次，实现阴影的效果
turtles.goto(0, 0)
turtles.showturtle()
turtles.color('red', 'pink')
turtles.write(love, font=('华文新魏', 30,), align="center")
turtles.up()
turtles.hideturtle()
# 绘制署名
if name != '':
    turtles.color('black', 'pink')
    time.sleep(2)
    turtles.goto(180, -180)
    turtles.showturtle()

    turtles.write(name, font=("Arial Rounded MT Bold", 20,), align="center", move=True)

# 点击窗口关闭
window = turtles.Screen()
window.exitonclick()