import turtle as t
import random

# colors = colorgram.extract("paintingHirst.jpg", 9)
#
# colors_rgb_mode = []
# for color in colors:
#     color_in_rgb = color.rgb
#     color_set = (color_in_rgb.r, color_in_rgb.g, color_in_rgb.b)
#     colors_rgb_mode.append(color_set)

# colors list extracted from colorgram module using an image
colors = [(244, 241, 239), (79, 163, 101), (222, 218, 64), (181, 177, 100), (242, 230, 235), (59, 102, 158),
          (199, 67, 42), (206, 90, 61), (176, 24, 36)]

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
pos_val_of_y = -250


def paint_row():
    """turtle paints a row of dots, size of 20 and in between each, a space of 50. there are 10 dots in 1 row"""
    for _ in range(10):
        # the turtle draws dot
        tim.pendown()
        tim.dot(20, random.choice(colors))

        # the turtle gets into position to draw dot
        tim.penup()
        tim.forward(50)
    return


def config_position(num):
    """configures the position of the turtle using the x and y-axis of a grid"""
    num += 50
    tim.setposition(-250, num)
    return num


# getting in position to draw
tim.penup()
tim.setposition(-250, -250)

# the turtle begins to paint
for _ in range(10):
    # turtle paints a row
    paint_row()
    # turtle gets into position while painting
    pos_val_of_y = config_position(pos_val_of_y)

screen = t.Screen()
screen.exitonclick()
