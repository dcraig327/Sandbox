import turtle

MOVE_DISTANCE = 20
STARTING_OFFSET_X = 0
STARTING_OFFSET_Y = 0
STARTING_POSITIONS = [(STARTING_OFFSET_X, STARTING_OFFSET_Y), (-MOVE_DISTANCE + STARTING_OFFSET_X, STARTING_OFFSET_Y),
                      ((-MOVE_DISTANCE * 2) + STARTING_OFFSET_X, STARTING_OFFSET_Y)]
ANGLE_UP = 90
ANGLE_LEFT = 180
ANGLE_RIGHT = 0
ANGLE_DOWN = 270


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.segments = []
        self.head = None
        self.tail = None
        self.user_input = False
        self.growing = False
        self.create_snake()

    def create_snake(self):
        for p in STARTING_POSITIONS:
            self.add_segment(p)

    def reset(self):
        self.growing = False
        for seg in self.segments:
            seg.reset()
        self.segments.clear()           # segments = []
        self.head = None
        self.tail = None
        self.create_snake()

    def add_segment(self, position):
        t = turtle.Turtle(shape="square")
        t.hideturtle()
        t.penup()
        t.color("white")
        t.goto(position)
        t.speed(0)
        t.showturtle()
        self.segments.append(t)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def grow(self):
        self.growing = True

    def move(self):
        if not self.segments:
            return
        tail_location = len(self.segments) - 1
        if self.growing:
            self.add_segment(self.tail.position())
            self.growing = False
        for n in range(tail_location, 0, -1):
            p = self.segments[n - 1].position()
            self.segments[n].goto(p)
        self.head.forward(MOVE_DISTANCE)
        self.user_input = False

    def up(self):
        if self.head.heading() != ANGLE_DOWN and not self.user_input:
            self.head.setheading(ANGLE_UP)
            self.user_input = True

    def down(self):
        if self.head.heading() != ANGLE_UP and not self.user_input:
            self.head.setheading(ANGLE_DOWN)
            self.user_input = True

    def left(self):
        if self.head.heading() != ANGLE_RIGHT and not self.user_input:
            self.head.setheading(ANGLE_LEFT)
            self.user_input = True

    def right(self):
        if self.head.heading() != ANGLE_LEFT and not self.user_input:
            self.head.setheading(ANGLE_RIGHT)
            self.user_input = True
