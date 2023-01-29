from turtle import Turtle, Screen
import turtle
from random import Random, randint, choice

turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    ans = (r, g, b)
    return ans


color_list = [(195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27),
              (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130),
              (121, 35, 40), (182, 98, 82), (207, 202, 146), (144, 176, 161), (178, 150, 156), (176, 202, 188),
              (217, 179, 172), (22, 77, 93), (33, 79, 62), (95, 143, 150), (160, 111, 117), (214, 178, 183),
              (168, 202, 212)]
# joker.speed()
joker = Turtle()
joker.speed('fastest')

joker.rt(45)
joker.penup()
joker.fd(150)

# joker.dot(20, choice(color_list))
joker.rt(135)
joker.fd(300)
# joker.dot(20, choice(color_list))
joker.rt(180)
'''quadaratic time logic'''
# for j in range(10):
#     for i in range(9):
#         joker.dot(20, choice(color_list))
#         joker.fd(50)
#         joker.dot(20, choice(color_list))
#     if j % 2 == 0:
#         joker.lt(90)
#         joker.fd(30)
#         joker.lt(90)
#     else:
#         joker.rt(90)
#         joker.fd(30)
#         joker.rt(90)
# # joker.fd(300)
'''Linear time logic my'''
is_first = True
no_of_dots = 100
for dot_count in range(1, no_of_dots + 1):
    print(dot_count)
    joker.dot(20, choice(color_list))
    joker.fd(50)
    if dot_count % 10 == 0:
        joker.setheading(90)
        joker.fd(50)
        if dot_count % 20 != 0:
            joker.setheading(180)
            joker.fd(50)
        else:

            joker.setheading(0)
            joker.fd(50)
            print(dot_count)

''' angela's logic'''
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#
#     joker.dot(20, choice(color_list))
#     joker.forward(50)
#
#     if dot_count % 10 == 0:
#         joker.setheading(90)
#         joker.forward(50)
#         joker.setheading(180)
#         joker.forward(500)
#         joker.setheading(0)


my_screen = Screen()
my_screen.exitonclick()
