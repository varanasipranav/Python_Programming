import turtle as t
t.speed('fastest')
def Img1():
    t.pensize(2)
    c=['red','light green','blue']
    for i in range(12):
        t.color(c[i%3])
        t.circle(75)
        t.right(30)
    t.mainloop()
Img1()
