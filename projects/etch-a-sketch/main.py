# w - forwards
# s - backwards
# a - counter-clockwise/left
# d - clockwise/right
# c - clear & center
# ESC - quit

from turtle import Turtle, Screen

t = Turtle()
s = Screen()
step = 10


# ESC - quit
def kb_esc():
    s.bye()


# c - clear
def kb_c():
    s.resetscreen()


# w - forward
def kb_w():
    t.forward(step)


# a - left
def kb_a():
#    t.left(step)
    heading = t.heading() + step
    t.setheading(heading)


# s - back
def kb_s():
    t.forward(-step)


# d - right
def kb_d():
    #t.right(step)
    heading = t.heading() - step
    t.setheading(heading)


s.onkey(kb_esc, "Escape")
s.onkeypress(kb_a, "a")
s.onkeypress(kb_s, "s")
s.onkeypress(kb_d, "d")
s.onkeypress(kb_w, "w")
s.onkeypress(kb_c, "c")

s.listen()
s.mainloop()
