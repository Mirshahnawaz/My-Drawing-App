from tkinter import *
from turtle import *
import turtle



def new_window():
    
    
    def window2():

        def Draw1():
            
            turtle.bgcolor('black')

            piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200),
                     (-170, 100), (-160, 40), (-170, 10), (-150, -10),
                     (-140, 10), (-40, -20), (0, -20)],
                    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10),
                     (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
                     (40, 120), (0, 120)]]

            piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0),
                     (-186, -30), (-186, -40), (-120, -170), (-110, -210),
                     (-80, -230), (-64, -210), (0, -210)],
                    [(0, -210), (64, -210),
                     (80, -230), (110, -210), (120, -170), (186, -40), (186, -30),
                     (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]

            piece3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280),
                     (-60, -260), (-30, -260), (-20, -250), (0, -250)],
                    [(0, -250), (20, -250),
                     (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240),
                     (60, -220), (0, -220)]]

            piece1goto = (0,120)
            piece2goto = (0,-30)
            piece3goto = (0,-220)

            def draw_piece(piece,piecegoto):
                turtle.penup()
                turtle.goto(piecegoto)
                turtle.pendown()
                turtle.color('red')
                turtle.begin_fill()
                for i in range(len(piece[0])):
                    x,y =piece[0][i]
                    turtle.goto(x,y)

                for i in range(len(piece[1])):
                    x,y=piece[1][i]
                    turtle.goto(x,y)

                turtle.end_fill()

            draw_piece(piece1,piece1goto)
            draw_piece(piece2,piece2goto)
            draw_piece(piece3,piece3goto)

            turtle.hideturtle()
            turtle.done()
        def Draw2():

            turtle.bgcolor('black')
            def circle(radius,color):
                turtle.color(color)
                turtle.begin_fill()
                turtle.circle(radius)
                turtle.end_fill()
                
            turtle.goto(-30,-280)
            circle(300,'red')

            turtle.goto(-30,-240)
            circle(260,'white')

            turtle.goto(-30,-200)
            circle(220,'red')

            turtle.goto(-30,-160)
            circle(180,'blue')

            turtle.goto(-200,75)
            turtle.begin_fill()
            turtle.color('white')

            for i in range(5):
                turtle.forward(340)
                turtle.right(144)
            turtle.end_fill()

            turtle.hideturtle()
            turtle.done()



        def Draw3():

            turtle.bgcolor('black')
            
            

            def my_goto(x, y):
                penup()
                goto(x, y)
                pendown()
                
            def eyes():
                
                fillcolor("#ffffff")
                begin_fill()

                tracer(False)
                a = 2.5
                for i in range(120):
                    if 0 <= i < 30 or 60 <= i < 90:
                        a -= 0.05
                        lt(3)
                        fd(a)
                    else:
                        a += 0.05
                        lt(3)
                        fd(a)
                tracer(True)
                end_fill()

            def whisker():
                my_goto(-32, 135)
                seth(165)
                fd(60)

                my_goto(-32, 125)
                seth(180)
                fd(60)

                my_goto(-32, 115)
                seth(193)
                fd(60)

                my_goto(37, 135)
                seth(15)
                fd(60)

                my_goto(37, 125)
                seth(0)
                fd(60)

                my_goto(37, 115)
                seth(-13)
                fd(60)

            def mouth():
                my_goto(5, 148)
                seth(270)
                fd(100)
                seth(0)
                circle(120, 50)
                seth(230)
                circle(-120, 100)

            def belt():
                fillcolor('#e70010')
                begin_fill()
                seth(0)
                fd(200)
                circle(-5, 90)
                fd(10)
                circle(-5, 90)
                fd(207)
                circle(-5, 90)
                fd(10)
                circle(-5, 90)
                end_fill()

            def nose():
                my_goto(-10, 158)
                seth(315)
                fillcolor('#e70010')
                begin_fill()
                circle(20)
                end_fill()

            def black_eyes():
                seth(0)
                my_goto(-20, 195)
                fillcolor('#000000')
                begin_fill()
                circle(13)
                end_fill()

                pensize(6)
                my_goto(20, 205)
                seth(75)
                circle(-10, 150)
                pensize(3)
                my_goto(-17, 200)
                seth(0)
                fillcolor('#ffffff')
                begin_fill()
                circle(5)
                end_fill()
                my_goto(0, 0)

            def face():
                fd(183)
                lt(45)
                fillcolor('#ffffff')
                begin_fill()
                circle(120, 100)
                seth(180)

                fd(121)
                pendown()
                seth(215)
                circle(120, 100)
                end_fill()
                my_goto(63.56, 218.24)
                seth(90)
                eyes()
                seth(180)
                penup()
                fd(60)
                pendown()
                seth(90)
                eyes()
                penup()
                seth(180)
                fd(64)

            def head():
                penup()
                circle(150, 40)
                pendown()
                fillcolor('#00a0de')
                begin_fill()
                circle(150, 280)
                end_fill()

            def body():
                my_goto(0, 0)
                seth(0)
                penup()
                circle(150, 50)
                pendown()
                seth(30)
                fd(40)
                seth(70)
                circle(-30, 270)

                fillcolor('#00a0de')
                begin_fill()

                seth(230)
                fd(80)
                seth(90)
                circle(1000, 1)
                seth(-89)
                circle(-1000, 10)

                seth(180)
                fd(70)
                seth(90)
                circle(30, 180)
                seth(180)
                fd(70)

                seth(100)
                circle(-1000, 9)

                seth(-86)
                circle(1000, 2)
                seth(230)
                fd(40)

                circle(-30, 230)
                seth(45)
                fd(81)
                seth(0)
                fd(203)
                circle(5, 90)
                fd(10)
                circle(5, 90)
                fd(7)
                seth(40)
                circle(150, 10)
                seth(30)
                fd(40)
                end_fill()

            def arms():
                seth(70)
                fillcolor('#ffffff')
                begin_fill()
                circle(-30)
                end_fill()

                my_goto(103.74, -182.59)
                seth(0)
                fillcolor('#ffffff')
                begin_fill()
                fd(15)
                circle(-15, 180)
                fd(90)
                circle(-15, 180)
                fd(10)
                end_fill()

                my_goto(-96.26, -182.59)
                seth(180)
                fillcolor('#ffffff')
                begin_fill()
                fd(15)
                circle(15, 180)
                fd(90)
                circle(15, 180)
                fd(10)
                end_fill()

                my_goto(-133.97, -91.81)
                seth(50)
                fillcolor('#ffffff')
                begin_fill()
                circle(30)
                end_fill()

            def pocket():
                my_goto(-103.42, 15.09)
                seth(0)
                fd(38)
                seth(230)
                begin_fill()
                circle(90, 260)
                end_fill()

                my_goto(5, -40)
                seth(0)
                fd(70)
                seth(-90)
                circle(-70, 180)
                seth(0)
                fd(70)

            def bell():
                my_goto(-103.42, 15.09)
                fd(90)
                seth(70)
                fillcolor('#ffd200')
                begin_fill()
                circle(-20)
                end_fill()
                seth(170)
                fillcolor('#ffd200')
                begin_fill()
                circle(-2, 180)
                seth(10)
                circle(-100, 22)
                circle(-2, 180)
                seth(180 - 10)
                circle(100, 22)
                end_fill()
                goto(-13.42, 15.09)
                seth(250)
                circle(20, 110)
                seth(90)
                fd(15)
                dot(10)
                my_goto(0, -150)




            pensize(3)
            speed(8)
            head()
            belt()
            face()
            nose()
            mouth()
            whisker()
            body()
            arms()
            pocket()
            bell()
            black_eyes()
            penup()
            goto(100, -300)
            ht()
            done()








        window2 = Toplevel(window)

        window2.geometry("1000x600")
        window2.title('MY DRAWING APP')
        window2.iconbitmap(r'icon.ico')
        window2.configure(bg = "#ffffff")
        canvas = Canvas(
            window2,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"background2.png")
        background = canvas.create_image(
            500.0, 300.0,
            image=background_img)

        img0 = PhotoImage(file = f"img0.png")
        b0 = Button(window2,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Draw1,
            relief = "flat")

        b0.place(
            x = 86, y = 416,
            width = 123,
            height = 68)

        img1 = PhotoImage(file = f"img1.png")
        b1 = Button(window2,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = Draw2,
            relief = "flat")

        b1.place(
            x = 444, y = 414,
            width = 113,
            height = 65)

        img2 = PhotoImage(file = f"img2.png")
        b2 = Button(window2,
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = Draw3,
            relief = "flat")

        b2.place(
            x = 786, y = 411,
            width = 123,
            height = 73)

        window2.resizable(False, False)
        window2.mainloop()

    
    
    window2()

window = Tk()

window.geometry("1000x600")
window.title('MY DRAWING APP')
window.iconbitmap(r'icon.ico')
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    514.5, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"button1.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = new_window,
    relief = "flat")

b0.place(
    x = 602, y = 320,
    width = 220,
    height = 65)

window.resizable(False, False)
window.mainloop()
