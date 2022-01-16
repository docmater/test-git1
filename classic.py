import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #绘制单段数码管
    turtle.speed(1000000000)
    drawGap()
    turtle.pendown()
    turtle.pencolor("black") if draw else turtle.pencolor("white")
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    for i in date:
        if i == '&':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '*':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '$':
            turtle.write('日',font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '-':
            turtle.write('时',font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '=':
            turtle.write('分',font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '+':
            turtle.pencolor("black")
            turtle.write('秒',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-650)
    turtle.pensize(5)
    btome = datetime.datetime.now().strftime('%Y&%m*%d$%H-%M=%S+')
    global btomes
    btomes = datetime.datetime.now().strftime('%H-%M=%S+')
    drawDate(btome)
    turtle.hideturtle()

va = 1
main()
a = eval(datetime.datetime.now().strftime('%M'))
while va == 1:
    while eval(datetime.datetime.now().strftime('%M')) == a:
        turtle.goto(390, 0)
        drawDate(datetime.datetime.now().strftime('%S+'))
        turtle.goto(390, 0)
    while eval(datetime.datetime.now().strftime('%M')) != a:
        turtle.goto(210,0)
        drawDate(datetime.datetime.now().strftime('%M=%S+'))
        turtle.goto(210,0)
        a = eval(datetime.datetime.now().strftime('%M'))








