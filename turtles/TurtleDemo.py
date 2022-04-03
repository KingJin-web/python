# @Description	: 使用turtle模块绘制奥运五环
# @Author		: 老九学堂·窖头
# @Copyright	：http://www.xuetang9.com
# @Version		: 1.0

import turtle

turtle.width(2)
turtle.fillcolor("violet")
turtle.circle(2)

turtle.width(10)	#增加画笔的宽度

turtle.color("blue")
turtle.circle(50)

turtle.color("black")
turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.circle(50)

turtle.color("red")
turtle.penup()
turtle.goto(240, 0)
turtle.pendown()
turtle.circle(50)

turtle.color("yellow")
turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
turtle.circle(50)

turtle.color("green")
turtle.penup()
turtle.goto(180, -50)
turtle.pendown()
turtle.circle(50)

# 点击窗口关闭
window = turtle.Screen()
window.exitonclick()
