import turtle


def space(turtle_obj):
    """
    The function add a 50 pixels space between letters.
    :param turtle_obj: the turtle object.
    :type turtle_obj: turtle.Turtle()
    :return: None
    :rtype: None
    """
    turtle_obj.penup()
    turtle_obj.forward(50)


def letter_A(turtle_obj, first):
    """
    The function draw the letter A.
    :param turtle_obj: the turtle object.
    :type turtle_obj: turtle.Turtle()
    :param first: this is the first element in the line or not.
    :type first: bool
    :return:None
    :rtype:None
    """
    if not first:
        turtle_obj.forward(50)

    turtle_obj.pendown()

    # \
    turtle_obj.right(65)
    turtle_obj.forward(115)

    # \
    turtle_obj.right(360)
    turtle_obj.backward(115)

    # /
    turtle_obj.right(50)
    turtle_obj.forward(115)

    # half /
    turtle_obj.left(360)
    turtle_obj.backward(50)

    # -
    turtle_obj.right(65)
    turtle_obj.backward(55)

    # half \
    turtle_obj.right(65)
    turtle_obj.backward(50)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(25)
    turtle_obj.forward(105)
    turtle_obj.right(90)


def letter_B(turtle_obj):
    """ The function draw the letter B. """

    turtle_obj.pendown()

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)

    # lower )
    turtle_obj.right(90)
    turtle_obj.circle(-25, -180)

    # upper )
    turtle_obj.right(180)
    turtle_obj.circle(-25, -180)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.forward(25)


def letter_C(turtle_obj):
    """ The function draw the letter C. """

    # take a bit forward because it's a big letter
    turtle_obj.penup()
    turtle_obj.forward(50)
    turtle_obj.pendown()

    # draw circle
    turtle_obj.right(180)
    turtle_obj.circle(50, 180)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(90)
    turtle_obj.forward(100)
    turtle_obj.right(90)


def letter_D(turtle_obj):
    """ The function draw the letter D. """

    turtle_obj.pendown()

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)

    # )
    turtle_obj.right(90)
    turtle_obj.circle(-50, -180)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.forward(50)


def letter_E(turtle_obj):
    """ The function draw the letter E. """

    turtle_obj.pendown()

    # upper -
    turtle_obj.forward(50)
    turtle_obj.backward(50)
    turtle_obj.right(90)

    # upper |
    turtle_obj.forward(50)
    turtle_obj.left(90)

    # middle -
    turtle_obj.forward(50)
    turtle_obj.backward(50)
    turtle_obj.right(90)

    # lower |
    turtle_obj.forward(50)
    turtle_obj.left(90)

    # bottom -
    turtle_obj.forward(50)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(90)
    turtle_obj.forward(100)
    turtle_obj.right(90)


def letter_F(turtle_obj):
    """ The function draw the letter F. """

    turtle_obj.pendown()

    # upper -
    turtle_obj.forward(50)
    turtle_obj.backward(50)
    turtle_obj.right(90)

    # upper |
    turtle_obj.forward(50)
    turtle_obj.left(90)

    # bottom -
    turtle_obj.forward(50)
    turtle_obj.backward(50)
    turtle_obj.right(90)

    # bottom |
    turtle_obj.forward(50)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(180)
    turtle_obj.forward(100)
    turtle_obj.right(90)
    turtle_obj.forward(50)


def letter_G(turtle_obj):
    """ The function draw the letter G. """

    # take a bit forward because it's a big letter
    turtle_obj.forward(50)

    turtle_obj.pendown()

    # (
    turtle_obj.right(180)
    turtle_obj.circle(50, 180)

    # the little |
    turtle_obj.left(90)
    turtle_obj.forward(50)
    turtle_obj.right(90)

    # -
    turtle_obj.backward(25)
    turtle_obj.forward(50)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(90)
    turtle_obj.forward(50)
    turtle_obj.right(90)


def letter_H(turtle_obj):
    """ The function draw the letter H. """

    turtle_obj.pendown()

    # left |
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.backward(50)

    # -
    turtle_obj.left(90)
    turtle_obj.forward(50)
    turtle_obj.left(90)

    # right |
    turtle_obj.backward(50)
    turtle_obj.forward(100)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(90)


def letter_I(turtle_obj):
    """ The function draw the letter I. """

    turtle_obj.pendown()

    # upper -
    turtle_obj.forward(20)
    turtle_obj.backward(10)

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.left(90)

    # -
    turtle_obj.forward(10)
    turtle_obj.backward(20)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(90)
    turtle_obj.backward(100)
    turtle_obj.left(90)
    turtle_obj.forward(20)


def letter_J(turtle_obj):
    """ The function draw the letter J. """

    # take a bit forward because it's a big letter
    turtle_obj.forward(20)
    turtle_obj.pendown()

    # -
    turtle_obj.forward(10)
    turtle_obj.right(90)

    # |
    turtle_obj.forward(100)

    # u
    turtle_obj.circle(-30, 180)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.circle(-30, -180)
    turtle_obj.backward(100)
    turtle_obj.left(90)


def letter_K(turtle_obj):
    """ The function draw the letter K. """

    turtle_obj.pendown()

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.backward(50)

    # lower \
    turtle_obj.left(45)
    turtle_obj.forward(70)
    turtle_obj.backward(70)

    # upper /
    turtle_obj.left(90)
    turtle_obj.forward(70)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(45)


def letter_L(turtle_obj):
    """ The function draw the letter L. """

    turtle_obj.pendown()

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)

    # _
    turtle_obj.left(90)
    turtle_obj.forward(60)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(90)
    turtle_obj.forward(100)
    turtle_obj.right(90)


def letter_M(turtle_obj):
    """ The function draw the letter M. """

    # move start position down
    turtle_obj.right(90)
    turtle_obj.forward(100)

    turtle_obj.pendown()

    # |
    turtle_obj.right(180)
    turtle_obj.forward(100)

    # \
    turtle_obj.right(160)
    turtle_obj.forward(90)

    # /
    turtle_obj.left(140)
    turtle_obj.forward(90)

    # |
    turtle_obj.right(160)
    turtle_obj.forward(100)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.backward(100)
    turtle_obj.left(90)


def letter_N(turtle_obj):
    """ The function draw the letter N. """

    # move start position down
    turtle_obj.right(90)
    turtle_obj.forward(100)

    turtle_obj.pendown()

    # |
    turtle_obj.right(180)
    turtle_obj.forward(100)

    # /
    turtle_obj.right(150)
    turtle_obj.forward(115)

    # |
    turtle_obj.left(150)
    turtle_obj.forward(100)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(90)


def letter_O(turtle_obj):
    """ The function draw the letter O. """

    # take a bit forward because it's a big letter
    turtle_obj.penup()
    turtle_obj.forward(50)

    turtle_obj.pendown()

    # ()
    turtle_obj.circle(-50)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.forward(50)


def letter_P(turtle_obj):
    """ The function draw the letter P. """

    turtle_obj.pendown()

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.backward(50)
    turtle_obj.left(90)

    # )
    turtle_obj.circle(25, 180)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(180)
    turtle_obj.forward(25)


def letter_Q(turtle_obj):
    """ The function draw the letter Q. """

    # take a bit forward because it's a big letter
    turtle_obj.forward(50)
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.left(90)

    # ()
    turtle_obj.pendown()
    turtle_obj.circle(50)

    # 、
    turtle_obj.right(45)
    turtle_obj.forward(30)
    turtle_obj.backward(30)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(135)
    turtle_obj.forward(100)
    turtle_obj.right(90)
    turtle_obj.forward(50)


def letter_R(turtle_obj):
    """ The function draw the letter R. """

    turtle_obj.pendown()

    # |
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.right(180)
    turtle_obj.forward(100)

    # )
    turtle_obj.right(90)
    turtle_obj.circle(-25, 180)

    # \
    turtle_obj.pendown()
    turtle_obj.left(135)
    turtle_obj.forward(70)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(135)
    turtle_obj.forward(100)
    turtle_obj.right(90)


def letter_S(turtle_obj):
    """ The function draw the letter S. """

    # move to the right start position
    turtle_obj.right(90)
    turtle_obj.forward(100)

    turtle_obj.pendown()

    # bottom )
    turtle_obj.right(-90)
    turtle_obj.circle(25, -60)
    turtle_obj.circle(25, 60)
    turtle_obj.circle(25, 180)

    # upper (
    turtle_obj.circle(-25, 180)
    turtle_obj.circle(-25, 60)
    turtle_obj.circle(-25, -60)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.forward(25)


def letter_T(turtle_obj):
    """ The function draw the letter T. """

    turtle_obj.pendown()

    # -
    turtle_obj.forward(100)
    turtle_obj.backward(50)
    turtle_obj.right(90)

    # |
    turtle_obj.forward(100)
    turtle_obj.right(180)
    turtle_obj.forward(100)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(90)
    turtle_obj.forward(50)


def letter_U(turtle_obj):
    """ The function draw the letter U. """

    turtle_obj.pendown()

    # left |
    turtle_obj.right(90)
    turtle_obj.forward(75)

    # u
    turtle_obj.circle(25, 180)

    # right |
    turtle_obj.forward(75)

    # move to the right end position
    turtle_obj.right(90)


def letter_V(turtle_obj):
    """ The function draw the letter V. """

    turtle_obj.pendown()

    # \
    turtle_obj.right(65)
    turtle_obj.forward(105)

    # /
    turtle_obj.left(130)
    turtle_obj.forward(105)

    # move to the right end position
    turtle_obj.right(65)


def letter_W(turtle_obj):
    """ The function draw the letter W. """

    turtle_obj.pendown()

    # \
    turtle_obj.right(65)
    turtle_obj.forward(105)

    # /
    turtle_obj.left(130)
    turtle_obj.forward(70)

    # \
    turtle_obj.right(130)
    turtle_obj.forward(70)

    # /
    turtle_obj.left(130)
    turtle_obj.forward(105)

    # move to the right end position
    turtle_obj.right(65)


def letter_X(turtle_obj):
    """ The function draw the letter X. """

    turtle_obj.pendown()

    # \
    turtle_obj.right(50)
    turtle_obj.forward(120)

    # move to the right position
    turtle_obj.penup()
    turtle_obj.right(130)
    turtle_obj.forward(80)
    turtle_obj.pendown()

    # /
    turtle_obj.right(130)
    turtle_obj.forward(120)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.right(50)


def letter_Y(turtle_obj):
    """ The function draw the letter Y. """

    turtle_obj.pendown()

    # \
    turtle_obj.right(65)
    turtle_obj.forward(60)

    # |
    turtle_obj.right(25)
    turtle_obj.forward(40)
    turtle_obj.backward(40)

    # /
    turtle_obj.left(160)
    turtle_obj.forward(60)

    # move to the right end position
    turtle_obj.right(70)
    turtle_obj.penup()


def letter_Z(turtle_obj):
    """ The function draw the letter Z. """

    turtle_obj.pendown()

    # upper -
    turtle_obj.forward(80)

    # /
    turtle_obj.right(135)
    turtle_obj.forward(120)

    # bottom -
    turtle_obj.left(135)
    turtle_obj.forward(80)

    # move to the right end position
    turtle_obj.penup()
    turtle_obj.left(90)
    turtle_obj.forward(85)
    turtle_obj.right(90)


def get_input():
    """
    The function take input from the user and validate it.
    :return: the sentence string.
    :rtype: str
    """
    valid_input = True
    sentence = ''
    while valid_input:
        sentence = turtle.textinput('Input', 'Enter the sentence you would like to write (only A-Z): ')
        if sentence is not None and sentence != '' and sentence != '\n' and sentence.replace(' ', '').isalpha():
            valid_input = False
    return sentence.upper()


def main():
    # Settings
    tur = turtle.Screen()
    tur.bgcolor("black")

    turtle_obj = turtle.Turtle()
    turtle_obj.shape('classic')  # square, arrow, circle, turtle, triangle, classic
    turtle_obj.color("white")
    turtle_obj.pensize(10)

    # Positions
    x_pos = -420
    y_pos = 390

    # Functions dict
    draw = {"A": letter_A, "B": letter_B, "C": letter_C, "D": letter_D, "E": letter_E, "F": letter_F, "G": letter_G,
            "H": letter_H, "I": letter_I, "J": letter_J, "K": letter_K, "L": letter_L, "M": letter_M, "N": letter_N,
            "O": letter_O, "P": letter_P, "Q": letter_Q, "R": letter_R, "S": letter_S, "T": letter_T, "U": letter_U,
            "V": letter_V, "W": letter_W, "X": letter_X, "Y": letter_Y, "Z": letter_Z}

    for word in get_input().split(' '):
        turtle_obj.penup()
        turtle_obj.setx(x_pos)
        turtle_obj.sety(y_pos)

        for index, letter in enumerate(word, start=1):
            if letter in draw.keys():
                if index == 1 and letter == 'A':
                    draw[letter](turtle_obj, True)
                elif letter == 'A':
                    draw[letter](turtle_obj, False)
                else:
                    draw[letter](turtle_obj)
                space(turtle_obj)
        y_pos -= 150
    turtle.exitonclick()


if __name__ == '__main__':
    try:
        main()
    except turtle.Terminator:
        pass
