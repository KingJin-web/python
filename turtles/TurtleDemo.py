# @Description	: 使用turtle模块绘制奥运五环
# @Author		: 老九学堂·窖头
# @Copyright	：http://www.xuetang9.com
# @Version		: 1.0

import turtles

turtles.width(2)
turtles.fillcolor("violet")
turtles.circle(2)

turtles.width(10)	#增加画笔的宽度

turtles.color("blue")
turtles.circle(50)

turtles.color("black")
turtles.penup()
turtles.goto(120, 0)
turtles.pendown()
turtles.circle(50)

turtles.color("red")
turtles.penup()
turtles.goto(240, 0)
turtles.pendown()
turtles.circle(50)

turtles.color("yellow")
turtles.penup()
turtles.goto(60, -50)
turtles.pendown()
turtles.circle(50)

turtles.color("green")
turtles.penup()
turtles.goto(180, -50)
turtles.pendown()
turtles.circle(50)

# 点击窗口关闭
window = turtles.Screen()
window.exitonclick()
